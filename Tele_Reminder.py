#ver 1.0

#import
import requests
from datetime import datetime, timedelta, time
from cryptography.fernet import Fernet

#variables
secret_key=b'Uc7hKWvXlxgs7EBti9keaJA8l3TfoieqUnejyKDeAys='
bt_tkn=b'gAAAAABe3lsH-SaI_7TLuE6D_s9iLeT3jzRf96__57Bmi9Vs8IeLWgCcwAuxLJHVVWUk8CqxrkQbuQonIRREG7MMoxJra-GFZgFDP9gzfdSpwq7m1E3u2-l65QxYtzJ-7G25t0Od0e4OYWg4EMZL87Sf9iobmqFBiQ=='
cipher = Fernet(secret_key)
#encrypted_text = cipher.encrypt(b'123')

proxyList = {
	#"http": "http://169.57.1.85:80",
	"https": "https://45.77.46.62:8080",
#	"https": "https://157.245.251.117:8080",
#	"https": "https://169.57.157.148:8123",
#	"https": "https://144.76.214.157:1080",
#	"https": "https://46.46.140.61:8080",
#	"https": "https://169.57.1.85:80",
#	"https": "https://64.56.218.161:8080",
#	"https": "https://185.72.27.12:8080",
#	"https": "https://163.172.180.18:8811",
#	"https": "https://169.57.1.84:80",
#	"https": "https://200.89.178.156:3128",
#	"https": "https://12.139.101.100:80",
#	"https": "https://105.27.237.27:80",
#	"https": "https://119.81.199.85:8123",
}

#procedures
def telegram(text, notification):
	decrypted_text = cipher.decrypt(bt_tkn)
	params = {'chat_id': '318841796',  'text': text, 'disable_notification': notification}
	response = requests.post('https://api.telegram.org/'+decrypted_text.decode('utf-8')+'/sendMessage', proxies=proxyList, data=params)
	print (response)


#program
print ('Start working - ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
telegram('555', True)
