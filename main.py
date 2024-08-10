import os, sys

AddToTemp = [["CMDS.bat",'''
doskey Brick-Install=C:/SRC/runPackageInstaller.bat
DEL "%~f0"          
'''],["PyLibs.bat", '''
ehco installing libarys
pip install requests
ehco libarys installed
DEL "%~f0"
''']]
AddToSRC = [["Packages.json",'''
{
    "update": ["https://brickspackagemanager.github.io/PackagesJsonPage/", "user", "pass", false,"Packages.json"]
}

'''],
["addpackage.py",'''
import requests
import os 
import sys
import json
print("use the command update to get the repositorys")
PKG = open("Packages.json", "r")
packageToInstall = input("Install Package (to update use cmd update): ")
packages = json.loads(PKG.read())
PKG.close()
print("Package Repo: " + packages[packageToInstall][0])
print("Sending Request")
r = requests.get(packages[packageToInstall][0],stream = True, auth=(packages[packageToInstall][1], packages[packageToInstall][2]))

if r.status_code == 200:
    # Print the HTML source code
    # print(r.text)
    PKGW = open(packages[packageToInstall][4], "w")
    PKGW.write(r.text)
    PKGW.close()
    
else:
    print("error 404 webpage not found or canot acesses")
print("StatusCode: " + str(r.status_code))


'''],["runPackageInstaller.bat",'''
cd C:/SRC/
python addpackage.py
''']]


for i in range(len(AddToTemp)):
    f = open("C:\\Bricks\\Temp\\"+AddToTemp[i][0], "w")
    f.write( AddToTemp[i][1])
    f.close()
    print("Loaded Temp File: " + AddToTemp[i][0])

for i in range(len(AddToSRC)):
    f = open("C:\\Bricks\\SRC\\"+AddToSRC[i][0], "w")
    f.write(AddToSRC[i][1])
    f.close()
    print("Loaded Script File: " + AddToSRC[i][0])


x = input("Press Enter To Return To Bash>")