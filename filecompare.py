import argparse
import tqdm
from os.path import exists

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str, help="Sourcefile")
parser.add_argument("-c", "--compare", type=str, help="Filename with values to REMOVE")
parser.add_argument("-o", "--output", type=str, help="Removed lines")
parser.add_argument("-t", "--threshold", type=int, help="Break threshhold (Default: 5).")
args = parser.parse_args()

if not args.input:
    print("Missing input file.")
    exit()
if not args.compare:
    print("Missing compare file.")
    exit()
if not args.output:
    print("Missing output file.")
    exit()
if not args.threshold:
    threshold = 10
else:
    threshold = args.threshold

def find_items(compare, inputslist):
    cleanup = []
    count = 0
    # print("\nChecking " + str(len(inputslist)) + " of items.")
    # print("Looking for: " + compare)
    for line in inputslist:
        if compare.strip() in line.strip():
            cleanup.append(count)
        count += 1
    if len(cleanup) > 0:
        return cleanup
    else:
        return 0

def writeRemaining(inputsList, output):
    f = open(output, 'w')
    for line in inputsList:
        f.write(line.strip()+"\n")
    f.close()


if __name__=="__main__":
    compares = open(args.compare, 'r')
    compareArray = compares.readlines()
    inputs = open(args.input)
    inputsArray = inputs.readlines()

    largelist = tqdm.tqdm(compareArray, desc="Filtering", ascii=False, ncols=75)
    for compare in largelist:
        result = find_items(compare, inputsArray)
        if result:
            print(" Removing: " + str(len(result)) + " items")
            if len(result) >= int(threshold):
                print("\n\nHitting threshold; exiting - check line of exit point in:" + args.compare + "\n\n")
                exit()
            for pos in result:
                inputsArray[pos] = None
            result = None
        inputsArray = list(filter(None, inputsArray))
    writeRemaining(inputsArray, args.output)