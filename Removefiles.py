import time
import os
import shutil

# path = 'C:/Users/fahim/Desktop/Byjus future school project/c99/testFolders'
# days = 0.01

path = input('Path: ')
days = float(input('Days: '))
days *= 86400
days = time.time()-days
q = list(os.walk(path))

if os.path.exists(path):
  for i in range(len(q)):
    joinPath = ''
    if i-1 != -1:
      joinPath = os.path.join(q[0][0], q[0][1][i-1])
    if i >= 1:
      for j in q[i][2]:
        w = os.path.join(joinPath, j)
        wStat = os.stat(w).st_ctime
        if wStat <= days:
          os.remove(w)
        else:
          shutil.rmtree()
else:
  print('File not found')