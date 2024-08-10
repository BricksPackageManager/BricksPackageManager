@echo off
echo installing Bricks
set /p UserInputPath=This Requirs Python to run Please Install If not
set /p UserInputPath=Press Enter To Confirm Install

echo Made Directory Bricks at C:\
mkdir C:\Bricks
mkdir C:\Bricks\Packages
echo Made Directory Packages at C:\Bricks
mkdir C:\Bricks\SRC
echo Made Directory SRC at C:\Bricks
mkdir C:\Bricks\Temp
echo Made Directory Temp at C:\Bricks
set /p UserInputPath=enter to continue to Python
echo Runing SRC - main.py -
Python main.py
echo exected main.py
echo Running Temp Files
cd C:\Bricks\Temp
call CMDS.bat
call PyLibs.bat
set /p UserInputPath=thanks for installing