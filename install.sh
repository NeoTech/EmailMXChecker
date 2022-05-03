#!/bin/env bash
PYENV=$(which pyenv)
if [[ ! -f ${PYENV} ]]; then
    echo "Could not find pyenv-win || pyenv - for compatibility its required."
    exit 1
fi

PYTHON=$(pyenv which python)
echo "Found: ${PYTHON}"

if [[ ! -d dnscheck-venv ]]; then
    echo "VENV seems to be missing; Creating"
    ${PYTHON} -m venv dnscheck-venv
    case ${OS} in
        Windows_NT)
            . dnscheck-venv/Scripts/activate
            sleep 5
            pip install -r requirements.txt
        ;;
        *)
            case $(uname -s) in
                Linux)
                echo "Linux!"
                ;;
                *)
                    echo "No clue.. Verboten."
                ;;
            esac
        ;;
    esac
else
    echo "Virtual env exists, run activeate script."
    echo "example: source dnscheck-venv/Scripts/activate (Windows)"
    echo "example: source dnscheck-venv/bin/activate (Linux)"
fi
