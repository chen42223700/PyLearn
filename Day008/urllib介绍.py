#urllibΩÈ…‹
import urllib
sock = urllib.urlopen("http://driveintopython.org")
htmlSource = sock.read()
sock,close()
print(htmlSource)
