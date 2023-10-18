from PIL import Image

def int_to_bin(rgb):
    r,g,b = rgb
    return (
        '{0:08b}'.format(r),
        '{0:08b}'.format(g),
        '{0:08b}'.format(b)
    )

def bin_to_int(rgb):
    r,g,b = rgb
    return int(r,2),int(g,2),int(b,2)

image1 = Image.open("tree.png")

pixel_map1 = image1.load()

new_img = Image.new(image1.mode,image1.size)
pixels_new = new_img.load()

org_size = image1.size 

for i in range(image1.size[0]):
    for j in range(image1.size[1]):
        r,g,b = int_to_bin(pixel_map1[i,j])
        r = r[-2:] + "000000"
        g = g[-2:] + "000000"
        b = b[-2:] + "000000"
        pixels_new[i,j] = bin_to_int((r,g,b))
        
        if pixels_new[i, j] != (0, 0, 0):
            org_size = (i + 1, j + 1)
            
new_img = new_img.crop((0,0,org_size[0],org_size[1]))
new_img.save("cato.png")
new_img.show()