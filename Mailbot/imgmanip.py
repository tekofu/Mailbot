from PIL import Image
import io

def openImg(imgData):
    workImg = Image.open(io.BytesIO(imgData))
    return workImg

def lMirror(workImg):
    # Get some info about the image
    imgSize = workImg.size
    imgForm = workImg.format
    imgWidth = imgSize[0]
    imgHeight = imgSize[1]
    # Deal with odd image widths
    if imgWidth % 2 != 0:
        imgWidth = imgWidth - 1
    # Select the left half of the image
    cropBox = (0, 0, int(imgWidth / 2), imgHeight)
    # Flip it
    cropImg = workImg.crop(cropBox)
    cropImg = cropImg.transpose(Image.FLIP_LEFT_RIGHT)
    # Paste it on the right side
    workImg.paste(cropImg, (int(imgWidth / 2), 0, imgWidth, imgHeight))
    filename = 'output.' + imgForm
    workImg.save(filename)
    return filename

def rMirror(workImg):
    # Get some info about the image
    imgSize = workImg.size
    imgForm = workImg.format
    imgWidth = imgSize[0]
    imgHeight = imgSize[1]
    # Deal with odd image widths
    if imgWidth % 2 != 0:
        imgWidth = imgWidth - 1
    # Select the left half of the image
    cropBox = (int(imgWidth / 2), 0, imgWidth, imgHeight)
    # Flip it
    cropImg = workImg.crop(cropBox)
    cropImg = cropImg.transpose(Image.FLIP_LEFT_RIGHT)
    # Paste it on the right side
    workImg.paste(cropImg, (0, 0, int(imgWidth / 2), imgHeight))
    filename = 'output.' + imgForm
    workImg.save(filename)
    return filename