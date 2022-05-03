.PHONY: help

help:
	@echo "venv: creates virtual env and enters it."
	@echo "install: should be run inside virtual env."

venv:
	ifeq ($(OS),Windows_NT)
    	detected_OS := Windows
	else
    	detected_OS := $(uname -s)
	endif

	ifeq (detected_OS, Windwos)
		python3 -m venv dnscheck
		source dnscheck/Scripts/activate
	endif
	ifeq (detected_OS, Linux)
		@echo "Coming"
	endif
