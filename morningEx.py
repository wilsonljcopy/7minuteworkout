# -*- coding: utf-8 -*-
import time

def countDown(n):
	for i in xrange(n + 1):
		print n - i
		time.sleep(1)

def main():
	repeat = 12
	train = 40
	relax = 20
	
	countDown(10)
	print '\nStart!'
	for i in xrange(repeat + 1):
		print 'Ex', i + 1
		print "\a\a\a\a\a"
		countDown(train)
		print "\a\a\a"
		print "Relax..."
		countDown(relax)
	print '\nFinished!'

if __name__ == '__main__':
	main()