#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import platform


class AbstractPlayer:
    @staticmethod
    def initialize():
        launch_msg = """
=================================================================
 .d8b.  d8888b. .d8888. d888888b d8888b.  .d8b.   .o88b. d888888b
d8' `8b 88  `8D 88'  YP `~~88~~' 88  `8D d8' `8b d8P  Y8 `~~88~~'
88ooo88 88oooY' `8bo.      88    88oobY' 88ooo88 8P         88    
88~~~88 88~~~b.   `Y8b.    88    88`8b   88~~~88 8b         88    
88   88 88   8D db   8D    88    88 `88. 88   88 Y8b  d8    88    
YP   YP Y8888P' `8888Y'    YP    88   YD YP   YP  `Y88P'    YP    
                                                                
d8888b. db       .d8b.  db    db d88888b d8888b. 
88  `8D 88      d8' `8b `8b  d8' 88'     88  `8D 
88oodD' 88      88ooo88  `8bd8'  88ooooo 88oobY' 
88~~~   88      88~~~88    88    88~~~~~ 88`8b   
88      88booo. 88   88    88    88.     88 `88. 
88      Y88888P YP   YP    YP    Y88888P 88   YD   
=================================================================

This is a ascii media player based on python.
We use ffmpeg to deal with the video file.
We follow the GNU GENERAL PUBLIC - VERSION 3 LICENSE.
Welcome to put forward suggestions and contributions code to our project.

.svf(String Video File) is our recognizable media format,it's a zip file that includes media metadata, frames and
audio file.You can also use ordinary video file to generate the SVF file.

About the use of other open source software, can be found in the readme file.

Press any key to continue...
            """

        print(launch_msg)
        input()
        if platform.system().lower() == 'windows':
            os.system('cls')
        else:
            os.system('clear')

    @staticmethod
    def help():
        help_msg = """
======================================================= Commands =======================================================
Command          Parameter(s)                           Functions
------------------------------------------------------------------------------------------------------------------------
play             -path <SVF File Path>                  Open a SVF File and play it!
                 -history                               Get play history and choose one to play!
probe            -path <SVF File Path>                  Get metadata of a SVF file.
                 -history                               Get play history and choose one to get metadata.
generate         <Video File Path>                      Convert video files to SVF file.
help                                                    Show this help message.
========================================================================================================================
        """