#!/usr/bin/env python3.5
import getpass
import sys
import telnetlib
from langdetect import detect

HOST="ctf.4programmers.net"
PORT="37331"
tn = telnetlib.Telnet(HOST,PORT)


while True:
    line_of_text=tn.read_until(match=b"\n") #'Choose: arp,rmr,fr,en,de,hu,sa,pl 0/300\n'
    print(line_of_text)
    line_of_text=tn.read_until(match=b"\n",timeout=1) #b'la diesen handedruck dir sagen in einem hochgewolbten engen gotischen zimmer faust ...'
    print(line_of_text)

    language=detect(line_of_text.decode("utf-8"))
    print(language)
    tn.write(str.encode(language+"\n"))
