##Import datetime
from datetime import datetime 
import operator
def blocked(filename):
  ip_name = []
  store_list =[]
  date = []
  valid =[]
  time = []
  data =[]
  with open(filename,'r') as f:
    for line in f:
      date_time = line.split()[3]
      ip_name.append(line.split()[0]) # stores the ip address or domain name
      data.append(line) # stores the entire line for the file
      valid.append(line.split()[-2]) # stores the interger to check is sucess or failed attempt
      time.append(date_time[13:])
      date_time = date_time[1:12]
      date_time = convertDate(date_time, time[-1])
      date.append(date_time) # stores the date_time of each request in datetime format
    #for time in datetime
    # loops for each element in the file and stores for  3 consecutive failed attemps in 20 seconds
    for i in range(len(time)-1):
      diff_time = 0
      count = 1
      #if dt[i] not in hash_map:
      j=1
        #hash_map[dt[i]]=0
      diff_time = (abs((date[i] - date[i+j]).seconds))
      #uses difference in datetime and failed or sucess code to keep track of failed count 
      #if count = 3 adds the data to the list 
      # 200 code means sucess , rest are fail 
      while (diff_time <= 20) and (int(valid[i]) != 200):  
        if (ip_name[i] == ip_name[i+j]):
          count += 1
        if (count == 3):
          store_list.append([date[i], ip_name[i], data[i]])
          break
        j= j + 1
        diff_time = (abs((date[i] - date[i+j]).seconds))
    finalRetList=[]

    #checks if there are any diplicate entries within the next 5 min or 300 seconds
    for i in range(1,len(store_list)):
      flag = True
      j=1
      diff_time = (abs((store_list[i][0] - store_list[i-j][0]).seconds))
      #loops backword in the list to check for diplicate entries
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

#converts date in string formate to datetime format to calculate the time difference 
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
    fileHandler.write("%s \n" % (item))
  fileHandler.close()

##write output to file
if __name__ == "__main__":
  blocked_list = blocked("log.txt")
  writeFile(blocked_list, "blocked.txt")



