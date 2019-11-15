# The transformation code extracted from the original python script
# located in "original_challenge_files/transform_8c0f9f59eb5dbf67e03748af36d55258.py"

def qq(x, y):
    return (2 * x + 3 * y + 29) % 256

def transform(pixelinfo):
    pixelreverse = [pixelinfo[len(pixelinfo)-1-i] for i in range(len(pixelinfo))]
    out = [pixelinfo[i] for i in range(len(pixelinfo))]
    for i in range(len(pixelinfo)):
        out[0] = qq(pixelreverse[i], out[0])
        for j in range(1,len(pixelinfo)):
            out[j] = qq(out[j-1], out[j])
    return out

def str_qq(x, y):
    return "((2 * {} + 3 * {} + 29) mod 256)".format(x, y)


def print_transformation():
    pixelinfo = ["x", "y", "z"]
    pixelreverse = [pixelinfo[len(pixelinfo)-1-i] for i in range(len(pixelinfo))]
    out = [pixelinfo[i] for i in range(len(pixelinfo))]
    for i in range(len(pixelinfo)):
        out[0] = str_qq(pixelreverse[i], out[0])
        print(out[0])
        for j in range(1, len(pixelinfo)):
            out[j] = str_qq(out[j - 1], out[j])
            print(out[j])
        print("\n")

    print("\n")
    for l in out:
        print(l)
