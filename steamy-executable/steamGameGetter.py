#! /usr/bin/python

"------------------------------------- IMPORTS -------------------------------------------"
import steamapi
import csv
import Tkinter as tk
from Tkinter import Message
from Tkinter import Label
import ImageTk
import Image
import ttk
from Tkinter import StringVar
from time import sleep
import tkMessageBox
import os
import sys

""" "------------------------- ABOUT STEAM GAME GETTER "----------------------------------
    -- Steam Game Getter --
    A Python client for exporting your Steam Library and (eventually) profile content
    to a universal format (CSV) for use in programs like Excel and Numbers.

    -- Resources -- 
    Uses the Python wrapper/external module 'steamapi' from Smiley Barry and official Steam API
    from Valve Software.

    -- Resource Links --
    Valve's Steam API: http://steamcommunity.com/dev
    Smiley Barry's steamapi wrapper': https://github.com/smiley/steamapi

    -- Version Information --
    Author: Landon Robinson
    Version: 0.9 (as of March 10, 2015)
    Since: December 7, 2014

"""
"------------------------- CUSTOMIZE COMPONENTS OF USER INTERFACE -------------------------------"

def getScriptPath():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

runningPath = getScriptPath()
print "Script running at: " + runningPath

#Build Root UI Window
root1 = tk.Tk()
root1.iconbitmap('C:\Users\Landon\Desktop\Python Workspace\Steam-Library-Exporter\steambmp.ico')
root1.wm_title('Steam Library Exporter v0.9')
root1.tk_setPalette(background = "#FFFFFF", foreground = "black")

#Build Text & Entry Window Elements
packable_update = Label(root1, text = 'Ready!')

welcomeMessage = "Welcome to Steam Library Exporter!"
secondMessage = "This app gathers your entire Steam library from the web and all available stats within. \nIt even generates a handy Excel/Numbers spreadsheet for you!"
welcome1 = Message(root1, text=welcomeMessage, width=500, justify='center')
welcome2 = Message(root1, text=secondMessage, width=500, justify='center')

label = tk.Label(root1, text='Enter your Steam Login ID: ')
entry = tk.Entry(root1)
entry.focus_set()

#Image UI
steamLogo = ImageTk.PhotoImage(Image.open('C:\Users\Landon\Desktop\Python Workspace\Steam-Library-Exporter\steamExporterBanner.png'))
panel = tk.Label(root1, image = steamLogo)

"------------------------------------- MAIN METHOD -------------------------------------"
def mainMethod():

    #Message: To Display After User Enters Steam Username
    update_the_label('Searching...')

    #API Credentials (get your own here: http://steamcommunity.com/dev/apikey)
    STEAM_API_KEY = ""
    steamapi.core.APIConnection(api_key=STEAM_API_KEY)
    
    #User Prompt (for Steam ID)
    #steamUser = raw_input("Enter Steam ID: ")
    print str(entry.get())
    steamUser = entry.get()
    me = steamapi.user.SteamUser(userurl=steamUser)

    #Configure CSV Options and Filename
    csvFileName = steamUser + "-steam-library.csv"
    outputFile = open(csvFileName, 'wb')
    writer = csv.writer(outputFile, dialect='excel')
    writer.writerow(["Game","Minutes Played"])

    #Message: To Display After Account was Successfully Found via Web Call
    update_the_label('Account found.')

    #Print Found User Information
    print "Found User: " + me.name
    print "w/ XP Level of: " + str(me.level)
    print "w/ This Game Library: \n"

    #Fetch Raw User's Games List from Steam
    rawGameListFromSteam = me.games

    #Lists to Store Game Names and Playtimes
    exportableGameList = []
    exportablePTList = []

    #Dictionary to Store Game Names and Playtimes Together
    myDictionary = {}

    #Message: To Display After Library Compilation Has Begun
    update_the_label('Compiling game library...')

    #Add Names from Steam Game Objects to exportableGameList
    for game in rawGameListFromSteam:
        if game.name.encode('utf-8') in exportableGameList:
            exportableGameList.append(game.name.encode('utf-8')+" (duplicate)")
            exportablePTList.append(game.playtime_forever)
        else:
            exportableGameList.append(game.name.encode('utf-8'))
            exportablePTList.append(game.playtime_forever)

    #Sort Dictionary
    for x in range(len(exportableGameList)):
        myDictionary[exportableGameList[x]] = exportablePTList[x]
        print str(x) + " " + str(exportableGameList[x])

    #Export to File
    print "\nExporting Game Library to File..."
    for key in sorted(myDictionary.iterkeys()):
        #print "%s: %s" % (key, myDictionary[key])
        writer.writerow([key, myDictionary[key]])
    
    #Close the File
    print "Done. File available now."
    outputFile.close()

    #Message: To Display Upon Completion of Job
    update_the_label('Job complete! :) Your file: ' + csvFileName)
    os.popen("start explorer " + runningPath)

    emailReadyGameList = str('\n '.join(exportableGameList))


    if tkMessageBox.askyesno('Steam Library Exporter v0.9', 'Thanks for using Steam Library Exporter! \nWant to run it again?'):
        print "Running again!"
        entry.delete(0,tk.END)
        update_the_label("Ready (again)!")
    else:
        root1.destroy()

"------------------------------------- Label Update Method ------------------------------------**"

def update_the_label(newText):
    sleep(1)
    packable_update.configure(text = newText)
    root1.update_idletasks()

"------------------------------------- UI Packing/Execution ------------------------------------**"

#Setup Button to Trigger Main Method when Pressed
goButton = tk.Button(root1, text="Start", width=25, command=mainMethod, relief=tk.RAISED)

#Pack Elements into Root Window
panel.pack(side=tk.TOP, fill = "both", expand = "yes")
welcome1.pack()
welcome2.pack()
label.pack()
entry.pack()
goButton.pack(padx=5,pady=5)
packable_update.pack()

#Run the Code with UI
root1.mainloop()