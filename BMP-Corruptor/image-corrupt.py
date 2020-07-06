#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ File Handling ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import math, random

def GoTo(linenum):
    global line
    line = linenum

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

while True:
  #open files
  target = str(input("image file (example: 'target.bmp')  >"))
  if (target == ""):
    target = "target"
  input_file = open(target + ".bmp","rb")
  target = str(input("output file (example: 'output.bmp') >"))
  if (target == ""):
    target = "output"
  output_file = open(target + ".bmp","wb")

  #create byte data
  data = bytearray()
  data.extend(input_file.read())

  offset_hex = bytes([data[10]]) + bytes([data[11]]) + bytes([data[12]]) + bytes([data[13]])
  offset = int.from_bytes(offset_hex, byteorder='little')
  
  #offset = data[10] # start of file
  #x = 15,14,13,12
  #y = 19,18,17,16
  img_x_hex = bytes([data[21]]) + bytes([data[20]]) + bytes([data[19]]) + bytes([data[18]])
  img_y_hex = bytes([data[25]]) + bytes([data[24]]) + bytes([data[23]]) + bytes([data[22]])
  img_x = int.from_bytes(img_x_hex, byteorder='big')
  img_y = int.from_bytes(img_y_hex, byteorder='big')

  print(str(img_x) + " by " + str(img_y))
  #print(str(img_x * img_y) + " pixels")
  print(convert_size(len(data)))
  print(str(offset) + " offset")
  print("predicted size " + convert_size(offset + (img_y + img_x*img_y) * 3))

  proceed = input("proceed? (y/n) >")
  if (proceed == "y") or (proceed == ""):
    break
  else:
    input_file.close()
    output_file.close()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Main Section ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

offset_y = 0

print("working...")

shift = 0

for xIndex in range (0,img_x):
  for yIndex in range (0,img_y):
    #b = data[offset + (y*3) + x + 0]
    #g = data[offset + (y*3) + x + 1]
    #r = data[offset + (y*3) + x + 2]
    x = xIndex * 3
    y = yIndex * 3
    
    xy = (offset + (y + x*img_y))

    if (random.randint(0,100000) > 99999):
      shift = shift + random.randint(100,20000)

    if (xy + 2 + shift*2 < len(data)):
      data[xy + 0] = data[xy + 0 + shift * 2]
      data[xy + 1] = data[xy + 1 + shift * 2]
      data[xy + 2] = data[xy + 2 + shift * 2]
    else:
      data[xy + 0] = 0
      data[xy + 1] = 0
      data[xy + 2] = 0

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Output and Close ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
output_file.write(bytes(data))
input_file.close()
output_file.close()
input("done")

GoTo(1)
