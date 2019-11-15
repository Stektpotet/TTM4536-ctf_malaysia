from transformation import transform
from PIL import Image

transform_table = {}


def fill_table():
    for b in range(0, 255):
        for g in range(0, 255):
            for r in range(0, 255):
                # Store an entry with the transformed pixel as key, and the original as value
                transform_table[tuple(transform ([r, g, b]))] = (r, g, b)


def naive_optimized_fill_table(granularity=(1, 1, 1)):
    for b in range(0, 255, granularity[2]):
        for g in range(0, 255, granularity[1]):
            for r in range(0, 255, granularity[0]):
                # Store an entry with the transformed pixel as key, and the original as value
                transform_table[tuple(transform ([r, g, b]))] = (r, g, b)


def usage_optimized_fill_table(img):
    # List all pixels in use for the given image
    pixels_in_use = set()
    for p in [(x, y) for x in range(0, img.size[0]) for y in range(0, img.size[1])]:
        pixels_in_use.add(img.getpixel(p))
    print("number of pixel variations in use: {}, which is {} fewer than the worst case".
          format(len(pixels_in_use), (256**3)-len(pixels_in_use)))

    # Enumerate all pixel variations and test their
    # existence before adding to the lookup-table
    for b in range(0, 255):
        for g in range(0, 255):
            for r in range(0, 255):
                transformed = tuple(transform([r, g, b]))
                if transformed in pixels_in_use:
                    transform_table[transformed] = (r, g, b)

    print("with memory optimisation: {}B".format(12*len(transform_table)))
    print("without optimisation: {}B".format(12*256**3))


def reverse(pixel):
    if pixel in transform_table:
        return transform_table[pixel]
    else:
        return 0, 0, 0


if __name__ == '__main__':
    image = Image.open("original_challenge_files/out1_e2ccdbfd607c147695bf5d733c5837e7.bmp")
    fill_table(image)
    transformed = Image.new(image.mode, image.size)

    for p in [(x, y) for x in range(0, image.size[0]) for y in range(0, image.size[1])]:
        pixel = image.getpixel(p)
        transformed.putpixel(p, reverse(pixel))

    transformed.save('out/lookup/usage_optimization.bmp')