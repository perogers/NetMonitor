import datetime
import os
import sys
import subprocess
import time

FNULL = open(os.devnull, 'w')
LOG_FILE = 'monitor.log'

def check(host_name, timeout):
    if(subprocess.call(['ping', '-q', '-t', timeout, host_name], stdout=FNULL, stderr=FNULL) > 0) :
        write_to_log('Failed to connect to: {0} on {1}\n'.format(host_name,  str(datetime.datetime.now())))

def main(host_name, timeout, sleeptime):
    start_log='Starting monitor for host: {0} on {1}\n'.format(host_name, str(datetime.datetime.now()))
    print start_log
    write_to_log(start_log)
    while(True):
        check(host_name, timeout)
        time.sleep(sleeptime)

def write_to_log(message):
    logfile = open(LOG_FILE, 'a')
    logfile.write(message)
    logfile.close()

if __name__ == "__main__":
    if( len(sys.argv) < 4 ):
        print "Error:  usage: monitory.py <host> <timeout seconds> <delay seconds>"
        sys.exit(1)
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]))
