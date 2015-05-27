![alt tag](http://i.imgur.com/wKW2xNM.jpg) 
NEW! Web Version
![alt tag](http://i.imgur.com/HKx6acx.png) 
Executable Version
Steam Library Exporter
=================
A lightweight Python-based program that fetches a user's game library from Steam and sorts and exports it to an Excel/Numbers sheet (CSV). Currently it fetches your username, XP level, library, and total playtime for each game. Goal: a quick and easy way to start tackling that backlog of Steam Sale games.

The program is free to use. Use it! Just please don't copy the code and make it to be your own thing. Be cool.

How does it work?
=================
This program is built in Python and makes use of Steam's API to fetch your game library and other details. It just needs your login ID. It'll all print out to an Excel/Numbers/LibreOffice/ApacheOpenOffice sheet for you, which will contain your whole list of games, sorted alphabetically, with your game playtime included.

It's just a CSV, so you could open it in Notepad if you really want.

Does it use any external modules?
=================
Yes. The client leverages both <a href="http://steamcommunity.com/dev">Valve's Steamworks API.</a> and Smiley Barry's Python wrapper <a href="https://github.com/smiley/steamapi">'steamapi'.</a> For now, you'll need to have Python installed to run the software (it's easy), but very soon, the program will be a simple executable for Windows, Mac and Linux. It will be executable in the 1.0 version set to release this Spring.

What's left to add?
=================
We've already added UI, but I want to add more exporting features related to friends lists, achievements, and badges, and more advanced Excel output (like tables). Version 1.0 (an executable) with library and playtime export will release in Spring 2015. 1.x versions will add more features.

I have an idea for a feature!
=================
Email me at landonrobinson92 [@] gmail.com.

License
=================
For more info see LICENSE.TXT. It's basically open-source -- just be a friend and credit me (and Smiley Barry if you use his wrapper like I did) in your future projects. Oh, and don't charge people for it.

Keep it free, pay it forward. :)
