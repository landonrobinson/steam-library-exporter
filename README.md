![alt tag](http://i.imgur.com/wKW2xNM.jpg) 
Steam Library Exporter
=================
A lightweight Python-based web (and beta executable) program that fetches a user's game library from Steam and sorts and exports it to an Excel/Numbers sheet (CSV). Currently it fetches your username, XP level, library, and total playtime for each game. Goal: a quick and easy way to start tackling that backlog of Steam Sale games.

The program is free to use. It will go live on a domain of some kind soon. 

How does it work?
=================
This program is built in Python with Flask UI and makes use of Steam's API to fetch your game library and other details. It just needs your account name. It'll all print out to an Excel/Numbers/LibreOffice/ApacheOpenOffice sheet for you, which will contain your whole list of games, sorted alphabetically, with your game playtime included. 

It's just a CSV, so you could open it in Notepad if you really want.

Does it use any external modules?
=================
Yes. The client leverages both <a href="http://steamcommunity.com/dev">Valve's Steamworks API.</a> and Smiley Barry's Python wrapper <a href="https://github.com/smiley/steamapi">'steamapi'.</a> A beta executable is available for download, but the premier version is the hot and swanky web version shown above. That's the top priority, and it's pretty much complete.

What's left to add?
=================
I've already added UI in both the executable and web versions, but I want to add more exporting features related to friends lists, achievements, and badges, and more advanced output (like tables). Version 1.0 (an executable) with library and playtime export released in March 2015. The web version will go live before the end of May. 1.x versions will add more features.

I have an idea for a feature!
=================
Email me at landonrobinson92 [@] gmail.com.

License
=================
For more info see LICENSE.TXT. It's basically open-source -- just be a friend and credit me (and Smiley Barry if you use his wrapper like I did) in your future projects. Oh, and don't charge people for it.

Keep it free, pay it forward. :)
