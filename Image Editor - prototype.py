# Created by Tuong Bao Nguyen on the 26/07/2023
# Created as part of a competition - creating a program in 20 minutes

import PIL.Image as pim

filename = input("Enter a filename: ")
filename2 = pim.open(filename)

# The following displays the information of the file that the 
# user inputted.
print(f"\nSummary of {filename}")
print(f"Mode: {filename2.mode}")
print(f"Width: {filename2.width}px")
print(f"Height: {filename2.height}px")

# The following code asks the user how they would like to edit
# their image
print("How would you like to edit your image:")
edit = "placeholder"
while edit not in (1, 2, 3, 4, 5):
    edit = int(input("Press 1 to make image negative, Press 2 for threshold, Press 3 for colour average, Press 4 to flip image or Press 5 to pinch and zoom image" ))

# The following code will inverse the image
if edit == 1:
    inversed = pim.new("L", filename2.size)
    for x in range(filename2.width):
        for y in range(filename2.height):
            old_colour = filename2.getpixel((x, y))
            new_colour = 255 - old_colour
            inversed.putpixel((x, y), new_colour)
    inversed.save("output.png")

# The following is for the threshold
if edit == 2:
    threshold = int(input("Enter a threshold: "))
    threshold_image = pim.new("1", filename2.size)
    for x in range(filename2.width):
        for y in range(filename2.height):
            old_colour = filename2.getpixel((x, y))
            if old_colour >= threshold:
                threshold_image.putpixel((x, y), 1)
            else:
                threshold_image.putpixel((x, y), 0)
    threshold_image.save("output.png")

# The following is to average the colours
if edit == 3:
    new_image = pim.new("L", filename2.size)
    for x in range(filename2.width):
        for y in range(filename2.height):
            r, g, b = filename2.getpixel((x, y))
            avg_val = int((r + g + b) / 3)
            new_image.putpixel((x, y), avg_val)       
    new_image.save("output.png")

# The following is to flip the image
if edit == 4:
    new_image = pim.new("L", filename2.size)
    for x in range(filename2.width):
        for y in range(filename2.height):
            pixel = filename2.getpixel((x, y))
            new_image.putpixel((new_image.width - 1 - x, new_image.height - 1 - y), pixel)       
    new_image.save("output.png")

# The following is to pinch and zoom the image
if edit == 5:
    width = int(input("Enter a width multiplier: "))
    height = int(input("Enter a height multiplier: "))
    newimage = pim.new("L", (filename2.width * width, filename2.height * height))
    counter3 = -1 * height
    for y in range(filename2.height):
        counter3 += height
        counter = -1
        for x in range(filename2.width):
            pixel = filename2.getpixel((x, y))
            for x2 in range(width):
                counter += 1
                counter2 = -1
                for y2 in range(height):
                    counter2 += 1
                    newimage.putpixel((counter, counter3 + counter2), pixel)
    newimage.save("output.png")
