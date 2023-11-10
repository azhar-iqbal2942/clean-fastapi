# with command `.SILENT` only echo commands will be printed everything else will be omitted
# .SILENT:

VENV = .venv

.PHONY: create-venv
create-venv:
	@if [ ! -d $(VENV) ]; then \
		python3 -m venv .venv; \
		echo "Virtual environment created."; \
	fi

.PHONY: run
run:
	@if [ -d $(VENV) ]; then \
		source $(VENV)/bin/activate; \
		pip install -r requirements.txt; \
		cd src && python main.py; \
		echo "Virtual environment activated."; \
	else \
		echo "Virtual environment not found. Run 'make create-venv' to create it."; \
	fi

.PHONY: clean 
clean:
	find . -type f -name '*.py[co]' -o -type f -name ".coverage" -o -type d -name __pycache__ -o -type d -name .pytest_cache  | xargs rm -rf
	echo "Process Completed"
