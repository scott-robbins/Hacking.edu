from threading import Thread
import socket
import time 
import sys 


def query_no_wait(rmt, p, request):
    try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((rmt,p))
	s.send(request)
    except socket.error:
        print('[!!] Error Connecting to %s' % rmt)
	pass
    s.close()

def query_and_wait(rmt, p, request):
    reply = ''
    try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((rmt, p))
	s.send(request)
	reply = s.recv(1024)
    except socket.error:
        print('[!!] Error Connecting to %s' % rmt)
	pass
    s.close()
    return reply


# Check Arguments 
if 4>len(sys.argv)>=3:
    rmt_host = sys.argv[1]
    port = int(sys.argv[2])
if len(sys.argv)>=4:
    rmt_host = sys.argv[1]
    port = int(sys.argv[2])
    req = sys.argv[3]
    print query_and_wait(rmt_host, port, req)
elif len(sys.argv)<2:
    print('[!!] Incorrect Usage ')
    print('$ python fuzzy_ask.py <rmt_ip> <port>')
    exit()


