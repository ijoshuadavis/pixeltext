from pixeltext import *

PT = PixelText("doi.txt")

### RANDOM TEST
PT.clearColorMap()
PT.createColorMapRandom()
PT.exportColorMap("cm_RANDOM_0.csv")

PT.createImage( "RANDOM_1x1_0.png", "000000", 1, 1)
PT.createImage( "RANDOM_4x3_0.png", "000000", 4, 3)
PT.createImage( "RANDOM_3x4_0.png", "000000", 3, 4)
PT.createImage( "RANDOM_5x7_0.png", "000000", 5, 7)
PT.createImage( "RANDOM_7x5_0.png", "000000", 7, 5)
PT.createImageCircle( "RANDOMCIRCLE_1x1_1_0.png", "000000", 1, 1)


### RANDOM BW TEST
PT.clearColorMap()
PT.createColorMapRandomBW()
PT.exportColorMap("cm_RANDOMBW_1.csv")

PT.createImage( "RANDOMBW_1x1_1.png", "000000", 1, 1)
PT.createImage( "RANDOMBW_4x3_1.png", "000000", 4, 3)
PT.createImage( "RANDOMBW_3x4_1.png", "000000", 3, 4)
PT.createImage( "RANDOMBW_5x7_1.png", "000000", 5, 7)
PT.createImage( "RANDOMBW_7x5_1.png", "000000", 7, 5)


### RANDOM CIRCLE TEXT TEST
PT.clearColorMap()
PT.createColorMapRandom()
PT.exportColorMap("cm_RANDOMCIRCLE_1.csv")

PT.createImageCircle( "RANDOMCIRCLE_1x1_1.png", "000000", 1, 1)
PT.createImageCircle( "RANDOMCIRCLE_4x3_1.png", "000000", 4, 3)
PT.createImageCircle( "RANDOMCIRCLE_3x4_1.png", "000000", 3, 4)
PT.createImageCircle( "RANDOMCIRCLE_5x7_1.png", "000000", 5, 7)
PT.createImageCircle( "RANDOMCIRCLE_7x5_1.png", "000000", 7, 5)



### IMPORT EXISTING MAP TEST
#PT.clearColorMap()
#PT.createColorMapRandom()
#PT.exportColorMap("cm_RANDOM_1.csv")

#PT.createImage( "RANDOM_1x1_0.1.png", "000000", 1, 1)
#PT.createImage( "RANDOM_4x3_0.1.png", "000000", 4, 3)
#PT.createImage( "RANDOM_3x4_0.1.png", "000000", 3, 4)
#PT.createImage( "RANDOM_5x7_0.1.png", "000000", 5, 7)
#PT.createImage( "RANDOM_7x5_0.1.png", "000000", 7, 5)
