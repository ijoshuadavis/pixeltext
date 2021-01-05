# File: pixeltext.py
# Purpose: Utility for development of PixelText images.
# Author: Joshua L. Davis
# Version: 1.1
# Date Modified: 01/01/2021
#
# PixelText is a content visualization concept to translate each unique word from 
# the targeted text (e.g. books, lyrics, poems) to a color (specified or random)
# and then display the word as a pixel in order as they appeared in the original
# text. Simply put, translate these words to pixels. The hope is to create novel
# and compelling art from sources that already possess meaning as well as possibly
# provide a new perspective on the text.
#
# Copyright©2021
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
##################################################################################

import sys
import string
import csv
import math
import random
import datetime
import re
import itertools
import sys
from PIL import Image, ImageDraw


class PixelText:

    ######################################################################################################################
    ### Factory Methods
    
###TODO ADD STATIC SPINNER METHODS....
    @staticmethod
    def spinnerInit(self):
        spinner = itertools.cycle(['↑', '↗', '→', '↘', '↓', '↙', '←', '↖'])
        spinner_count = 0

    @staticmethod    
    def spinnerUpdate(self):
        spinner = itertools.cycle(['↑', '↗', '→', '↘', '↓', '↙', '←', '↖'])
        spinner_count = 0




    ######################################################################################################################
    ### Initialization 
    def __init__(self, contentFile):
        self.contentFile = contentFile
        
        ###ADD check for file existence OR exit and destroy
      
      
        # Create Content Dictionary
        theContentFile = open(contentFile,"r")

        # Spinner Setup
        spinner = itertools.cycle(['↑', '↗', '→', '↘', '↓', '↙', '←', '↖'])
        spinner_count = 0
        sys.stdout.write("Creating Content Dictionary ")
        sys.stdout.write(next(spinner))   # write the next character
        sys.stdout.flush()                # flush stdout buffer (actual character display)
        sys.stdout.write('\b') 
            
        self.contentList = []
        for line in theContentFile.readlines():
            line = line.upper()
            line = re.sub(r'[\d]', '', line) #remove numbers
            line = re.sub(r'[-\']', '', line) #remove to complete words/thoughts
            line = re.sub(r'[\t\r\f\v\n\s,.:!@#$%^&*();?><"~`+_|\\\/=]', ' ', line) #remove whitespace and special chars
            spinner_count = spinner_count + 1
           
            if len(line) > 0:
                self.contentList = self.contentList + line.split()

            # Spinner Update
            if spinner_count == 50:
                sys.stdout.write(next(spinner))   # write the next character
                sys.stdout.flush()                # flush stdout buffer (actual character display)
                sys.stdout.write('\b')
                spinner_count = 0
        
        # Create Base Map
        self.colorMap = {}
        for word in self.contentList:
            self.colorMap[word] = ""

        # Spinner Final
        sys.stdout.write('\b')
        sys.stdout.write("...Done!\n")
        sys.stdout.flush()                # flush stdout buffer (actual character display)
            




    ######################################################################################################################
    ### Color Mapping Methods

    ### createColorMapRandom #############################################################################################
    def createColorMapRandom(self):
        # Spinner Setup
        spinner = itertools.cycle(['↑', '↗', '→', '↘', '↓', '↙', '←', '↖'])
        sys.stdout.write("Creating Random ColorMap ")
        sys.stdout.write(next(spinner))   # write the next character
        sys.stdout.flush()                # flush stdout buffer (actual character display)
        sys.stdout.write('\b') 


        self.colorMap = {}
        for word in self.contentList:
            colorR = random.randint(0, 255)
            colorG = random.randint(0, 255)
            colorB = random.randint(0, 255)
            self.colorMap[word] = "%02x%02x%02x" % (colorR, colorG, colorB)

            # Spinner Update
            sys.stdout.write(next(spinner))   # write the next character
            sys.stdout.flush()                # flush stdout buffer (actual character display)
            sys.stdout.write('\b')
            
        # Spinner Final
        sys.stdout.write('\b')
        sys.stdout.write("...Done!\n")
        sys.stdout.flush()                # flush stdout buffer (actual character display)
        
    ### createColorMapRandomBW - Create a Black and White Random Color Map ###############################################
    def createColorMapRandomBW(self):
        # Spinner Setup
        spinner = itertools.cycle(['↑', '↗', '→', '↘', '↓', '↙', '←', '↖'])
        sys.stdout.write("Creating B&W Random ColorMap ")
        sys.stdout.write(next(spinner))   # write the next character
        sys.stdout.flush()                # flush stdout buffer (actual character display)
        sys.stdout.write('\b') 

        self.colorMap = {}
        for word in self.contentList:
    	    colorR = random.randint(0, 255)
    	    colorG = colorR
    	    colorB = colorR
    	    self.colorMap[word] = "%02x%02x%02x" % (colorR, colorG, colorB)

    	    # Spinner Update
    	    sys.stdout.write(next(spinner))   # write the next character
    	    sys.stdout.flush()                # flush stdout buffer (actual character display)
    	    sys.stdout.write('\b')
            
        # Spinner Final
        sys.stdout.write('\b')
        sys.stdout.write("...Done!\n")
        sys.stdout.flush()                # flush stdout buffer (actual character display)



    ### modifyWordColor ##################################################################################################        
    def modifyWordColor(self, word, color):
        self.colorMap[word] = color
        
        
    ### exportColorMap ###################################################################################################  
    def exportColorMap(self, fileName):
        # Spinner Setup
        spinner = itertools.cycle(['↑', '↗', '→', '↘', '↓', '↙', '←', '↖'])
        spinner_count = 0

        # Spinner Start
        sys.stdout.write("Exporting ColorMap ")
        sys.stdout.write(next(spinner))   # write the next character
        sys.stdout.flush()                # flush stdout buffer (actual character display)
        sys.stdout.write('\b') 
        
        
        textUniqueWordList = {}
        for word in self.contentList:
            if word in textUniqueWordList:
                textUniqueWordList[word] = textUniqueWordList[word] + 1
            else:
                textUniqueWordList[word] = 1
         
        theOutFile = open(fileName,"w")
        
        textSortedUniqueWordList = textUniqueWordList.keys()
        sorted(textSortedUniqueWordList)
        
        for word in textSortedUniqueWordList:
            theOutFile.write (word + "," + self.colorMap[word] + "," + str(textUniqueWordList[word]) + "\n")

            # Spinner Update
            if spinner_count == 50:
                sys.stdout.write(next(spinner))   # write the next character
                sys.stdout.flush()                # flush stdout buffer (actual character display)
                sys.stdout.write('\b')
                spinner_count = 0
 
        theOutFile.close()

        # Spinner Final
        sys.stdout.write('\b')
        sys.stdout.write("...Done!\n")
        sys.stdout.flush()                # flush stdout buffer (actual character display)

                
    ### importColorMap ###################################################################################################
    def importColorMap(self, fileName, backgroundColor):

        # Spinner Setup
        spinner = itertools.cycle(['↑', '↗', '→', '↘', '↓', '↙', '←', '↖'])
        sys.stdout.write("Importing ColorMap ")
        sys.stdout.write(next(spinner))   # write the next character
        sys.stdout.flush()                # flush stdout buffer (actual character display)
        sys.stdout.write('\b') 
        
        self.theMapFile = csv.reader(open(fileName,"rb"))
        
        self.colorMap = {}
        for row in self.theMapFile:
            if row[1] != "":
                self.colorMap[row[0]] = row[1]
            else:
                self.colorMap[row[0]] = backgroundColor

            # Spinner Update
            sys.stdout.write(next(spinner))   # write the next character
            sys.stdout.flush()                # flush stdout buffer (actual character display)
            sys.stdout.write('\b')

        # Spinner Final
        sys.stdout.write('\b')
        sys.stdout.write("...Done!\n")
        sys.stdout.flush()                # flush stdout buffer (actual character display)
        

    ### clearColorMap ####################################################################################################
    def clearColorMap(self):
        for word in self.contentList:
            self.colorMap[word] = ""




    
    ######################################################################################################################
    ### Image Creation Methods
            
    ### createImage ######################################################################################################
    def createImage(self, fileName, backgroundColor, aspectWidth, aspectHeight):

        # Spinner Setup
        spinner = itertools.cycle(['↑', '↗', '→', '↘', '↓', '↙', '←', '↖'])
        sys.stdout.write("Creating PixelText %s " %fileName)
        sys.stdout.write(next(spinner))   # write the next character
        sys.stdout.flush()                # flush stdout buffer (actual character display)
        sys.stdout.write('\b')
        
        sqrtContentLength = math.modf(math.sqrt(len(self.contentList)))
        
        if sqrtContentLength[0] < 0.5:
            imageSizeX = int(math.modf(math.sqrt(len(self.contentList)))[1] + 1)
            imageSizeY = int(math.modf(math.sqrt(len(self.contentList)))[1])

        elif sqrtContentLength[0] > 0.5:
            imageSizeX = int(math.modf(math.sqrt(len(self.contentList)))[1] + 1)
            imageSizeY = int(math.modf(math.sqrt(len(self.contentList)))[1] + 1)

        else:
            imageSizeX = int(sqrtContentLength[1])
            imageSizeY = int(sqrtContentLength[1])

        if imageSizeX - imageSizeY == 0:
            imageSize = int(imageSizeX * aspectWidth/aspectHeight), int(imageSizeY * aspectHeight/aspectWidth)
        elif imageSizeX - imageSizeY > 0:
            imageSize = int(imageSizeX * aspectWidth/aspectHeight) + 1, int(imageSizeY * aspectHeight/aspectWidth)
        elif imageSizeX - aspectHeight < 0:
            imageSize = int(imageSizeY * aspectWidth/aspectHeight), int(imageSizeY * aspectHeight/aspectWidth) + 1

        contentImage = Image.new( "RGB", imageSize, "#" + backgroundColor )
        contentImageDraw = ImageDraw.Draw(contentImage)
        
        i = 0
        j = 0

        for word in self.contentList:     
            try:
                if( self.colorMap[word] != "" ):
                    contentImageDraw.point((i,j),"#" + self.colorMap[word])
                else:
                    contentImageDraw.point((i,j),"#" + backgroundColor)
            except:
                contentImageDraw.point((i,j),"#800080")
            
            i = i + 1
            if (i == imageSize[0]):
                i = 0
                j = j + 1

            # Spinner Update
            sys.stdout.write(next(spinner))   # write the next character
            sys.stdout.flush()                # flush stdout buffer (actual character display)
            sys.stdout.write('\b')

        contentImage.save(fileName)

        # Spinner Final
        sys.stdout.write('\b')
        sys.stdout.write("...Done!\n")
        sys.stdout.flush()                # flush stdout buffer (actual character display)

        print("Dimention: ", imageSize[0], " x ", imageSize[1], "Words: ", len(self.contentList), " >> ", imageSize[0] * imageSize[1], " = ",imageSize[0] * imageSize[1] -  len(self.contentList)," SQRT:", math.sqrt(len(self.contentList)))

    ### createImageCircle - Instead of left to right placement of pixel, doing in circle #################################
    def createImageCircle (self, fileName, backgroundColor, aspectWidth, aspectHeight):

        # Spinner Setup
        spinner = itertools.cycle(['↑', '↗', '→', '↘', '↓', '↙', '←', '↖'])
        sys.stdout.write("Creating PixelText %s " %fileName)
        sys.stdout.write(next(spinner))   # write the next character
        sys.stdout.flush()                # flush stdout buffer (actual character display)
        sys.stdout.write('\b')

        sqrtContentLength = math.modf(math.sqrt(len(self.contentList)))
        
        if sqrtContentLength[0] < 0.5:
            imageSizeX = int(math.modf(math.sqrt(len(self.contentList)))[1] + 1)
            imageSizeY = int(math.modf(math.sqrt(len(self.contentList)))[1])

        elif sqrtContentLength[0] > 0.5:
            imageSizeX = int(math.modf(math.sqrt(len(self.contentList)))[1] + 1)
            imageSizeY = int(math.modf(math.sqrt(len(self.contentList)))[1] + 1)

        else:
            imageSizeX = int(sqrtContentLength[1])
            imageSizeY = int(sqrtContentLength[1])


        if imageSizeX - imageSizeY == 0:
            imageSize = int(imageSizeX * aspectWidth/aspectHeight), int(imageSizeY * aspectHeight/aspectWidth)
        elif imageSizeX - imageSizeY > 0:
            imageSize = int(imageSizeX * aspectWidth/aspectHeight) + 1, int(imageSizeY * aspectHeight/aspectWidth)
        elif imageSizeX - aspectHeight < 0:
            imageSize = int(imageSizeY * aspectWidth/aspectHeight), int(imageSizeY * aspectHeight/aspectWidth) + 1

        contentImage = Image.new( "RGB", imageSize, "#" + backgroundColor )
        contentImageDraw = ImageDraw.Draw(contentImage)
        
        i = 0
        j = 0
        k = 0
        l = 0
        n = 0


        if imageSize[0] * imageSize[1] - len(self.contentList) != 0:
            n = imageSize[0] * imageSize[1] - len(self.contentList)
            while n != 0:
                if (l == 0): ## Draw to the right
                    i = i + 1
                    if (i == imageSize[0] - k - 1):
                        l = 1
                        
                elif (l == 1): ## Draw to the down
                    j = j + 1
                    if (j == imageSize[1] - k - 1):
                        l = 2
                        
                elif (l == 2): ## Draw to the left
                    i = i - 1
                    if (i == k):
                        l = 3
                        
                elif (l == 3): ## Draw to the up
                    j = j - 1
                    if (j == k):
                        i = i + 1
                        j = j + 1
                        k = k + 1
                        l = 0

                n = n - 1
        
        for word in self.contentList:      
            try:
                if( self.colorMap[word] != "" ):
                    contentImageDraw.point((i,j),"#" + self.colorMap[word])
                else:
                    contentImageDraw.point((i,j),"#" + backgroundColor)
            except:
                contentImageDraw.point((i,j),"#800080")

            if (l == 0): ## Draw to the right
                i = i + 1
                if (i == imageSize[0] - k - 1):
                    l = 1
                    
            elif (l == 1): ## Draw to the down
                j = j + 1
                if (j == imageSize[1] - k - 1):
                    l = 2
                    
            elif (l == 2): ## Draw to the left
                i = i - 1
                if (i == k):
                    l = 3
                    
            elif (l == 3): ## Draw to the up
                j = j - 1
                if (j == k):
                    i = i + 1
                    j = j + 1
                    k = k + 1
                    l = 0

            # Spinner Update
            sys.stdout.write(next(spinner))   # write the next character
            sys.stdout.flush()                # flush stdout buffer (actual character display)
            sys.stdout.write('\b')

        contentImage.save(fileName)

        # Spinner Final
        sys.stdout.write('\b')
        sys.stdout.write("...Done!\n")
        sys.stdout.flush()                # flush stdout buffer (actual character display)

        print("Dimention: ", imageSize[0], " x ", imageSize[1], "Words: ", len(self.contentList), " >> ", imageSize[0] * imageSize[1], " = ",imageSize[0] * imageSize[1] -  len(self.contentList)," SQRT:", math.sqrt(len(self.contentList)))
