#!/bin/usr/python

"""
	Hack FACBOOK SQL
"""

import os
import sys
from time import sleep

def type(s):
	for ASU in s + '\n':
		sys.stdout.write(ASU)
		sys.stdout.flush()
		sleep(50. / 1000)

os.system('clear')
print ("""\033[1;31m
         WELCOME TO HACK FACEBOOK SQL
\033[1;31m   ██__________██
___█▒█________█▒█
__█▒███____███▒█
__█▒████████▒▒█
__█▒████▒▒█▒▒██
__████▒▒▒▒▒████
___█▒▒▒▒▒▒▒████
__█▒▒▒▒▒▒▒▒████______█                            _██▒█▒▒▒▒▒█▒▒████__█▒█
_█▒█●█▒▒▒█●█▒▒███_█▒▒█
_█▒▒█▒▒▒▒▒█▒▒▒██_█▒▒█
__█▒▒▒=▲=▒▒▒▒███_██▒█
__██▒▒█♥█▒▒▒▒███__██▒█
____███▒▒▒▒████____█▒█
______██████________███
_______█▒▒████______██
_______█▒▒▒▒▒████__██
_______█▒██▒██████▒█     Shanzida
_______█▒███▒▒▒█████
_____█▒████▒▒▒▒████
______█▒███▒██████__
""")

a = input("\033[1;33m Username target/ID: ")
os.system('clear')
print ("\033[1;36m SQL Server: OK ")
sleep(0.5)
print ("\033[1;36m Check FACEBOOK VALUE. ")
sleep(2)
print ("\033[1;36m Status VALUE: OK!.... ")
print (' ')
print (' ')
print ("\033[1;32m Start SQL TARGET..... ")
print (' ')
type ("\033[1;32m Take Data SQL....")
sleep(0.5)
type ("\033[1;32m Use SQL FACEBOOK...")
sleep(0.5)
type ("\033[1;32m Baypass Access LOG-IN...")
sleep(0.5)
print ("\033[1;32m Baypass Success! ")
sleep(1)
print (' ')

type ("\033[1;32m Looking for Password SQL... ")
sleep(2)
type ("\033[1;32m Got Password SQL...")
sleep(0.5)
type ("\033[1;32m Baypass LOG-IN SQL ")
sleep(2)
print ("\033[1;32m Baypass LOG-IN SQL Success! ")
print (' ')

print ("\033[1;32m Is Login FACEBOOK TARGET...")
sleep(3)
print (' ')
print ("\033[1;33m Username : %s" % (a))
print ("\033[1;33m Password : CAN BE CHANGE IN YOUR HEART ")
sleep(3)
print (' ')
print ("\033[1;32m Login Success! ")
print (' ')
print ("\033[1;32m Change PAGE LOG-IN ")
sleep(2)
print ("\033[1;31m  Success! ")
print (' ')
print ("\033[1;32m Remove LOG-IN SQL ")
sleep(2)
print ("\033[1;31m  Success! ")
print (' ')
sleep(0.5)
print ("""\033[1;35m
Note : 
The username and password have been successful
""")
print (' ')
type ("\033[1;33m THanKs 👍 ")

z = open("pass.txt","w")


message= """
---------------------
Username: %s" % (a)) 
Password: can be changed
---------------------
	"""
z.write(message)
z.close()

os.system('mkdir /sdcard/Results')
os.system('mv pass.txt /sdcard/Results')