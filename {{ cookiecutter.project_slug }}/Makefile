.PHONY: help eserv ecli b c t tidy ddb
.DEFAULT_GOAL := help

FILES=`find . -type f -name *.py`
export PATH:=/home/smitty/.local/bin:$(PATH)
export DPATH:=/home/smitty/.local/lib/python3.7/site-packages

help:
	@echo ""
	@echo "Handy project commands:"
	@echo ""
	@echo "target   | description"
	@echo "---------+------------"
	@echo "eserv      Run emacs daemon in venv"
	@echo "ecli       Run emacsclient after eserv is running"
	@echo "b          fix style with black"
	@echo "c          check typing with mypy"
	@echo "t          run tests quickly with the default Python"
	@echo "tidy       fix style, type check, and test"
	@echo "ddb        start dynamodb service"
	@echo ""
eserv:
	@find ~/.emacs.d -type f -name ".elc" -delete && emacs --daemon && echo "\n" && emacsclient -t --eval '(dired-jump)'
ecli:
	@emacsclient -t --eval '(dired-jump)'
b:
	@PYTHONPATH=$(DPATH) black --config etc/pyproject.toml $(FILES)
c:
	@PYTHONPATH=$(DPATH) mypy --config-file etc/mypy.ini $(FILES)
t:
	@PYTHONPATH=$(DPATH) python -m pytest -c etc/pytest.ini tests --capture=no
tidy: b c t
	echo "tidy"
ddb:
	@java -Djava.library.path=~/bin/DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb
