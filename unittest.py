from pixeltext import *

doiPT = PixelText("doi.txt")

doiPT.createColorMapRandom()

doiPT.createImage( "doi1.png", "ff0000", 1, 1)
doiPT.createImage( "doi2.png", "ff0000", 4, 3)
doiPT.createImage( "doi3.png", "ff0000", 3, 4)
doiPT.createImage( "doi4.png", "ff0000", 5, 7)

doiPT.createColorMapRandomBW()

doiPT.createImage( "doi5.png", "ff0000", 1, 1)
doiPT.createImage( "doi6.png", "ff0000", 4, 3)
doiPT.createImage( "doi7.png", "ff0000", 3, 4)
doiPT.createImage( "doi8.png", "ff0000", 5, 7)

doiPT.exportColorMap("doi.csv")