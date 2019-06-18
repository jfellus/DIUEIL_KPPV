from matplotlib import pyplot as plt
import matplotlib as mpl


def show(image, anim=False):
    if anim:
        plt.ion()
    else:
        plt.ioff()
    plt.clf()
    image = image.reshape(28,28)
    p = plt.imshow(image, cmap=mpl.cm.Greys)
    p.set_interpolation('nearest')
    plt.show()
    if anim:
        plt.pause(.1)


def showm(images, anim=False, title=''):
    if anim:
        plt.ion()
    else:
        plt.ioff()
    plt.clf()
    plt.title(title)
    for (i,image) in enumerate(images):
        plt.subplot(1,len(images),i+1)
        image = image.reshape(28,28)
        p = plt.imshow(image, cmap=mpl.cm.Greys)
        p.set_interpolation('nearest')
    plt.show()
    if anim:
        plt.pause(.1)
