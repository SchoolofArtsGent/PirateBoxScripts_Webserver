import os, cgi
arguments = cgi.FieldStorage()
path = "/opt/piratebox/www/Shared/" + arguments['f'].value
#print 'deleting ' + path
os.system('rm "' + path + '"')
print("Location:/cgi-bin/shared_files.py")
print # to end the CGI response headers.
