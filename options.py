import os.path
import praw
import re
import sys
import time


def clear():
	sys.stdout.write("\033[F")
	sys.stdout.flush()
	
def write(str):
	clear()
	sys.stdout.write(str+' \r')
	sys.stdout.flush()

def getHourly():
	epoch = int(time.time())
	

# bot login credentials
username = ''
password = ''



# Your app details
user_agent = 'bot'
client_id = ''
client_secret = ''

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,                                            username=username,
    password=password)
    

subreddit = reddit.subreddit('wallstreetbets')

put = 1
call = 1


print('_-OPTIONS-_')
for c in subreddit.stream.comments():
	
	body = c.body.lower()
	total = put + call
	out = " put: " + str(round(put/total*100,2))+"% call: " + str(round(call/total*100,2)) + '%' 
	


	if "put" in body:
		put = put+1
		print(out, end = '\r', flush = True)
		
		
		
	elif "call" in body:
		call = call + 1
		print(out, end = '\r', flush = True)
	
		
	elif '/' in body:
		
		ticker = re.search(r'[A-Z]{1,5} \d', c.body)
		pos_tsd = re.search(r'[A-Z]{1,5} \d{1,5}[cp] \d{1,2}/\d{1,2}', c.body)
		pos_tds = re.search(r'[A-Z]{1,5} \d{1,2}/\d{1,2} \d{1,5}[cp]', c.body)
	#	print('.')
		if pos_tds is not None:
			print(' ' * len(out) , end = '  \r')
			#print('%s %s %s' % (str(ticker.group(0)), strike.group(0), date.group(0)))
			if ticker is not None:
				#print('Ticker: '+ticker.group(0))
				pass
			print(pos_tds .group(0))
			print('-'*20)
		elif pos_tsd is not None:
			print(' ' * len(out), end = '  \r')
			#print('%s %s %s' % (str(ticker.group(0)), strike.group(0), date.group(0)))
			if ticker is not None:
				#print('Ticker: '+ticker.group(0)
				pass
			print(pos_tsd .group(0))
			print('-' *20)
		
#	print('\n')
