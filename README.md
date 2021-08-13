![ingress enlightened hexagon logo](https://i.imgur.com/Wkz5R31.png) whisperplayer
=======================
v3.1
rebuilt, download the package. some sounds now included

## Installation/Requirements
- Try the setup.py (make sure you have `pip` and `setup-tools`), or the setup.bat on Windows (should install `pip` and `setup-tools` if needed)
- if that doesn't work, manually install things:
From command line:
  python -m ensurepip --upgrade
  pip install pygame tk pathlib datetime

## Usage

1. Load a number of sounds using the Load Directories button. Load music/longer audio with the ⏏ button

2. Set Min & Max Delay between samples. The mixer will wait for a random number of seconds between these values before randomly playing another sample from the list 

3. Play/Stop with Play/Stop button
  

### Issues:  
- If Search Subdirectories is checked, it will search all folders in the folder you selected. Be Careful! If you run Load Directory on your user or root folder with Subdirectories checked, it could take a long time!

- The Directory Selection dialog shows all folders are empty. Haven't figured that one out yet, but it'll still load the files in the directory.

~~The Windows exe gives an error and closes when you close it. Working as designed, the long way around?~~

- If you want to build your own bdist, you'll need to do some tweaks to the setup.py to specify TCL & TK

![ingress enlightened hexagon logo](https://i.imgur.com/Wkz5R31.png)

>> #### old install info, out of date
>> **INSTALLATION**
>> - Install using setup.py, or [download Windows exe](https://github.com/thejohnd/whisper-player/dist/exe.win32-3.6.zip) from the dist folder
>> 
>> .- **Python:** requires pygame & tkinter
>> 
>> .- **Windows exe:** Download zip file from /dist folder, unzip, run whisperplayer.exe
>> 
>> ~~Windows zip doesn't require python installation~~
>> ~~Ubuntu & Python:** Need to install python3-tk, python3-dev via your package manager. Then install cx_freeze via pip.~~
