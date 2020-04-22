from PIL import Image, ImageChops

# Open images
im1 = Image.open("flag.png").convert("1")
im2 = Image.open("lemur.png").convert("1")

result = ImageChops.logical_xor(im1,im2)
result.save("result.png")

# This is a partial solution. Use stegsolver and XOR Images there instead.
# Or Image Magick
# convert flag.png lemur.png -fx "(((255*u)&(255*(1-v)))|((255*(1-u))&(255*v)))/255" result.png