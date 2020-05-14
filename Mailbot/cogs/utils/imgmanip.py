from PIL import Image
import io
import aiohttp


async def openImg(imgUrl):
    async with aiohttp.ClientSession() as session:
        async with session.get(imgUrl) as req:
            imgData = await req.read()
    workImg = Image.open(io.BytesIO(imgData))
    return workImg


def ultiMirror(workImg, flag):
    # Get some info about the image
    imgSize = workImg.size
    imgForm = workImg.format
    imgWidth = imgSize[0]
    imgHeight = imgSize[1]
    # Deal with odd image widths/heights
    if imgWidth % 2 != 0:
        imgWidth += - 1
    if imgHeight % 2 != 0:
        imgHeight += - 1

    # Base cropbox state
    #cropBox = (0, 0, imgWidth, imgHeight)

    # Designate different section boxes
    cropLeft = (0, 0, int(imgWidth / 2), imgHeight)
    cropRight = (int(imgWidth / 2), 0, imgWidth, imgHeight)
    cropTop = (0, 0, imgWidth, int(imgHeight / 2))
    cropBot = (0, int(imgHeight / 2), imgWidth, imgHeight)

    # Change flip direction depending on flags
    if flag == 'l' or 'r':
        flipDir = Image.FLIP_LEFT_RIGHT
        if flag == 'l':
            cropImg = workImg.crop(cropLeft)
            cropImg = cropImg.transpose(flipDir)
            workImg.paste(cropImg, cropRight)
        if flag == 'r':
            cropImg = workImg.crop(cropRight)
            cropImg = cropImg.transpose(flipDir)
            workImg.paste(cropImg, cropLeft)
    if flag == 't' or 'b':
        flipDir = Image.FLIP_TOP_BOTTOM
        if flag == 't':
            cropImg = workImg.crop(cropTop)
            cropImg = cropImg.transpose(flipDir)
            workImg.paste(cropImg, cropBot)
        if flag == 'b':
            cropImg = workImg.crop(cropBot)
            cropImg = cropImg.transpose(flipDir)
            workImg.paste(cropImg, cropTop)

    filename = f'output.{imgForm}'
    workImg.save(filename)
    return filename
