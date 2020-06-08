#ver 1.0

#import
import requests
#import random
#from sys import exit
#from time import sleep
from datetime import datetime, timedelta, time

#variables
proxyList = {
	#"http": "http://169.57.1.85:80",
	"https": "https://169.57.1.85:80",
	"https": "https://64.56.218.161:8080",
	"https": "https://157.245.251.117:8080",
}

#procedures
def telegram(text, notification):
	params = {'chat_id': '318841796',  'text': text, 'disable_notification': notification}
	response = requests.post('https://api.telegram.org/bot363794957:AAG0N43yr_atdip4gKxuymeyR2f3stH_LMA/sendMessage', proxies=proxyList, data=params)


#program
print ('Start working - ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
telegram('555', True)
