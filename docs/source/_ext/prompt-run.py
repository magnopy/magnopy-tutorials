from __future__ import annotations


from docutils import nodes

from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective
from sphinx.util.typing import ExtensionMetadata

from typing import ClassVar
from docutils.parsers.rst import directives
from sphinx.util.typing import OptionSpec
from docutils.nodes import Element, Node
from sphinx.util import logging

import subprocess
import os


logger = logging.getLogger(__name__)


def run_script(command, options):
    if "extra-command" in options:
        command_to_run = f"{command} {options['extra-command']}"
    else:
        command_to_run = command

    command_to_run = command_to_run.replace("{{IP}}", options["input-prefix"])
    command_to_run = command_to_run.replace("{{OP}}", options["output-prefix"])

    command_to_show = command.replace("{{IP}}", "")
    command_to_show = command_to_show.replace("{{OP}}", "")

    output = subprocess.run(command_to_run.split(" "), capture_output=True, text=True)

    if output.returncode != 0:
        raise ValueError("Script executed with errors.")

    with open(os.path.join(options["output-prefix"], "console-output.txt"), "w") as f:
        f.write(output.stdout)

    return command_to_show


class PromptRun(SphinxDirective):
    """Directive for a prompt block that will be executed."""

    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec: ClassVar[OptionSpec] = {
        "class": directives.class_option,
        "name": directives.unchanged,
        "input-prefix": directives.path,
        "output-prefix": directives.path,
        "extra-command": directives.unchanged_required,
    }

    def run(self) -> list[Node]:
        document = self.state.document
        if len(self.content) != 1:
            return [
                document.reporter.error(
                    ValueError(
                        f"Only one-line commands are supported, got {len(self.content)} lines"
                    ),
                    line=self.lineno,
                )
            ]

        location = self.state_machine.get_source_and_line(self.lineno)
        head, _ = os.path.split(location[0])
        if "input-prefix" in self.options:
            self.options["input-prefix"] = os.path.join(
                head, self.options["input-prefix"]
            )
        if "output-prefix" in self.options:
            self.options["output-prefix"] = os.path.join(
                head, self.options["output-prefix"]
            )

        command = run_script(command=self.content[0], options=self.options)

        literal: Element = nodes.literal_block(command, command)

        literal["classes"] += self.options.get("class", [])

        literal["language"] = "bash"

        self.set_source_info(literal)

        self.add_name(literal)

        return [literal]


def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_directive("prompt-run", PromptRun)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
