from PIL import Image
from flask import Flask


def printImageText():
  im = Image.open("Reindeer.jpg")

  grayscale = " `.^*~>ion=a%@&$#"

  imageList = []
  print(im.getpixel((134,0)))
  for i in range(117):
    imageList.append([])
    for x in range(175):
      imageList[i].append(((im.getpixel((x,i))[0] + im.getpixel((x,i))[1] + im.getpixel((x,i))[2])/255)/3)

  
  everyOther = 0
  for i in imageList:
    print("")
    for x in i:
      if everyOther == 0:
        everyOther = 1
      else:
        everyOther = 0
    
      print(str(grayscale[int(round(x*(len(grayscale)-1),1))])*2,end="")
      if everyOther == 0:
        print(str(grayscale[int(round(x*(len(grayscale)-1),1))])*2,end="")
  return imageList


def printImageTextUpdated():
  im = Image.open("Reindeer.jpg")

  grayscale = "#$&@%a=noi>~*^.` "

  imageList = []
  everyOther = 0
  for i in range(117):
    imageList.append([])
    for x in range(175):
      if everyOther == 0:
        everyOther = 1
      if everyOther == 1:
        pixelNumber=((im.getpixel((x,i))[0] + im.getpixel((x,i))[1] + im.getpixel((x,i))[2])/255)/3
      imageList[i].append(str(grayscale[int(round(pixelNumber*(len(grayscale)-1),1))]))
        
      pixelNumber=((im.getpixel((x,i))[0] + im.getpixel((x,i))[1] + im.getpixel((x,i))[2])/255)/3
      imageList[i].append(str(grayscale[int(round(pixelNumber*(len(grayscale)-1),1))]))
  imageText="""
    """
  for i in imageList:
    imageText +="<br>"
    for x in i:
      imageText+=x

  
  
  return "<style> h1 {font-family:monospace;font-size:3px;}</style><h1>" + imageText + "</h1>"
  


app = Flask(__name__)

@app.route('/')
def hello_world():
  return printImageTextUpdated()

if __name__ == '__main__':
  app.run(host='0.0.0.0')
