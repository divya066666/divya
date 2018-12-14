import datetime
inputDate ='1/13/99'
day,month,year = inputDate.split('/')
isValidDate = True
try :
    datetime.datetime(int(year),int(month),int(day))
except ValueError :
    isValidDate = False
if(isValidDate) :
    print "yes"
else :
    print "no"
