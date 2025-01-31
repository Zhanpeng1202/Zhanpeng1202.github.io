#!/usr/bin/env python3

import sys
from PIL import Image

def make_white_transparent(input_path, output_path):
    # Open the image and ensure it is in RGBA format
    img = Image.open(input_path).convert("RGBA")
    
    datas = img.getdata()
    new_data = []

    for item in datas:
        # item is in the format (R, G, B, A)
        r, g, b, a = item
        # Check if pixel is pure white (255, 255, 255)
        if r == 255 and g == 255 and b == 255:
            # Make it transparent by setting A=0
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    # Update image data with new_data
    img.putdata(new_data)
    # Save in PNG format (which supports transparency)
    img.save(output_path, "PNG")

def main():

        
    input_file = "/Users/luozhanpeng/Code/Website/Zhanpeng1202.github.io/assets/img/zhanpeng_bg.png"
    output_file = "/Users/luozhanpeng/Code/Website/Zhanpeng1202.github.io/assets/img/zhanpeng_bg1.png"
    
    make_white_transparent(input_file, output_file)
    print(f"Finished. Transparent image saved as: {output_file}")

if __name__ == "__main__":
    main()
