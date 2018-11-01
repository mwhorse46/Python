import os

curDir = os.getcwd()
print(curDir)

os.mkdir('newDir')

import time

time.sleep(2)

os.rename('newDir','newDir2')
time.sleep(2)

os.rmdir('newDir2')
