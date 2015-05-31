from os import listdir
from os.path import isfile, join, getsize, getctime
import time, cgi

mypath = "/opt/piratebox/www/Shared/"

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

files = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
print "Content-Type: text/html"
print
print '<html><head><title>Radius - Files</title></head><body>'
print '<div><a href="/">Home</a></div>'
print '<table>'
for f in files:
    print '<tr>'
    print '<td><a href="/Shared/' + f + '">' + f + '</td>'
    size = sizeof_fmt(getsize(join(mypath,f)));
    print '<td>' + size + '</td>'
    print '<td>' + time.ctime(getctime(join(mypath,f))) + '</td>'
    print '<td><a href="/cgi-bin/delete_shared_file.py?f=' + f + '">delete</td>'
    print '</tr>'
print '</table>'
print '</body></html>'
