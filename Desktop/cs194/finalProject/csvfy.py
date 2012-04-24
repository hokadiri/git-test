import sys
import csv
import re
'''
with open('some.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(someiterable)
'''
if __name__ == "__main__":
  strArr = []
  if (len(sys.argv) > 1):
    with open(sys.argv[1],"r") as f:
      for line in f.readlines():
        strArr.append(line.split())

  with open(sys.argv[2],"wb") as f:
    
    writer = csv.writer(f)
 
    for arr in strArr:
      s = re.split('\W+',arr)
      if len(re.findall(r"[a-zA-Z]+", s[1])) != 0:
        s[0] = "%s %s"%(s[0],s[1])
        del(s[1])
      writer.writerow(s)


