VENV := .venv

requirements.txt: requirements.in
	test -r $(VENV) || make $(VENV)
	source $(VENV)/bin/activate \
	&& pip-compile --no-emit-index-url --output-file requirements.txt requirements.in

pip_sync: requirements.txt
	source $(VENV)/bin/activate && pip-sync requirements.txt
