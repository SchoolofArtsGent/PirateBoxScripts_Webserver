from os import listdir
from os.path import isfile, join
mypath = "/opt/piratebox/www/Shared/"
files = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
for f in files:
    print f
