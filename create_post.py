 import os
import re
#if not os.path.exists('f.txt'):
#	f = open('f.txt', 'w+')
#	f.close()
	
def rint(txt, fn = 'out.txt'):
	if not os.path.exists(fn):
		f = open(fn, 'w+')
		f.close()
	f = open(fn,'a')
	f.write(txt)
	f.close()
	
f = open('positions.csv', 'r')
c = f.readline()

plays = c.split(',')

calls = []
puts = []
for p in set(plays):
	sc = re.search(r'\d{1,5}c', p.split(':')[0])
	sp = re.search(r'\d{1,5}p', p.split(':')[0])
	if sc:
		calls.append(p)
	if sp:
		puts.append(p)
	
#print('~~~~')
print('-' * 20)
print('CALLS')
print('-'*20)

for call in sorted(calls):
	play = call.split(':')[0]
	url = call.split(':')[1]
	print('[%s](%s)\n' %(play, url))
	
print('-' * 20)
print('PUTS')
print('-' * 20)

for put in sorted(puts):
	play = put.split(':')[0]
	url = put.split(':')[1]
	print('[%s](%s)\n' %(play, url))

print('and since im unable to capture all positions, heres some comments that *might* have plays in them:\n')

m = open('dcomments.csv', 'r')
mp = m.readline()

u = mp.split(',')

for ur in u:
	#print(ur)
	try:
		sig = ur.split(':')[0]
		url = ur.split(':')[1]
		print('[%s](%s)' % (sig, url))
	except:
		pass

	
