from pixeltext import *

doiPT = PixelText("doi.txt")

doiPT.modifyWordColor("A", "ff0000")

doiPT.createImage( "doi1.png", "000000", 1, 1)
doiPT.createImage( "doi2.png", "000000", 4, 3)
doiPT.createImage( "doi3.png", "000000", 3, 4)
doiPT.createImage( "doi4.png", "000000", 5, 7)

doiPT.exportColorMap("doi.csv")