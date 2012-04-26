import csv
strArr = []
with open('./MusicMatch/data/unemployment.csv', 'rb') as f:
  reader = csv.reader(f)
  for row in reader:
    #print row
    strArr.append([row[0],'\'%s\''%(row[1]), row[2]] )
#'''
for row in strArr:
  print row

with open('./MusicMatch/data/unemployment2.csv', 'wb') as f:
  writer = csv.writer(f)
  writer.writerows(strArr)
#'''
