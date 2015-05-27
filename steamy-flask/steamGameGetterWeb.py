#! /usr/bin/python

"------------------------------------- IMPORTS -------------------------------------------"
import steamapi
import csv
import flask

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
    Version: 0.9 (as of May 26, 2015)
    Since: December 7, 2014

"""
"------------------------- CUSTOMIZE COMPONENTS OF FLASK INTERFACE -------------------------------"


"------------------------------------- MAIN METHOD -------------------------------------"
def mainMethod():

    #API Credentials (get your own here: http://steamcommunity.com/dev/apikey)
    STEAM_API_KEY = "7AB68F473F3EB3390A18732EB7F17D5F"
    steamapi.core.APIConnection(api_key=STEAM_API_KEY)
    
    #User Prompt (for Steam ID)
    steamUser = raw_input("Enter Steam ID: ")
    me = steamapi.user.SteamUser(userurl=steamUser)

    #Configure CSV Options and Filename
    csvFileName = steamUser + "-steam-library.csv"
    outputFile = open(csvFileName, 'wb')
    writer = csv.writer(outputFile, dialect='excel')
    writer.writerow(["Game","Minutes Played"])

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

    emailReadyGameList = str('\n '.join(exportableGameList))

if __name__ == "__main__":
    mainMethod()