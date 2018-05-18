'''

@author: John DeAscentis
@title: TreeMixer
@summary: Sound app for SEA-ENL project for Ingress Navarro 2018
@version: 0.2b
'''
from datetime import timedelta, datetime
from pathlib import Path, PurePath, PureWindowsPath
from random import randint
#import tkinter.tix as tix
from tkinter import filedialog, messagebox
from tkinter import *
from mixer import mixer
import os


root = Tk()
root.winfo_toplevel().title('Seattle ENL - Navarro 2018  -  Sound Player')

subdir_checkbox_val = 1
listboxvar = []
global listedFiles  # list of the loaded files
global _soundPlaying  # play flag
global minDelay, maxDelay, thisDelay  # delay between fx
global nextCue  # datetime object for next fx cue
global play_icon, stop_icon, sea_icon
global nowPlaying
_soundPlaying = 0
minDelay = IntVar()  # default MIN delay between fx
maxDelay = IntVar()  # default MAX delay between fx
if os.name == 'nt':
    play_icon = PhotoImage(file=PureWindowsPath('./res/playicon.png'))
    stop_icon = PhotoImage(file=PureWindowsPath('./res/stopicon.png'))
    sea_icon = PhotoImage(file=PureWindowsPath('./res/sea-enl-logo_icon.png'))
else:
    play_icon = PhotoImage(file=PureWindowsPath('./res/playicon.png'))
    stop_icon = PhotoImage(file=PureWindowsPath('./res/stopicon.png'))
    sea_icon = PhotoImage(file=PureWindowsPath('./res/sea-enl-logo_icon.png'))

#===============================================================================
#   Call Mixer setup
#===============================================================================
mix = mixer()


#===============================================================================
#   Called on Click of 'Load directory'
#===============================================================================
def fileBrowserCallback():
    #===========================================================================
    # Pop up directory
    # select dialog
    # call get_dir to process selected directory
    # get selected path from file browser window
    #===========================================================================
    d = filedialog.askdirectory(title="Select Sounds Directory", parent=root)
    print(d)
    if d == '':
        pass
    else:
        try:
            dpath = Path(d)
            if dpath.exists() :  get_dir(d)
            else:
                gui_raise("Directory {} doesn't exist".format(dpath))
        except Exception as e:
            print(e)


#===============================================================================
# Return all files in selected folder/subdirs of correct filetype
#===============================================================================
def get_dir(args):
    global listedFiles
    # # SET FILETYPE HERE
    filetype = 'ogg'
    onlyfiles = []
    dirpath = "."
    try:
        dirpath = Path(args)
        if subdir_checkbox_val:
            # search all subdirs
            onlyfiles = list(dirpath.glob('**/*.ogg'))
        else:
            # don't search subdirs
            onlyfiles = list(dirpath.glob('*/*.ogg'))
        listedFiles = onlyfiles
        if onlyfiles[0]:  # creates IndexError if empty, caught by 1st except
            listbox.delete(0, END)  # clear listbox for new filelist
            for s in onlyfiles:
                t = PurePath(s)
                listbox.insert(END, t.name)

    except IndexError:
        # sounds_loaded = 0
        if dirpath == '.':
            return dirpath
        else:
            errmsg = 'No %s files found in selected folder' % filetype
            listbox.delete(0, END)
            gui_raise(errmsg)
    except:
        # sounds_loaded = 0
        errmsg = 'Error opening files in folder'
        gui_raise(errmsg)


#===============================================================================
#    PLAY BUTTON HANDLER
#===============================================================================
def play_pushed(event=''):
    global _soundPlaying, minDelay, maxDelay, nextCue
    try:
        minDelay.get()
        maxDelay.get()
        if not (0 <= minDelay.get() <= maxDelay.get()):
            raise ValueError('Delay must be (0 <= minDelay <= maxDelay)')
    except:
        messagebox.showerror('Invalid Values',
                             'Delay must be: [0 <= minDelay <= maxDelay]')
        minDelay.set('')
        maxDelay.set('')

    if _soundPlaying == 0:
        if listbox.size() > 0:
            thisDelay = randint(minDelay.get(), maxDelay.get())
            nextCue = datetime.now() + timedelta(seconds=thisDelay)
            _soundPlaying = 1
            # play_button.state(statespec='selected')
            play_button.config(relief=RIDGE, image=stop_icon)
            play_loop()

        else:
            messagebox.showwarning('No sounds',
                                   'No sounds loaded')
    elif _soundPlaying == 1:
        _soundPlaying = 0
        if mix.stop_sound():
            raise RuntimeError('ERROR: mixer failed to stop')
        else:
            print('Mixer stopped')
            # play_button.state(statespec='')
            play_button.config(relief=FLAT, image=play_icon)


