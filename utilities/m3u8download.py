import json
import os
import urllib.request
import subprocess

def DownloadM3u8(link,downLoadLocation):
    ffmpegExe = os.environ['FFMPEG_PATH']
    command = r"%s -i %s -c copy %s" % (ffmpegExe,link,downLoadLocation)
    print(command)
    subprocess.call(command)

def main():
    fileName ='C:\Personal\Jsons\episodes.json' 
    with open(fileName) as data_file:    
        data = json.load(data_file)
    for key,value in data.items():
        outputLocation = r"C:\Personal\Videos\%s.mp4" % key.replace(' ','')
        DownloadM3u8(value,outputLocation)
    
if __name__ == "__main__":
    if 'isNullRun' in globals():
        True
    else:
        main()
    