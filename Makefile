test:
	python3 -m pytest -q

validate:
	python3 -m tools.validate

info:
	python3 -m cli.main info

sandbox:
	python3 -m sandbox.run
