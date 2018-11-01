# this program has no error but you have to place actual domain name and password in order to access all the things.

from ftplib import FTP

ftp = FTP('domainname.com')
ftp.login(user='username',passwd='password')
ftp.cwd('/specificdomain-ro-location/')

def grabFile():
    fileName = 'fileName.txt'
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    ftp.quit()
    localfile.close()

def placeFile():
    fileName = 'fileName.txt'
    ftp.storbinary('STOR '+filename, open(filename, 'rb'))
    ftp.quit()




