import csv

strArr = []
stateArr = []
unempArr = []
lifeExpectArr = []
crimeArr = []
with open('./MusicMatch/data/unempFINAL.csv', 'rb') as f:
  reader = csv.reader(f)
  i = 0
  for row in reader:
    if i == 0:
      i = i + 1
      continue
    else:
      stateArr.append(row[0])
      unempArr.append(row[1])
      lifeExpectArr.append(row[2])
      crimeArr.append(row[3])
    #strArr.append([row[0],'\'%s\''%(row[1]), row[2]] )
  lifeExpectArr.sort()
  unempArr.sort()
  crimeArr.sort()
  
  print lifeExpectArr[0], lifeExpectArr[len(lifeExpectArr) - 1] 
  print unempArr[0], unempArr[len(unempArr) - 1] 
  print crimeArr[0], crimeArr[len(crimeArr) - 1] 
#def normalizer(num):
  
