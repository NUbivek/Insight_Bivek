##Import date time
from datetime import datetime 
import operator
# @param name of the log file
# @return list containing top 10 busiest hour
def getTop10busiest(filename):
  hash_map = {}
  date = []
  time = []
  dt =[]
  with open(filename,'r') as f: ### Runs when the file is open
    for line in f: #### Run for loop to iterate
      date_time = line.split()[3]
      dt.append(date_time[1:]+line.split()[4][:-1]) # stores the data that needs to be written inside the hours.txt file
      time.append(date_time[13:])
      date_time = date_time[1:12]
      date_time = convertDate(date_time, time[-1])
      date.append(date_time) # stores the date_time of each request in datetime formate
    #for time in datetime
    # loops for each element in the logfile stores the time and count in a hash table 
  for i in range(len(time)-1):
    diff_time = 0
    if dt[i] not in hash_map:
      j=1
      hash_map[dt[i]]=1
      diff_time = (abs((date[i] - date[i+j]).seconds))
      # loops to find the no. of request in 1 hours from the current request
      # campares the difference in log times in second . 1 hour = 3600 second
      while diff_time < 3600:  
        hash_map[dt[i]] = hash_map[dt[i]] + 1
        j= j+ 1
        diff_time = (abs((date[i] - date[i+j]).seconds))
      #condition for last elemmt as previous loop covers till len -1 elememt
  if dt[len(dt)-1] not in hash_map:
    hash_map[dt[i]]=1

  finalRetList=[]
  #find the top 10 busiest hour 
  for item in hash_map:
    if (len(finalRetList)<10):
      finalRetList.append([item,hash_map[item]])
      finalRetList = sorted(finalRetList, key=operator.itemgetter(1))
    else:
      if hash_map[item]>finalRetList[0][1]:
        finalRetList[0]=[item,hash_map[item]] 
        finalRetList = sorted(finalRetList, key=operator.itemgetter(1))
  # returns in decending order
  return sorted(finalRetList, key=operator.itemgetter(1) , reverse = True) 

#converts date in string format to date/time format to calculate the time difference 
def convertDate(date, time):
  temp = date.split('/')
  time = time.split(':')
  date =''
  for i in temp:
    date = date + ' ' + i 
  date = datetime.strptime(date[1:], '%d %b %Y')
  date = date.replace(hour=int(time[0]), minute=int(time[1]), second=int(time[2]))
  return date
#wrires required information to the file hours.txt
def writeFile(tuplesOfHostFreq, filename):
  fileHandler = open(filename, 'w')
  for item in tuplesOfHostFreq:
    fileHandler.write("%s, %d\n" % (item[0],item[1]))
  fileHandler.close()

##write to file named "hours"
if __name__ == "__main__":
  busiest_time = getTop10busiest("log.txt")
  writeFile(busiest_time, "hours.txt")



