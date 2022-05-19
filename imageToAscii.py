import argparse

from asciiConverter import AsciiConverter

# TODO:: Add more command line arguments to configure image to greater degree
# Add text file printer similar to sl

if __name__ == "__main__":
    
    # Read args
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--image", help="Input image path")
    parser.add_argument("-o", "--saveLoc", help="Path where converted ascii image should be saved")
    args = parser.parse_args()

    # Parse args
    if not args.image:
        exit(1)

    saveLoc = "./"    
    if args.saveLoc:
        saveLoc = args.saveLoc

    # Print parsed args 
    print(f"Input image path: {args.image}")
    print(f"Output image save path: {saveLoc}")
    #help(AsciiConverter)
    
    converter = AsciiConverter(args.image, outputSize = (400,100))
    converter.convertIntoAscii()
