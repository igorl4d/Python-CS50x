from cs50 import get_int
height = 0
while (height < 1  or height > 8):
    height = get_int("Height of pyramid")

for i in range(height):
    print((height - 1 - i) * " ", end="")
    print((i + 1) * "#")

for
        