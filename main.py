__author__ = 'Carlos'

import time

def timeNow():
    localtime = time.asctime( time.localtime(time.time()) )
    print "Hello world!", "your local time is: ", localtime

def main():
    timeNow()

if __name__ == '__main__':
    main()
