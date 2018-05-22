[enlhex128] whisperplayer
=======================
v2.1




**INSTALLATION**
- Install using setup.py, or [download Windows exe](https://github.com/thejohnd/whisper-player/dist/exe.win32-3.6.zip) from the dist folder

.- **Python:** requires pygame & tkinter

.- **Windows exe:** Download zip file from /dist folder, unzip, run whisperplayer.exe
..- Windows zip doesn't require python installation


1. Load Sounds using Load Directories button

2. Set Min & Max Delay between samples. The mixer will wait for a random number of seconds between these values before randomly playing another sample from the list 

3. Play/Stop with Play/Stop button
  

Issues:  
- If Search Subdirectories is checked, it will search all folders in the folder you selected. Be Careful! If you run Load Directory on your user or root folder with Subdirectories checked, it could take a long time!

- The Directory Selection dialog shows all folders are empty. Haven't figured that one out yet, but it'll still load the files in the directory.

- The Windows exe gives an error and closes when you close it. Working as designed, the long way around?

- If you want to build your own bdist, you'll need to do some tweaks to the setup.py to specify TCL & TK

[enlhex128]: https://i.imgur.com/Wkz5R31.png