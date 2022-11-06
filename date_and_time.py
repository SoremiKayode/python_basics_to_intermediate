import datetime
from ensurepip import version
from pdb import pm
from time import strftime
from django.http import HttpResponseBadRequest

from numpy import number

date = datetime.datetime.now()

# print(date.year)
# print(date.month)
# print(date.day)
# print(date.hour)
# print(date.minute)
# print(date.second)
# print(date.microsecond)

print(date.strftime("%B"))

%a - week days in short version
%A - Week day in full version
%w - week day as number
%d - day as number
%b -  Month name short version
%B month name full version
%m - Month as number
%H - Hour 23 Hours 
%i - Hour 12 Hour 
%p - am or pm
%M - Minute 
%S - Seconds 







