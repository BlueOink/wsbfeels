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
	
def writefile(txt, fn):
	if not os.path.exists(fn):
		f = open(fn, 'w+')
		f.close()
	f = open(fn,'a')
	f.write(txt)
	f.close()
	

# bot login credentials
username = ''
password = ''



# Your app details
user_agent = ''
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
for submission in subreddit.new(limit=999):
	epoch = int(time.time())
	if (epoch - submission.created_utc)/60/60 >= 24:
		break
	submission.comments.replace_more()
	for c in submission.comments.list():

		body = c.body.lower()
		total = put + call
		out = " put: " + str(round(put/total*100,2))+	"% call: " + str(round(call/total*100,2)) + '%' 
	


		if "put" in body:
			put = put+1
			print(out, end = '\r', flush = True)
		
		
		
		elif "call" in body:
			call = call + 1
			print(out, end = '\r', flush = True)
	
		#https://query2.finance.yahoo.com/v7/finance/options/SPY?date=1471564800
		elif '/' in body:
			#print(c.body + '\n%s'%('-'*20))
			strike = re.search(r'\d{1,5}[cCpP]', c.body)
			ticker = re.search(r'(\$)?[A-Z]{2,5}', c.body)
			date = re.search(r' \d{1,2}/\d{1,2}', c.body)
			pos_tsd = re.search(r'[A-Z]{1,5} (\$)?\d{1,5}[cpCP] \d{1,2}/\d{1,2}', c.body)
			pos_tds = re.search(r'[A-Z]{1,5} \d{1,2}/\d{1,2} (\$)?\d{1,5}[cpCP]', c.body)
		
			if pos_tds:
				print(' ' * len(out) , end = '  \r')
				print(pos_tds .group(0))
				writefile(pos_tds.group(0)+':'+c.permalink +',' ,'positions.csv')
				print('-'*20)
			elif pos_tsd:
				print(' ' * len(out), end = '  \r')
				print(pos_tsd .group(0))
				writefile(pos_tsd.group(0) +':'+c.permalink +',', 'positions.csv')
				print('-' *20)
			elif date:
				writefile(date.group(0)+':'+c.permalink + ',', 'dcomments.csv')
			elif strike:
				writefile(strike.group(0)+':'+c.permalink + ',', 'dcomments.csv')
			#elif ticker:
				#writefile(ticker.group(0)+':'+c.permalink + ',', 'dcomments.csv')
		
print('done!')
