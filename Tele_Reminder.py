#ver 1.0

#import
import requests
#import random
from sys import exit
from time import sleep
from datetime import datetime, timedelta, time

#variables


#procedures
def telegram(text, notification):
	params = {'chat_id': '318841796',  'text': text, 'disable_notification': notification}
	response = requests.post('https://api.telegram.org/bot363794957:AAG0N43yr_atdip4gKxuymeyR2f3stH_LMA/sendMessage', data=params)


#program
print ('Start working - ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
telegram('555', True)
