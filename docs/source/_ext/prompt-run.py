from __future__ import annotations


from docutils import nodes

from requests import options
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

from pathlib import Path


logger = logging.getLogger(__name__)


def run_script(command, op, ip, extra_command=None):
    def process_command(command_text):
        i = 0
        for_run = ""
        for_show = ""
        while i < len(command_text) - 6:
            if command_text[i : i + 5] in ["{{IP:", "{{OP:"]:
                if command_text[i + 2 : i + 4] == "IP":
                    extra_path = ip
                else:
                    extra_path = op
                _ = ""
                i += 5
                while i < len(command_text) - 2:
                    if command_text[i : i + 2] == "}}":
                        break
                    else:
                        _ += command_text[i]
                    i += 1
                i += 2

                for_show += _
                for_run += f"{(extra_path / Path(_)).resolve()}"
            else:
                for_run += command_text[i]
                for_show += command_text[i]
                i += 1

        return for_run, for_show

    command_to_run, command_to_show = process_command(command_text=command)

    if extra_command is not None:
        command_to_run += f" {process_command(command_text=extra_command)[0]}"

    output = subprocess.run(command_to_run.split(" "), capture_output=True, text=True)

    if output.returncode != 0:
        raise ValueError(
            f"Executed:\n\n{command_to_run}\nWith list of arguments\n{command_to_run.split(' ')}\nGot error:\n{output.stderr}"
        )

    os.makedirs(op, exist_ok=True)

    with open(op / "console-output.txt", "w") as f:
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

        location = Path(self.state_machine.get_source_and_line(self.lineno)[0])

        if "input-prefix" in self.options:
            IP_path = location.parent / Path(self.options["input-prefix"])
        else:
            IP_path = Path(".")
        if "output-prefix" in self.options:
            OP_path = (
                location.parent
                / f"prompt-run_{location.stem}"
                / Path(self.options["output-prefix"])
            )
        else:
            OP_path = Path(".")

        command = run_script(
            command=self.content[0],
            op=OP_path,
            ip=IP_path,
            extra_command=self.options["extra-command"],
        )

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
