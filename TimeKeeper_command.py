import time
import datetime
import sys
import os
import termios  
import tty
import select

def timing():
    key = raw_input()
    print "Start timing! (Stop with KeyBoardInterrupt(ctrl + c)!)"
    start, startd = time.time(), datetime.datetime.now()

    try:
        while True:
            stop, stopd = time.time(), datetime.datetime.now()
            spend, time_dis = (stop - start), (stopd - startd)
            sys.stdout.write('\r' + '%s' % time_dis)
            sys.stdout.flush()
        
    except KeyboardInterrupt:
        Time_keeper = round(spend,2)
        print "\nEnd timing!\n\nSpend: %s s " % Time_keeper

if __name__ == '__main__':
    key = None
    while key != 'q':
        print "Strike the <Enter> button will start timing:"
        timing()
        print "Input q to quit, or restart!"
        key = raw_input()




