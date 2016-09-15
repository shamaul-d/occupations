occ = open("occupations.csv","r")
ZeList = []
occ.next()
for row in occ:
        ZeList.append(row)
occDict = {}
for i in ZeList:
    d = i.rfind(",")
    occDict[i[0:d]] = float(i[d+1:len(i)])
del occDict['Total']

def randOcc():
    
