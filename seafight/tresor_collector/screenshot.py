import pyscreenshot as ImageGrab
import pyautogui

from PIL import Image
from PIL import ImageOps

def locateAll(needleImage, haystackImage, grayscale=False, limit=None):
    needleFileObj = None
    haystackFileObj = None
    if isinstance(needleImage, str):
        # 'image' is a filename, load the Image object
        needleFileObj = open(needleImage, 'rb')
        needleImage = Image.open(needleFileObj)
    if isinstance(haystackImage, str):
        # 'image' is a filename, load the Image object
        haystackFileObj = open(haystackImage, 'rb')
        haystackImage = Image.open(haystackFileObj)


    if grayscale:
        needleImage = ImageOps.grayscale(needleImage)
        haystackImage = ImageOps.grayscale(haystackImage)

    needleWidth, needleHeight = needleImage.size
    haystackWidth, haystackHeight = haystackImage.size

    needleImageData = tuple(needleImage.getdata()) # TODO - rename to needleImageData??
    haystackImageData = tuple(haystackImage.getdata())

    needleImageRows = [needleImageData[y * needleWidth:(y+1) * needleWidth] for y in range(needleHeight)] # LEFT OFF - check this
    needleImageFirstRow = needleImageRows[0]

    assert len(needleImageFirstRow) == needleWidth
    assert [len(row) for row in needleImageRows] == [needleWidth] * needleHeight

    numMatchesFound = 0

    for y in range(haystackHeight):
        for matchx in _kmp(needleImageFirstRow, haystackImageData[y * haystackWidth:(y+1) * haystackWidth]):
            foundMatch = True
            for searchy in range(1, needleHeight):
                haystackStart = (searchy + y) * haystackWidth + matchx
                if needleImageData[searchy * needleWidth:(searchy+1) * needleWidth] != haystackImageData[haystackStart:haystackStart + needleWidth]:
                    foundMatch = False
                    break
            if foundMatch:
                # Match found, report the x, y, width, height of where the matching region is in haystack.
                numMatchesFound += 1
                yield (matchx, y, needleWidth, needleHeight)
                if limit is not None and numMatchesFound >= limit:
                    # Limit has been reached. Close file handles.
                    if needleFileObj is not None:
                        needleFileObj.close()
                    if haystackFileObj is not None:
                        haystackFileObj.close()


    # There was no limit or the limit wasn't reached, but close the file handles anyway.
    if needleFileObj is not None:
        needleFileObj.close()
    if haystackFileObj is not None:
        haystackFileObj.close()
        
def _kmp(needle, haystack): # Knuth-Morris-Pratt search algorithm implementation (to be used by screen capture)
    # build table of shift amounts
    shifts = [1] * (len(needle) + 1)
    shift = 1
    for pos in range(len(needle)):
        while shift <= pos and needle[pos] != needle[pos-shift]:
            shift += shifts[pos-shift]
        shifts[pos+1] = shift

    # do the actual search
    startPos = 0
    matchLen = 0
    for c in haystack:
        while matchLen == len(needle) or \
              matchLen >= 0 and needle[matchLen] != c:
            startPos += shifts[matchLen]
            matchLen -= shifts[matchLen]
        matchLen += 1
        if matchLen == len(needle):
            yield startPos
        
def center(coords):
    return (coords[0] + int(coords[2] / 2), coords[1] + int(coords[3] / 2))




[width,height] = pyautogui.size()
print(width,height)

# import pyautogui
# pyautogui.displayMousePosition()

# map
m_x1 = 1484
m_y1 = 289
m_x2 = 1577
m_y2 = 382
# screen
s_x1 = 614
s_y1 = 300
s_x2 = 1374
s_y2 = 880

while(1):
	img = ImageGrab.grab(bbox=(m_x1,m_y1,m_x2,m_y2))
	#img = ImageGrab.grab(bbox=(s_x1,s_y1,s_x2,s_y2))

	# detect yellow point in map :
	#print(list(locateAll('target2.png', 'map.png', grayscale=True, limit=1)))
	print(list(locateAll('target2.png', img, grayscale=True, limit=1)))

	# detect meat in sea :
	#print(list(locateAll('small_pic.png', 'big_pic.png', grayscale=False, limit=None)))
	
	sleep(1)