#===============================================================================
#   SEND THE SOUND LIST TO THE PYGAME MIXER TO PLAY
#===============================================================================
def play_loop():
    global listedFiles, nextCue, _soundPlaying

    if _soundPlaying == 1:
        try:
            if (datetime.now() >= nextCue):
                mix.play_sound(listedFiles)
                nextCue = new_cue(minDelay.get(), maxDelay.get())
            else:
                pass
        except TypeError:
                play_pushed()
                print("Playback stopped - you put in a bad delay value\n")
                print("Press play again to resume")
    else:
        pass


#===============================================================================
#   splitting out function to set a new fx play cue
#   Returns datetime for nextCUE
#   - call new_cue(x) to return a cue in exactly x seconds
#   - call with (minD, maxD) to return a cue in random secs in range(minD,maxD)
#   - call with new_cue() to get a cue for now
#===============================================================================
def new_cue(minD=0, maxD=0, **options):
    if (minD < 0) or (maxD < 0):
        gui_raise("Invalid new_cue: minD & maxD cannot be negative")
        return 0
    elif (minD > maxD):
        gui_raise("Invalid new_cue: maxD must be greater than minD")
        return 0
    else:  # if minD & maxD are legit set thisDelay, then return datetime cue
        if (maxD == 0):
            if(minD == 0):
                thisDelay = 0
            else:
                thisDelay = minD
        else:
            thisDelay = randint(minD, maxD)

        nxtQ = datetime.now() + timedelta(seconds=thisDelay)
        return nxtQ


#===============================================================================
#   Macro for GUI Error Box
#===============================================================================
def gui_raise(msg, title="Error"):
    messagebox.showerror(title, msg)


#===============================================================================
#   Macro for quick entry box making
#===============================================================================
def makeentry(parent, caption, width=None, **options):
    entry = Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    Label(parent, padx=7, pady=3, text=caption).pack(side=LEFT)
    return entry


#===============================================================================
#    MAIN
#===============================================================================
if __name__ == '__main__':

    #==========================================================================
    #   GUI LAYOUT
    #===========================================================================

    frame_top = Frame(root,
                      height=70,
                      width=35,
                      padx=5,
                      pady=5)

    #==========================================================================
    #   TOP FRAME LAYOUT
    #===========================================================================
    # BUTTON
    frame_loadbutton = Frame(frame_top)
    b1 = Button(frame_loadbutton,
                text="Load Directory",
                command=fileBrowserCallback)
    b1.pack(side=TOP)
    # CHECKBOX
    subdir_chkbox = Checkbutton(frame_loadbutton,
                                    text='Include subdirectories',
                                    variable=subdir_checkbox_val)
    # subdir_chkbox.select()
    subdir_chkbox.pack(side=BOTTOM)
    icon = Label(frame_top, image=sea_icon)

    frame_loadbutton.pack(side=LEFT, expand=1)
    icon.pack(side=RIGHT, fill=Y, expand=1)
    frame_top.pack(side=TOP, expand=1, fill=BOTH)

    #===========================================================================
    #   FILES LIST LAYOUT
    #===========================================================================
    list_scrollbar = Scrollbar(root, orient=VERTICAL)
    listbox = Listbox(root, width=75, height=40,
                      yscrollcommand=list_scrollbar.set)
    list_scrollbar.config(command=listbox.yview)
    list_scrollbar.pack(side=RIGHT, fill=Y)
    listbox.pack(side=TOP, fill=BOTH, expand=1)

    #===========================================================================
    #   PLAY BUTTON
    #===========================================================================
    play_button = Button(root,
                             image=play_icon,
                             command=play_pushed,
                             relief=FLAT,
                             padx=5
                             )
    play_button.config(borderwidth=5, default=NORMAL)
    play_button.pack(side=LEFT, padx=5)

    #===========================================================================
    #   Min and Max Delay Boxes
    #===========================================================================
    frame_dBox1 = Frame(root, padx=15, pady=5)
    minDbox = makeentry(frame_dBox1,
                        "Min delay (sec)",
                        3,
                        textvariable=minDelay)
    minDelay.set("2")
    frame_dBox1.pack(fill=X, expand=1)

    frame_dBox2 = Frame(root, padx=15)
    maxDbox = makeentry(frame_dBox2,
                        "Max delay (sec)",
                        3,
                        textvariable=maxDelay)
    maxDelay.set("15")
    frame_dBox2.pack(fill=X, expand=1)

    #===========================================================================
    #    keybinding
    #===========================================================================
    root.bind("<space>", play_pushed)

    #===========================================================================
    #     SHOOP DA LOOP [mainloop replacement]
    #===========================================================================

    while True:
        mix.pywait(mils=10)
        try:
            play_loop()
            root.update_idletasks()
            root.update()
        except TclError:
            exit()
