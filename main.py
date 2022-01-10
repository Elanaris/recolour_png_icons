import os
from PIL import Image, ImageFilter


# VARIABLES
colours = {
    "red": (255, 0, 0),
    "orange": (255, 128, 0),
    "black": (0, 0, 0),
    "green": (0, 255, 0),
    "cyan": (0, 255, 255),
    "purple": (127, 0, 255),
    "magenta": (255, 0, 127),
    "grey": (128, 128, 128)
}
transparent_img_names = ["d4", "d10", "d12", "d20", "d48", "d100"]
non_trans_img_names = ["d8"]
source_folder = "dices/"


# MAIN FUNCTION
def recolour_icons(img, rgb, colour_name, name, transparent_bg=True):
    im = Image.open(img).convert("RGBA")
    # Changes white pixels to transparent
    if not transparent_bg:
        for x in range(im.width):
            for y in range(im.height):
                if im.getpixel((x, y))[0] == 255 and im.getpixel((x, y))[1] == 255 and \
                        im.getpixel((x, y))[2] == 255 and im.getpixel((x, y))[3] > 230:
                    im.putpixel((x, y), (255, 255, 255, 0))
    # Changes all pixels to the resulting colour (transparency level stays the same)
    for x in range(im.width):
        for y in range(im.height):
            im.putpixel((x, y), (rgb[0], rgb[1], rgb[2], im.getpixel((x, y))[3]))
    # Blurs the picture if it had white background before,
    # because the resulting edges tend to be too sharp
    if not transparent_bg:
        im = im.filter(ImageFilter.BoxBlur(0.3))
    # Change the save location if needed
    im.save(f"{colour_name}/{name}-{colour_name}.png", "PNG")


# CALL THE FUNCTION
for colour, colour_rgb in colours.items():
    # Creates folders for the recoloured pictures
    try:
        os.mkdir(colour)
    except FileExistsError:
        pass
    # Recolours pictures based on whether they have transparent or white background
    for i in transparent_img_names:
        img_path = f"{source_folder}{i}.png"
        recolour_icons(img_path, colour_rgb, colour, name=i)
    for i in non_trans_img_names:
        img_path = f"{source_folder}{i}.png"
        recolour_icons(img_path, colour_rgb, colour, name=i, transparent_bg=False)
