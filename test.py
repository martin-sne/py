#!/usr/bin/python 
import re 
from collections import Counter

global file
file = "employer.txt"

def all():
	for line in open(file):
		print(line.strip())

def tech():
	for line in open(file):
		if re.match(".*Technology.*", line):
			 print(line.strip())

def part():
	with open(file) as textFile:
        	lines = [line.split() for line in textFile]

		for x in range(0, len(lines)):
			print "Name: " + str(lines[x][1]) + "  Salary: " + str(lines[x][4]) 

def reports():
	print "ID Name Position Department Salary"
	for line in open(file):
                print(line.strip())
	print "Report Genrated-------\n"


def details():
	a=[]
	with open(file) as textFile:
                lines = [line.split() for line in textFile]
		for x in range(0, len(lines)):
			s_temp = str(lines[x][4])
			s = s_temp[1:]
			s_new = s.replace(",", "")
			a.append(int(s_new))

		m = max(a)
		p = a.index(m)
		print lines[p][0] + lines[p][1] +lines[p][2] +lines[p][3] +lines[p][4] 

def stats():
	bla=[]
	num_words = 0

	with open(file, 'r') as f:
    		for line in f:
        		words = line.split()
			words_join = ' '.join(words)
			bla.append(words_join)		
        		num_words += len(words)
			
		print "Number of words: " + str(num_words)

		test = ' '.join(bla)

		print Counter(test.split()).most_common()

def main():
	menu = {}
	menu['1'] = "Prints every line" 
	menu['2'] = "only print lines with pattern technology"
	menu['3'] = "print only names and salary"
	menu['4'] = "print report of file"
	menu['5'] = "print details of employee with highest salary"
	menu['6'] = "report number of words, how often a word occurs"
	menu['7'] = "Exit"
 
	while True: 
  		options=menu.keys()
  		options.sort()
    		for entry in options: 
      			print entry, menu[entry]

    		selection=raw_input("Please Select:") 
    		if selection =='1': 
      			all() 
    		elif selection == '2': 
      			tech()
    		elif selection == '3':
      			part() 
    		elif selection == '4': 
     			reports()
    		elif selection == '5': 
     			details()
    		elif selection == '6': 
     			stats()
    		elif selection == '7': 
      			break
    		else: 
      			print "Unknown Option Selected!"

#stub to launch main
if __name__ == '__main__':
    main()
