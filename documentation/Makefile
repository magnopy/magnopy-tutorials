all: optimize-sd
	@echo "Done"

optimize-sd:
	@mkdir -p cubic-ferro-nn-easy-axis/optimize-sd
	@magnopy-optimize-sd -ss GROGU -sf cubic-ferro-nn-easy-axis/GROGU.txt -tt 0.0001 -s 2 2 1 -mf 2 0 0 -hpd -of cubic-ferro-nn-easy-axis/optimize-sd > cubic-ferro-nn-easy-axis/optimize-sd/console-output.txt
	@python3 cubic-ferro-nn-easy-axis/optimize-sd-make-light-html.py -supercell 2 2 1 -i cubic-ferro-nn-easy-axis/GROGU.txt -o cubic-ferro-nn-easy-axis/optimize-sd -sd cubic-ferro-nn-easy-axis/optimize-sd/SPIN_DIRECTIONS.txt -sp cubic-ferro-nn-easy-axis/optimize-sd/SPIN_POSITIONS.txt 