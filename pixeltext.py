# File: pixeltext.py
# Purpose: Utility for development of PixelText images.
# Author: Joshua L. Davis
# Version: 0.1.2
# Date Modified: 03/14/08
#
# PixelText is a content visualization concept to translate each unique word from 
# the targeted text (e.g. books, lyrics, poems) to a color (specified or random)
# and then display the word as a pixel in order as they appeared in the original
# text. Simply put, translate these words to pixels. The hope is to create novel
# and compelling art from sources that already possess meaning as well as possibly
# provide a new perspective on the text.
#
# Copyright2008
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

from PIL import Image, ImageDraw


class PixelText:

    def __init__(self, contentFile):
        self.contentFile = contentFile
        
        ###ADD check for file existence OR exit and destroy
      
      
        # Create Content Dictionary
        print("Creating Content Dictionary from",contentFile, "...")
        theContentFile = open(contentFile,"r")

        self.contentList = []
        for line in theContentFile.readlines():
            line = line.replace(" - ", "")
            line = line.replace("(", "")
            line = line.replace(")", "")
            line = line.replace("!", "")
            line = line.replace("?", "")
            line = line.replace(".", "")
            line = line.replace(",", "")
            line = line.replace(";", "")
            line = line.replace(":", "")
            line = line.replace("\"", "")
            line = line.replace(":", "")
            line = line.replace("  ", " ")
            line = line.replace("  ", " ")
            line = line.replace("  ", " ")
            line = line.replace("  ", " ")
            line = line.replace("  ", " ")            
            line = line.lstrip()
            line = line.rstrip()    
            line = line.replace("\r", "")
            line = line.replace("\n", "")
            line = line.replace("\t", "")
            line = line.upper()
            
            ###REFACTOR: Create regexp to speed up loading and content stripping
        
            if len(line) > 0:
                self.contentList = self.contentList + line.split(" ")
        
        # Create Base Map
        self.colorMap = {}
        for word in self.contentList:
            self.colorMap[word] = ""
        print("Content Dictionary",contentFile, "created!")
        
        
    # ColorMap Methods        
    def exportColorMap(self, fileName):
        print("Exporting ColorMap...")
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
 
        theOutFile.close()
        print("ColorMap exported!")
        
        
    # importColorMap
    def importColorMap(self, fileName, backgroundColor):
        print("Importing ColorMap...")
        self.theMapFile = csv.reader(open(fileName,"rb"))
        
        self.colorMap = {}
        for row in self.theMapFile:    
            if row[1] != "":
                self.colorMap[row[0]] = row[1]
            else:
                self.colorMap[row[0]] = backgroundColor
        print("ColorMap imported!")
    
    def createColorMapRandom(self):
        print("Creating Random ColorMap...")
        self.colorMap = {}
        for word in self.contentList:
            colorR = random.randint(0, 255)
            colorG = random.randint(0, 255)
            colorB = random.randint(0, 255)
            self.colorMap[word] = "%02x%02x%02x" % (colorR, colorG, colorB)
        print("Random ColorMap created!")
    
    def createColorMapRandomBW(self):
        print("Creating Random B&W ColorMap...")
        self.colorMap = {}
        for word in self.contentList:
    	    colorR = random.randint(0, 255)
    	    colorG = colorR
    	    colorB = colorR
    	    self.colorMap[word] = "%02x%02x%02x" % (colorR, colorG, colorB)
        print("Random B&W ColorMap created!")
            
    def modifyWordColor(self, word, color):
        self.colorMap[word] = color

    def clearColorMap(self):
        for word in self.contentList:
            self.colorMap[word] = ""
    
    
    # Create Image    
    def createImage(self, fileName, backgroundColor, aspectWidth, aspectHeight):
        print("Creating",fileName, aspectWidth, "x", aspectHeight, "...")
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

        imageSize = int(imageSizeX * aspectWidth/aspectHeight), int(imageSizeY * aspectHeight/aspectWidth)        

        contentImage = Image.new( "RGB", imageSize, "#" + backgroundColor )
        contentImageDraw = ImageDraw.Draw(contentImage)
        
        i = 0
        j = 0
        for word in self.contentList:
            #imageCoordinates = 0, 1
            
            try:
                if( self.colorMap[word] != "" ):
                    contentImageDraw.point((i,j),"#" + self.colorMap[word])
                else:
                    contentImageDraw.point((i,j),"#" + backgroundColor)
            except:
                contentImageDraw.point((i,j),"#800080")
            
            i = i + 1
            if (i == int(imageSizeX * aspectWidth/aspectHeight)):
                i = 0
                j = j + 1
        
        contentImage.save(fileName)
        print("PixelText", fileName, aspectWidth, "x", aspectHeight, "created!")
        
