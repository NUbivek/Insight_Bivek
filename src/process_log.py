// your Python code to implement the features could be placed here
// note that you may use any language, there is no preference towards Python


# -*- coding: utf-8 -*-
import operator
def getTop10IPs(filename):
  hash_map = {}
  with open(filename,'r') as f:
    for line in f:
      IPAddress = line.split()[0]
      hash_map[IPAddress] = hash_map.get(IPAddress, 0) + 1

  #finalRetList = sorted(hash_map.items(), key = lambda item: item[1], reverse = True)[:10]
  finalRetList=[]
  for item in hash_map:
    if (len(finalRetList)<10):
      finalRetList.append([item,hash_map[item]])
      finalRetList = sorted(finalRetList, key=operator.itemgetter(1))
    else:
      if hash_map[item]>finalRetList[0][1]:
        finalRetList[0]=[item,hash_map[item]] 
        finalRetList = sorted(finalRetList, key=operator.itemgetter(1))

  return finalRetList


def writeFile(tuplesOfHostFreq, filename):
  fileHandler = open(filename, 'w')
  for item in tuplesOfHostFreq:
    fileHandler.write("%s, %d\n" % (item[0],item[1]))
  fileHandler.close()


if __name__ == "__main__":
  topIPAddress = getTop10IPs("log.txt")
  writeFile(topIPAddress, "hosts.txt")

# -*- coding: utf-8 -*-
from heapq import heappush, heappop
import operator

def getTop10Resources(filename):
  heap = []
  hashSet = {}
  with open(filename,'r') as f:
    for line in f:
      splitLine = line.split()
      totalBytes = splitLine[-1]
      resource = splitLine[6]
      if len(resource) <= 1: 
        continue
      else:
        if resource not in hashSet:
          hashSet[resource] = 1
        else:
          hashSet[resource] += 1
      # if totalBytes == "-":
      #   totalBytes = 0
      # else:
      #   totalBytes = int(totalBytes)
      # heappush(heap, (-totalBytes, resource))
  sorted_x = sorted(hashSet.items(), key=operator.itemgetter(1))
  sorted_x = sorted_x[::-1]
  keys = [x[0] for x in sorted_x[:10]]
  # for x in sorted_x:
  #   print hashSet[x]
  return keys

def writeFile(tuplesOfHostFreq, filename):
  fileHandler = open(filename, 'w')
  for item in tuplesOfHostFreq:
    # print item
    fileHandler.write(item+'\n')
  fileHandler.close()

if __name__ == "__main__":
  topIPAddress = getTop10Resources("log.txt")
  writeFile(topIPAddress, "resources.txt")
  
  
# -*- coding: utf-8 -*-
from datetime import datetime 
import operator
def getTop10busiest(filename):
  hash_map = {}
  date = []
  time = []
  dt =[]
  with open(filename,'r') as f:
    for line in f:
      date_time = line.split()[3]
      dt.append(date_time[1:]+line.split()[4][:-1])
      time.append(date_time[13:])
      date_time = date_time[1:12]
      date_time = convertDate(date_time, time[-1])
      date.append(date_time)
    #for time in datetime
  for i in range(len(time)-1):
    diff_time = 0
    if dt[i] not in hash_map:
      j=1
      hash_map[dt[i]]=1
      diff_time = (abs((date[i] - date[i+j]).seconds))
      while diff_time < 3600:  
        hash_map[dt[i]] = hash_map[dt[i]] + 1
        j= j+ 1
        diff_time = (abs((date[i] - date[i+j]).seconds))

  if dt[len(dt)-1] not in hash_map:
    hash_map[dt[i]]=1

    #if date in hash_map 
    #hash_map[date] = 5
  finalRetList=[]
  for item in hash_map:
    if (len(finalRetList)<10):
      finalRetList.append([item,hash_map[item]])
      finalRetList = sorted(finalRetList, key=operator.itemgetter(1))
    else:
      if hash_map[item]>finalRetList[0][1]:
        finalRetList[0]=[item,hash_map[item]] 
        finalRetList = sorted(finalRetList, key=operator.itemgetter(1))

  #finalRetList = sorted(hash_map.items(), key = lambda item: item[1], reverse = True)[:10]
  return sorted(finalRetList, key=operator.itemgetter(1) , reverse = True) 

