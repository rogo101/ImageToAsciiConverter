import cv2
import numpy as np

# TODO:: Add getter/setter/helper functions to split up work
# Add functionality to save to file

class AsciiConverter:
    """Object that takes in image path and can then be used to:
        1. convert the image into ascii text
        2. print the ascii image to terminal
        3. save the ascii image to a txt file"""

    def __init__(self, imgPath, outputSize = None, color = False):
        """img is string = path to input image that will be converted
        outputSize is tuple(int, int) = dimenstions of output text: (height, width)
        color is boolean = if true ascii conversion will be colored else it won't"""

        # Read input image as grayscale
        self.img = cv2.imread(imgPath)
        self.imgHeight, self.imgWidth, self.imgNumChannels = self.img.shape

        # Verify that input image is colored before allowing output ascii to be colored
        if self.imgNumChannels >= 3 and color:
            self.color = True
        else:
            self.color = False
            self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            self.imgNumChannels = 1

        # If output dimensions are set, resize the image to match them 
        if outputSize:
            outputSizePreservedAspectRatio = (outputSize[0], int(outputSize[0] * self.imgHeight / self.imgWidth))
            self.img = cv2.resize(self.img, outputSizePreservedAspectRatio, interpolation = cv2.INTER_AREA)
            self.imgHeight, self.imgWidth = self.img.shape[0], self.img.shape[1]

        self.asciiImage = np.full((self.imgHeight, self.imgWidth), '+')

    def convertIntoAscii(self):
        """converts image into an ascii string that is saved in object memory"""

        # List of ascii characters, from least intense to most intense
        asciiChars = [' ', '.', "'", '`', '^', '"', ',', ':', ';', 'I', 'l', '!', 'i', '>', '<', '~', '+',
        '_', '-','?', ']', '[', '}', '{', '1', ')', '(', '|', '\\', '/', 't', 'f', 'j', 'r', 'x', 'n', 'u',
        'v', 'c', 'z', 'X', 'Y', 'U', 'J', 'C', 'L', 'Q', '0', 'O', 'Z', 'm', 'w', 'q', 'p', 'd', 'b', 'k',
        'h', 'a', 'o', '*', '#', 'M', 'W', '&', '8', '%', 'B', '@', '$'][::-1]

        # Normalize input image to have values from 0 to number of ascii characters in the list above
        # This way, each pixel corresponds to an ascii value
        normalizedImage = cv2.normalize(self.img, None, alpha = 0, beta = len(asciiChars) - 1, norm_type=cv2.NORM_MINMAX)

        # Clean the image
        for y in range(0, self.imgHeight):
            for x in range(0, self.imgWidth):
                print(asciiChars[normalizedImage[y, x]], end = "")
            print("")
