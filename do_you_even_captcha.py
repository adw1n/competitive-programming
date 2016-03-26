#!/usr/bin/env python3.5
import requests
import os, sys, subprocess
url="http://ctf.4programmers.net:37332/"
cookies=None
r=requests.get(url)
print(r.cookies)
while True:

    cookies=r.cookies["session"]
    print(cookies)
    print(r.text.split("\n")[3])
    img_link=r.text.split("\n")[4].split("\"")[1]
    #print(img_link)
    img_name=img_link.split("/")[-1]
    print(img_name)
    img_full_path=url+img_link[1:]
    #print(img_full_path)
    output = subprocess.check_output("wget "+img_full_path, shell=True)
    #print(output)
    output = subprocess.check_output("tesseract "+img_name+" stdout", shell=True)
    output=output.decode("utf-8").replace("\n","")

    print(output)
    print("name "+img_name)
    output = subprocess.check_output("rm "+img_name, shell=True)
    #print("output "+output)
    r=requests.post(url,data={"solution":output,"session":cookies},cookies=r.cookies)
