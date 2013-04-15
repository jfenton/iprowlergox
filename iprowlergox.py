#!/usr/bin/python
#
# iprowlergox.py (c) Jay Fenton 2013 <na.nu@na.nu>
#

import prowler
import urllib2
import simplejson as json
import sys
import os
import signal
import time

GOX_URL = 'http://data.mtgox.com/api/2/BTCUSD/money/ticker_fast'

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0) # Disable stdout buffering

key = None

try:
	key = open('iprowlergox.conf').read().rstrip('\r\n')
except: pass

if not key:
	print 'Please put your Prowler API key in iprowlergox.conf'
	sys.exit(-1)

if len(sys.argv) < 2:
	print 'Syntax: %s 95 105' % (sys.argv[0])
	sys.exit(-1)

low = float(sys.argv[1])
high = float(sys.argv[2])

p = prowler.Prowl(key)

breach = False

print '[ iWatchGox.py (c) Jay Fenton 2013 <na.nu@na.nu> ]'
sys.stdout.write('Monitoring for breaches of price range %s-%s.' % (str(low), str(high)))

p.post('Now monitoring for breaches of range %s-%s' % (str(low), str(high)), priority=2, app='iprowlergox', event='Monitoring started')

def signal_handler(signal, frame):
	print 'Exiting...'
	sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

while True:
	try:
		sys.stdout.write('.')

		data = json.loads(urllib2.urlopen(GOX_URL).read())
		last = float(data['data']['last']['value'])

		subject = None
		body = 'Mt.Gox USD is @ ' + str(last)

		if breach:
			if last > low:
				subject = 'Price Has Returned To Above Low Watermark'
				breach = False
			elif last < high:
				subject = 'Price Has Returned To Below High Watermark'
				breach = False
		elif last <= low:
			subject = 'Price Has Breached Low Watermark'
			breach = True
		elif last >= high:
			subject = 'Price Has Breached High Watermark'
			breach = True

		if subject and body:
			p.post(body, priority=2, app='iprowlergox', event=subject)
			sys.stdout.write('+')
			time.sleep(25) # Only send notifications at most every 30 seconds

	except:
		sys.stdout.write('!')

	time.sleep(5)

