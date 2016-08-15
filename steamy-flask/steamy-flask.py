#! /usr/bin/python
"------------------------------------- IMPORTS -------------------------------------------"
from flask import Flask
from flask import request
from flask import render_template
from flask import make_response
from flask_mail import Mail
from flask_mail import Message
import steamapi
import csv

"------------------------------------- FLASK APP -------------------------------------"
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("my-form.html")

@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']
    user_email = request.form['email']
    processed_text = text.upper()
    
    #API Credentials (get your own here: http://steamcommunity.com/dev/apikey)
    STEAM_API_KEY = ""
    steamapi.core.APIConnection(api_key=STEAM_API_KEY)
    
    #User Prompt (for Steam ID)
    steamUser = processed_text
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

    return render_template("my-form.html")
if __name__ == '__main__':
    app.run()