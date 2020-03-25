import os.path
import praw
import re
import sys


def clear():
	sys.stdout.write("\033[F")
	sys.stdout.flush()
	
def write(str):
	clear()
	sys.stdout.write(str+' \r')
	sys.stdout.flush()
	
	#print('\n')


def update(cp,pp, pos, posl):
	
	
#	if posl is None
	p = 'call: %s %% put: %s %%'  % (cp, pp)
	dash = '-' *20
	
	pos = pos + '\n'
	
	print('', end = '\r', flush = True)
	

# bot login credentials
username = ''
password = ''



# Your app details
user_agent = 'bot'
client_id = 'E2efw'
client_secret = 'rU'

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,                                            username=username,
    password=password)
    

subreddit = reddit.subreddit('wallstreetbets')

#if not os.path.exists('words.txt'):
#	f = open('words.txt', 'w+')
#	f.close()
put = 1
call = 1

print('_-OPTIONS-_')
for c in subreddit.stream.comments():
	
	body = c.body.lower()
	total = put + call
	out = " put: " + str(round(put/total*100,2))+"% call: " + str(round(call/total*100,2)) + '%' 
	#print(out)


	if "put" in body:
		put = put+1
		print(out, end = '\r', flush = True)
		#print(c.body)
		
		
	elif "call" in body:
		call = call + 1
		print(out, end = '\r', flush = True)
	
		#print('----')
		#print(c.body)
		
	elif '/' in body:
		strike = re.search(r'\d{1,5}[cp]', body)
		date = re.search(r'\d{1,2}/\d{1,2}', body)
		ticker = re.search(r'\w{1,5}',body)
		pos_tsd = re.search(r'\w{1,5} \d{1,5}[cp] \d{1,2}/\d{1,2}', body)
		pos_tds = re.search(r'\w{1,5} \d{1,2}/\d{1,2} \d{1,5}[cp]', body)
		#print('.')
		if pos_tds is not None:
		#	print(' ' * len(out))
			#print('%s %s %s' % (str(ticker.group(0)), strike.group(0), date.group(0)))
			print(pos_tds.group(0))
		elif pos_tsd is not None:
		#	print(' ' * len(out))
			#print('%s %s %s' % (str(ticker.group(0)), strike.group(0), date.group(0)))
			print(pos_tsd .group(0))
		
#	print('\n')