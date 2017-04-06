#Import data
import operator
def getTop10IPs(filename): #define filename
  hash_map = {}
  with open(filename,'r') as f: ##open filename
    for line in f:
      IPAddress = line.split()[0] 
      if IPAddress in hash_map:
        hash_map[IPAddress] += 1
      else:
        hash_map[IPAddress] = 1

 ####
  finalRetList=[]
  for item in hash_map:
    if (len(finalRetList)<10):
      finalRetList.append([item,hash_map[item]])
      finalRetList = sorted(finalRetList, key=operator.itemgetter(1))
    else:
      if hash_map[item]>finalRetList[0][1]:
        finalRetList[0]=[item,hash_map[item]] 
        finalRetList = sorted(finalRetList, key=operator.itemgetter(1))

  return sorted(finalRetList, key=operator.itemgetter(1), reverse=True)


def writeFile(tuplesOfHostFreq, filename):
  fileHandler = open(filename, 'w')
  for item in tuplesOfHostFreq:
    fileHandler.write("%s, %d\n" % (item[0],item[1]))
  fileHandler.close()


if __name__ == "__main__":
  topIPAddress = getTop10IPs("log.txt")
  writeFile(topIPAddress, "hosts.txt")
