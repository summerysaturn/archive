import sys

keys = ["1", "!", "2", "\"", "3", "4", "$", "5", "%", "6", "^", "7", "8", "*", "9", "(", "0", "q", "Q", "w", "W", "e", "E", "r", "t", "T", "y", "Y", "u", "i", "I", "o", "O", "p", "P", "a", "s", "S", "d", "D", "f", "g", "G", "h", "H", "j", "J", "k", "l", "L", "z", "Z", "x", "c", "C", "v", "V", "b", "B", "n", "m"]
keysHex = ["20", "21", "22", "23", "24", "26", "27", "28", "29", "2A", "2B", "2C", "2E", "2F", "30", "31", "32", "34", "35", "36", "37", "38", "39", "3A", "3C", "3D", "3E", "3F", "40", "42", "43", "44", "45", "46", "47", "48", "4A", "4B", "4C", "4D", "4E", "50", "51", "52", "53", "54", "55", "56", "58", "59", "5A", "5B", "5C", "5E", "5F", "60", "61", "62", "63", "64", "66"]

def HexToPiano (n):
    if n in keysHex:
        return keys[keysHex.index(n)]
    else:
        return ""

def BytesToStr (*vals: int):
    tempBytes = []
    for val in vals:
        tempBytes.append(data[val])
    return "".join(map(chr, tempBytes))

def BytesToInt (*vals: int):
    tempBytes = bytearray()
    for val in vals:
        tempBytes.append(data[val])
    return int.from_bytes(tempBytes, byteorder='big')

def GetByte(val: int):
    temp = format(data[val], '02X')
    return temp

FirstByteDict = {'8':3,'9':3,'A':3,'B':3,'C':2,'D':2,'E':3}
def FirstByteSkip (val: str):
    if val in FirstByteDict:
        return FirstByteDict[val]
    else:
        return 0

SecondByteDict = {'00':5,'20':4,'2F':0,'51':6,'54':8,'58':7,'59':5}
def SecondByteSkip (val: str):
    if val in SecondByteDict:
        return SecondByteDict[val]
    else:
        return 1

#open file
checkedArg = False
while True:
    #check to see args for filename, otherwise ask user
    if len(sys.argv) == 1 or checkedArg:
        filename = input("filename: ")
    else:
        filename = sys.argv[1]
        checkedArg = True

    # continue if filetype isn't .mid
    if ".mid" not in filename:
        continue

    # continue if file doesn't exist
    try:
        input_file = open(filename,"rb")
    except Exception:
        continue

    # create byte data from file
    data = bytearray(input_file.read())

    # check to see if midi file has a header, if not, continue
    if BytesToStr(0, 1, 2, 3) != "MThd":
        continue

    break

# 0 = single track, no need to scan for 
# 1 = multiple track
# 2 = multiple songs
trackFormat = BytesToInt(8,9)

if trackFormat == 2:
    input("Midi file has multiple songs, output may be produced incorrectly. Press enter to continue.")

if (trackFormat == 0):
    #single track
    trackLength = BytesToInt(18,19,20,21)
    print(trackLength)

if (trackFormat == 1):
    input("todo, multi-track currently unsupported")

output = ""
i = 23
#timeSinceLastNote = 0
while True:
    fn = GetByte(i)[0]
    sn = GetByte(i)[1]
    sb = GetByte(i+1)
    #do switches, refer to evernote
    if (fn == "9"):
        print("found note")
        key = HexToPiano(format(data[i+1], '02X'))
        output += key
        print(key)
        #timeSinceLastNote = 0
        #input()

    if (fn == "F"):
        if (sn == "0" or sn == "7"):
            #print("skipped", str(2 + BytesToInt(i+1)))
            i += 2 + BytesToInt(i+1)
        else:
            if (sb in ["01","02","03","04","05","06","07","7F"]):
                #print("skipped", str(2 + BytesToInt(i+2)))
                i += 2 + BytesToInt(i+2)
            else:
                #print("skipped", str(SecondByteSkip(sb)))
                i += SecondByteSkip(sb)
    else:
        #print("skipped", str(FirstByteSkip(fn)))
        i += FirstByteSkip(fn)

    #print(fn, sn, sb)

    if (fn == "F" and sn == "F" and sb == "2F"):
        print("eof")
        break

    #timeSinceLastNote += BytesToInt(i+1)

    i += 1

print(output)
