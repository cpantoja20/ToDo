# Makefile

.PHONY: test
test: 
	tox	-e venv


.PHONY: run
run: 
	python Api/app.py

.PHONY: clean
clean:
	find . -type d -name __pycache__ -exec rm -r {} \+
	rm -rf .tox
	rm -rf venv