from PIL import Image
im = Image.open(input("Enter image path: "))
width, height = im.size
ratio = height / width
resizeWidth = int(input("Enter width: "))
saveToFile = False
if input("Save to file? (y/n)") == "y":
    saveToFile = True
im = im.resize((resizeWidth, int(resizeWidth * ratio * 0.5)))

pixels = list(im.getdata())
width, height = im.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
if not saveToFile:
    for row in pixels:
        for pixel in row:
            print(f"\x1b[38;2;{pixel[0]};{pixel[1]};{pixel[2]}m█", end="")
        print("")
else:
    filename = input("Enter filename: ")
    for row in pixels:
        for pixel in row:
            f = open(filename, "a")
            f.write(f"\x1b[38;2;{pixel[0]};{pixel[1]};{pixel[2]}m█")
            f.close()
        f = open(filename, "a")
        f.write("\n")
        f.close()
