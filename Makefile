.PHONY: lint plot clean

lint:
	black .
	flake8 .

plot: clean
	python plot_diatomic.py

test:
	pytest -v

clean:
	rm -f *.png