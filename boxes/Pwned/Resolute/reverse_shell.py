from Crypto.Random import get_random_bytes
from threading import Thread
from numpy import random
import base64
import socket 
import time 
import sys 
import os 

def fuzz_request(ip,p, payload):
    reply = ''
	# Make Socket 
    try:
	 sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
         print '\033[1m[!!]\033[31m Unable to Create Socket\033[0m'
    	 time.sleep(0.5)
	 return reply
    try:
        sock.connect((ip,p))
        sock.send(payload)
        #print '[*] Payload Delivered to %s' % url
        tic = time.time()
        recvd = False
        while not recvd and (time.time()-tic)-timeout:
            reply = sock.recv(1024)
	    #print '[*] Got Reply %s' % reply
	    recvd = True
    except socket.error:
        pass
    sock.close()
    return reply



port = 80
url = sys.argv[1]
if len(sys.argv)>2:
    port = int(sys.argv[2])

# Craft Reverse Shell Payload 
# payload = '\x21\x23\x62\x2f\x6e\x69\x73\x2f\x0a'
psize = [5, 100]
t0 = time.time()
fuzzing = True
timeout = 5
reply = ''

print '** \033[1m\033[31mStarting Fuzzer ** \033[0m'
try:
    while fuzzing:
	n_bytes = random.random_integers(psize[0],psize[1], 1)[0]
        asdf = base64.b64encode(get_random_bytes(n_bytes))
        reply = fuzz_request(url,port,asdf)
	# See if anything useful happened
	header = reply.split('\n')[0]
	if 'HTTP/1.1' in header:
		print 'Got a something?! %s' % header
		if 'OK' in header.split(' '):
		    print '[!?] Might have found something...' 
	time.sleep(random.random_integers(1,100)/100.)	
except KeyboardInterrupt:
    print '[!!] Reverse-Shell Fuzzer Killed [%ss Elapsed]' %\
    	  str(time.time()-t0)
if not fuzzing:
    print '* %s' % reply
    print '** %s' % asdf

