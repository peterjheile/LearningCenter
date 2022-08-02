from PIL import Image
import numpy as np


img = Image.new(mode = "RGB", size=(200,200), color = (255,255,0))
# img.show()
# file1 = open("LearningCenter\PillowTesting\ImagesCreated\\firstImage.txt","w")

bitmap = np.array(img)

# print(str(np.array(img)))
# file1.write(str(np.array(img)))
print(bitmap)

for i in bitmap():
    for x in i:
        x = [0,0,0]

im = Image.fromarray(bitmap.astype(np.uint8))
# file1.close()

im.show()