def convertDate(date, time):
  temp = date.split('/')
  time = time.split(':')
  date =''
  for i in temp:
    date = date + ' ' + i 
  date = datetime.strptime(date[1:], '%d %b %Y')
  date = date.replace(hour=int(time[0]), minute=int(time[1]), second=int(time[2]))
  return date

def writeFile(tuplesOfHostFreq, filename):
  fileHandler = open(filename, 'w')
  for item in tuplesOfHostFreq:
    print item[0]
    print item[1]
    fileHandler.write("%s, %d\n" % (item[0],item[1]))
  fileHandler.close()


if __name__ == "__main__":

  busiest_time = getTop10busiest("log.txt")
  writeFile(busiest_time, "hours.txt")

# -*- coding: utf-8 -*-
from datetime import datetime 
import operator
def getTop10busiest(filename):
  ip_name = []
  store_list =[]
  date = []
  valid =[]
  time = []
  data =[]
  with open(filename,'r') as f:
    for line in f:
      date_time = line.split()[3]
      ip_name.append(line.split()[0])
      data.append(line)
      valid.append(line.split()[-2])
      time.append(date_time[13:])
      date_time = date_time[1:12]
      date_time = convertDate(date_time, time[-1])
      date.append(date_time)
    #for time in datetime
    for i in range(len(time)-1):
      diff_time = 0
      count = 1
      #if dt[i] not in hash_map:
      j=1
        #hash_map[dt[i]]=0
      diff_time = (abs((date[i] - date[i+j]).seconds))
      while (diff_time <= 20) and (int(valid[i]) != 200):  
        if (ip_name[i] == ip_name[i+j]):
          count += 1
        if (count == 3):
          store_list.append([date[i], ip_name[i], data[i]])
          break
        j= j + 1
        diff_time = (abs((date[i] - date[i+j]).seconds))

      #if date in hash_map 
      #hash_map[date] = 5
    finalRetList=[]

    for i in range(1,len(store_list)):
      flag = True
      j=1
      diff_time = (abs((store_list[i][0] - store_list[i-j][0]).seconds))
      while (diff_time < 300 and i-j >= 0):
        if store_list[i][1] == store_list[i-j][1]:
          flag =False
          break
        j=j+1
        if i-j>=0:
          diff_time = (abs((store_list[i][0] - store_list[i-j][0]).seconds))
      if flag:
        finalRetList.append(store_list[i][2]) 
  return finalRetList




'''

    for item in hash_map:
      if (len(finalRetList)<10):
        finalRetList.append([item,hash_map[item]])
        finalRetList = sorted(finalRetList, key=operator.itemgetter(1))
      else:
        if hash_map[item]>finalRetList[0][1]:
          finalRetList[0]=[item,hash_map[item]] 
          finalRetList = sorted(finalRetList, key=operator.itemgetter(1))
'''

  #finalRetList = sorted(hash_map.items(), key = lambda item: item[1], reverse = True)[:10]

def convertDate(date, time):
  temp = date.split('/')
  time = time.split(':')
  date =''
  for i in temp:
    date = date + ' ' + i 
  date = datetime.strptime(date[1:], '%d %b %Y')
  date = date.replace(hour=int(time[0]), minute=int(time[1]), second=int(time[2]))
  return date

def writeFile(tuplesOfHostFreq, filename):
  fileHandler = open(filename, 'w')
  for item in tuplesOfHostFreq:
    fileHandler.write("%s \n" % (item))
  fileHandler.close()


if __name__ == "__main__":

  busiest_time = getTop10busiest("log.txt")
  writeFile(busiest_time, "blocked.txt")







