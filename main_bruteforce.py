from PIL import Image
from transformation import transform

if __name__ == '__main__':
    image = Image.open("original_challenge_files/out1_e2ccdbfd607c147695bf5d733c5837e7.bmp")
    outfile = Image.new(image.mode, image.size)
    iteration = 1
    while iteration < 500:
        pixels = [(x, y) for x in range(0, image.size[0]) for y in range(0, image.size[1])]
        for p in pixels:
            sourcepixel = list(image.getpixel(p))
            tran = transform(sourcepixel)
            outfile.putpixel(p, tuple(tran))
        outfile.save("out/brute_force/brute_force{}.bmp".format(iteration))
        image = outfile
        iteration += 1

