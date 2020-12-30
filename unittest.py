# PixelText is a content visualization concept to translate each unique word from 
# the targeted text (e.g. books, lyrics, poems) to a color (specified or random)
# and then display the word as a pixel in order as they appeared in the original
# text. Simply put, translate these words to pixels. The hope is to create novel
# and compelling art from sources that already possess meaning as well as possibly
# provide a new perspective on the text.
#
# File: unittest.py
# Purpose: Provide utility for development of PixelText images
# Author: Joshua L. Davis
# Version: 0.1.2
# Date Modified: 03/14/08
#
# copyright�2008 
##################################################################################

from pixeltext import *

doiPT = PixelText("doi.txt")


doiPT.createImage("doi1.png", "ff0000", 1, 1)
doiPT.exportColorMap("doi1.csv")


doiPT.createColorMapRandom()
doiPT.createImage("doi2.png", "00ff00", 1, 1)
doiPT.exportColorMap("doi2.csv")


doiPT.createColorMapRandomBW()
doiPT.createImage("doi3.png", "0000ff", 1, 1)
doiPT.exportColorMap("doi3.csv")


doiPT.clearColorMap()
doiPT.createImage("doi1.1.png", "ff0000", 1, 1)
doiPT.exportColorMap("doi1.1.csv")


doiPT.importColorMap("doi2.csv", "00ff00")
doiPT.createImage("doi2.1.png", "00ff00", 1, 1)
doiPT.exportColorMap("doi2.1.csv")


doiPT.importColorMap("doi3.csv", "0000ff")
doiPT.modifyWordColor("A", "ff0000")
doiPT.createImage("doi3.1.png", "0000ff", 1, 1)
doiPT.exportColorMap("doi3.1.csv")


doiPT.createImage( "doi3.2.png", "0000ff", 1, 1)
doiPT.createImage( "doi3.3.png", "0000ff", 4, 3)
doiPT.createImage( "doi3.4.png", "0000ff", 3, 4)
doiPT.createImage( "doi3.5.png", "0000ff", 5, 7)






