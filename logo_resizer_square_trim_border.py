from PIL import Image, ImageChops, ImageOps
import argparse

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    #if bbox:
    return im.crop(bbox)

def make_square(im, min_size=256, fill_color='white'):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGBA', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im

def fill_transparent(image,  fill_color='white'):
    
    new_image = Image.new("RGBA", image.size, fill_color) # Create a white rgba background
    new_image.paste(image, mask=image)              # Paste the image on the background. Go to the links given below for details.
    return new_image

def resize(image, size=(180,180)):
    return image.resize(size,resample=Image.LANCZOS)

def add_border(image, border=10, border_color='white'):
    return ImageOps.expand(image,border=border,fill=border_color)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        'input_file',
        type=str,
        help="Location of the input image file"
    )

    args = parser.parse_args()

    im = Image.open(args.input_file).convert("RGBA")
    im = fill_transparent(im,  fill_color='white')
    im = trim(im)
    im = make_square(im, min_size=180, fill_color='white')
    im = resize(im, (180,180))
    im = add_border(im, border=10, border_color='white')
    im.show()

if __name__ == "__main__":
    main()