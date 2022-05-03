# https://github.com/rthalley/dnspython
# https://github.com/domainaware/checkdmarc

import dns.resolver
import argparse
import tqdm
from os.path import exists

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", help="Filename to parse")
parser.add_argument("-o", "--output", help="Filename to write no MX list")
args = parser.parse_args()

def checkArgs():
    global outputfilename
    global inputfile
    if "".__eq__(args.filename):
        print("Enther filename to process:")
        inputfile = input()
        print("Filename choosen:", inputfile)
    else:
        inputfile = args.filename

    if "".__eq__(args.output):
        print("What filename to write?:")
        outputfilename = input()
        print("Filename choosen:", outputfilename)
    else:
        outputfilename = args.output

    file_exists = exists(inputfile)
    if file_exists != True:
        print("File does not exist, Exits.")
        exit()

def generateList(inputList):
    outputlist = []
    tlist = tqdm.tqdm(inputList, desc="Extracting", ascii=False, ncols=75)
    for item in tlist:
        itemString = item.split("@")
        if(len(itemString) > 1):
            if itemString[1].strip() not in outputlist:
                outputlist.append(itemString[1].strip())
    return outputlist

def checkDns(inputList):
    offenders = []
    tlist = tqdm.tqdm(inputList, desc="Checking", ascii=False, ncols=75)
    for line in tlist:
        try:
            answers = dns.resolver.resolve(line.strip(), "MX")
        except:
            if line not in offenders:
                offenders.append(line)

    return offenders

def writeNoMXFile(inputList):
    f = open(outputfilename, 'a')
    for line in inputList:
        f.write("@" + line + "\n")
    f.close()
    print("Wrote:", str(len(inputList)), "lines to output.")

if __name__=="__main__":
    checkArgs()
    f = open(inputfile,'r')
    inputlines = f.readlines()
    f.close()
    offenders = checkDns(generateList(inputlines))
    writeNoMXFile(offenders)