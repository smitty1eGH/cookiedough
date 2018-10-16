.PHONY: help eserv ecli b c t tidy
.DEFAULT_GOAL := help

FILES=`find . -type f -name *.py`

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
	@echo ""
eserv:
	@find ~/.emacs.d -type f -name ".elc" -delete && emacs --daemon && echo "\n" && emacsclient -t --eval '(dired-jump)'
ecli:
	@emacsclient -t --eval '(dired-jump)'
b:
	@black $(FILES)
c:
	@mypy --config-file etc/mypy.ini $(FILES)
t:
	@python -m pytest tests --catpure=no
tidy: b c t
	echo "tidy"
