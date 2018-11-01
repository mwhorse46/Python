appendMe = '\nNew bit of information'

appendFile = open('example.txt','a')
appendFile.write(appendMe)
appendFile.close()
