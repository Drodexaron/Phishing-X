import time
import pyfiglet
import os

print("Checking for update...")

time.sleep(5)
print("--------------------")
username = input("[+]How can we shall you?: ")
print("--------------------")

time.sleep(2)
print("Welcome " + username + "!")
time.sleep(2)

time.sleep(2)

result = pyfiglet.figlet_format("Phishing X") 
print("--------------------------------------")
print(result) 
time.sleep(2)
print("----------------------------------------------")
print("Made by Anonymous Underground Black Eyes [AUBE]")
print("Note: We are not responsible for your shit")
print("----------------------------------------------")
time.sleep(3)
print("Available Web Pages")
print("-------------------")
print("[1] Facebook \n[2] Instagram \n[3] Twitter \n[4] Xbox \n[5] Camera")

chose = input("[+] Choose the Web Page: ")

if(chose=="1"):
    print("Generating Facebook Web Page...")
    time.sleep(5)
    page = "Facebook"
    print("[●] Link: ")
    time.sleep(2)
    print("[!] waiting for target...")
    

if(chose=="2"):
    print("Generating Instagram Web Page...")
    time.sleep(5)
    page = "Instagram"
    print("[●] Link: ")
    time.sleep(2)
    print("[!] waiting for target...")
    
if(chose=="3"):
    print("Generating Twitter Web Page...")
    time.sleep(5)
    page = "Twitter" 
    print("[●] Link: ")
    time.sleep(2)
    print("[!] waiting for target...")
    
if(chose=="4"):
    print("Generating Xbox Web Page...")
    time.sleep(5)
    page = "Xbox"
    print("[●] Link: ")
    time.sleep(2)
    print("[!] waiting for target...")

if(chose=="5"):
    print("Generating Xbox Web Page...")
    time.sleep(5)
    page = "Camera"
    print("[!] waiting for target...")
