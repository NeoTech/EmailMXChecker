So far this is only tested on Windows.
Using PyEnv-Win

Should work with Pyenv on Linux as well - getting to that in the future.

Meanwhile linux users should be able to enter the folder
and run `python -m venv dnscheck-venv && source dnscheck-venv/bin/activate`
And after that do: `pip install -r requirements.txt`

Useage:

`python mxcheck.py -f junkmail.txt -o nomx.txt`

This generates a "nomx" reference file. It will hold the offenders.

`python filecompare.py -i junkfile.txt -c nomx.txt -o output.txt -t 5`

This will run your junkfile against your offenders file and generate an output.
The threshold value will make sure that any "weird" occuring email dns matches that
will essentially erase your file gets caught and you can manually remove it and deal
with it before proceeding.