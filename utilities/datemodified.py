import json
import os
import urllib.request
import subprocess
from datetime import datetime
import re

def isSFVersion(fileName):
    if re.search('([\.0-9]{2,})(msi|cab)',fileName) != None:
        return re.search('\.?(([0-9]+\.?)*)(\.msi|\.cab)',fileName).groups(0)[0]
    return ""

def main():
    for root, dirs, files in os.walk(r"\\winfabfs\public\releases"):
        for fileName in files:
            if isSFVersion(fileName) != "":
                time = os.path.getctime(os.path.join(root,fileName))
                date = datetime.fromtimestamp(time).strftime("%Y/%m/%d")
                print("%s : %s" % (isSFVersion(fileName),str(date)))
    
if __name__ == "__main__":
    if 'isNullRun' in globals():
        True
    else:
        main()
    