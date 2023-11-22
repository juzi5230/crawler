from PIL import Image

def func(a):
    print(a)
    if a < 240:
      return 255
    else:
      return 0

def gen_frame(path):
    im = Image.open(path)
    alpha = im.getchannel('A')

    # Convert the image into P mode but only use 255 colors in the palette out of 256
    im = im.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)

    # Set all pixel values below 128 to 255 , and the rest to 0
    # mask = Image.eval(alpha, lambda a: 255 if a <=255 else 0)
    mask = Image.eval(alpha, func)

    # Paste the color of index 255 and use alpha as a mask
    im.paste(0, mask)
    # print('.....', alpha, mask)
    # The transparency index is 255
    im.info['transparency'] = 0

    return im

imglist = []
for i in range(1,39):
    index = str(i)
    if i < 10: 
        index = str(0) + '' + str(i)
    im = gen_frame(r'/Users/cheng/Desktop/crawler/loading/loading_000{}.png'.format(index))
    imglist.append(im)

im1 = gen_frame(r'/Users/cheng/Desktop/crawler/loading/loading_000{}.png'.format('00'))      
im1.save('GIF.gif', save_all=True, append_images=imglist, loop=0, duration=16.67)