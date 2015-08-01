#!/usr/bin/python

import time
import re
import glob
import sys

def two():
	with open ("employer.txt", "r") as myfile:
	    	data=myfile.readlines()
		for i,word in enumerate(data):
			print "iteration %i is %s" % (i,word) 

def three():
	prices = {"apple": 1.40, 'banana' : 1.20}
	purchase = { "apple" : 1, 'banana': 6}
	bill = sum(prices [fruit] * purchase[fruit] for fruit in purchase)
	print 'I owe the grocer $%.2f' % bill


def five(name):
	print 'hello', name

def four():
	now = time.localtime()
	hour = now.tm_hour
	if hour < 8:
		print 'sleeping'
	elif hour < 9:
		print 'commuting'
	elif hour < 17:
		print 'working'

def six():
	for string in ['123-5678','ILLEGAL']:
		if re.match(r'^\d{3}-\d{4}$', string):
			print string,'is a valid tel number'
		else:
			print string, 'rejected'

def seven():
	m = re.match(r'(\w+)(\w+)', "Albert Einstein, Scientist")
	print m.group(0)
	print m.group(1)
	print m.group(1,2)

def eight():
	python_files = glob.glob('*.py')
	for fn in sorted(python_files):
		print '----------', fn
		for line in open(fn):
			print ' ' + line.rstrip()

def nine():
	try:
		total = sum(int(arg) for arg in sys.argv[1:])
		print 'sum =', total
	except ValueError:
		print 'Please supply integer numbers on cmd line!'
def main():
	two()
	three()
	four()
	five('Martin')
	six()
	seven()
	eight()
	nine()

#stub to launch main
if __name__ == '__main__':
	            main()
