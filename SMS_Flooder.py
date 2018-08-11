from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC7c326140b219712c63fab1fd5a2841fa"
# Your Auth Token from twilio.com/console
auth_token  = "b2fa72320beb5841da8641ae5d5065f9"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+556140421608", 
    from_="+5521980536720",
    body="💀💀💀💀")

print(message.sid)

client = Client(account_sid, auth_token)

global end, verde, azul, amarelo, vermelho, purpleClaro, normal, cyanClaro, W, R, G, O, B, P, C, GR
end = '\033[0m'
# Colors

W  = '\033[0m'  # white (default)
R  = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
cyanClaro="\033[1;36m"
vermelho = '\033[31;1m'
verde = '\033[32;1m'
azul = '\033[34;1m'
amarelo= '\033[1;33m'
normal = '\033[0;0m'
purpleClaro= '\033[1;35m'


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering
time.sleep(8./90)

def Animation(String):
    animation = "|/-\\"
    for i in range(15):
        time.sleep(0.1)
        sys.stdout.write("\r" + "[" + animation[i % len(animation)] + "]" + G + String)
        sys.stdout.flush()
print('')

BannerOld = """
____________¶¶¶
___________¶___¶
____________¶¶¶
____________¶_¶
____________¶_¶
__________¶¶¶_¶¶¶                  
________¶¶__¶¶¶__¶¶¶            ▒█▀▀▀█ ▒█▀▄▀█ ▒█▀▀▀█  ▒█▀▀▀ █░░ █▀▀█ █▀▀█ █▀▀▄ █▀▀ █▀▀█  
______¶¶__¶¶¶¶¶¶¶___¶           ░▀▀▀▄▄ ▒█▒█▒█ ░▀▀▀▄▄  ▒█▀▀▀ █░░ █░░█ █░░█ █░░█ █▀▀ █▄▄▀ 
_____¶_______________¶          ▒█▄▄▄█ ▒█░░▒█ ▒█▄▄▄█  ▒█░░░ ▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀░ ▀▀▀ ▀░▀▀ 
____¶_________________¶
____¶_________________¶              +==========================================+
____¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶            |      SMS Sending Spam and Flooder        |
____¶____¶_______________¶           +==========================================+
____¶____¶___¶¶¶¶¶¶¶¶¶¶¶¶¶           | ♚ Coded: łuŧЋ1єr ルシアー                |
____¶___¶___¶___________¶¶¶          | ♚ Contact: @DreadPirateRobertt (Telegram)|
____¶___¶___¶_¶¶¶___¶¶¶__¶¶          | ♚ Date: 07/03/2017                       |
____¶___¶___¶_¶¶¶___¶¶¶__¶¶          | ♚ I take no responsibilities for the     |
____¶___¶___¶___________¶¶¶          |   use of this program !                  |
____¶____¶___¶¶¶¶¶¶¶¶¶¶¶¶¶           +==========================================+
____¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶             |          łαbørαŧøriø Fαηŧαsмα            |
____¶_________________¶              +==========================================+
____¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶
____¶___¶__¶__¶__¶__¶                          [1] ✉ Mensagem Normal
____¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶                          [2] ✉ Spam
____¶__¶___¶__¶__¶__¶                          [3] ✉ Historico de Mensagens
____¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
___¶¶¶_________________¶¶¶"""

BannerEnd = """_____________¶____¶ 
_________¶_¶¶¶¶¶¶¶¶¶¶ 
_____¶¶¶¶¶¶¶_________¶ 
___¶¶¶¶¶_____________¶ 
___¶_________________¶ 
____¶________________¶¶ 
____¶¶________________¶ 
_____¶________________¶¶ 
_____¶¶_______¶¶¶____¶¶¶ 
______¶_____¶¶___¶¶_¶___¶ 
______¶_____¶¶_____¶____¶ 
______¶¶____¶______¶¶¶¶¶¶¶     ╭━━━┳━╮╭━┳━━━╮╭━━━┳╮╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╭━━━╮╱╱╱╱╭╮
_______¶____¶¶__¶¶¶_____¶¶     ┃╭━╮┃┃╰╯┃┃╭━╮┃┃╭━━┫┃╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱┃╭━━╯╱╱╱╱┃┃
______¶¶¶¶____¶¶¶¶_____¶¶      ┃╰━━┫╭╮╭╮┃╰━━╮┃╰━━┫┃╭━━┳━━┳━╯┣━━┳━╮┃╰━━┳━╮╭━╯┃
______¶¶¶_______________¶¶     ╰━━╮┃┃┃┃┃┣━━╮┃┃╭━━┫┃┃╭╮┃╭╮┃╭╮┃┃━┫╭╯┃╭━━┫╭╮┫╭╮┃
_______¶¶¶______________¶¶     ┃╰━╯┃┃┃┃┃┃╰━╯┃┃┃╱╱┃╰┫╰╯┃╰╯┃╰╯┃┃━┫┃╱┃╰━━┫┃┃┃╰╯┃
________¶_____¶¶¶¶¶¶¶¶¶¶¶      ╰━━━┻╯╰╯╰┻━━━╯╰╯╱╱╰━┻━━┻━━┻━━┻━━┻╯╱╰━━━┻╯╰┻━━╯
_______¶¶_______¶¶¶¶¶ 
______¶¶¶¶¶_____¶ 
___¶¶¶¶__¶¶¶¶¶¶¶¶ 
__¶¶____¶¶_____¶¶ 
_¶¶_____¶¶______¶¶ 
¶¶______¶¶_______¶¶ 
_¶¶¶¶¶___¶¶______¶¶ 
_¶__¶¶¶¶¶¶_______¶¶ 
¶¶____¶___________¶¶ 
¶____¶¶__________¶¶¶ 
¶____¶¶____________¶ 
¶_____¶___________¶¶¶ 
¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶_¶ 
¶______¶_________¶___¶ 
¶¶¶¶__¶__________¶_¶¶¶ 
_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
___¶¶¶¶¶¶¶¶¶____¶ 
___¶¶___¶__¶____¶ 
___¶____¶__¶____¶ 
___¶¶___¶__¶____¶¶ 
__¶_______¶¶¶¶¶¶¶¶¶¶ 
_¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶ 
_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶"""


print azul + BannerOld
print('')
slowprint(P+" ♚ Coded: łuŧЋ1єr ルシアー ")
print('')
Animation(" ✉ SMS - Flooder ✉  ")
print('')

try:
	opt = raw_input(amarelo + '[*] Choose an Option > ')
except KeyboardInterrupt:
	print(vermelho+"\n \n[-] Exiting....")
	time.sleep(3)
	print cyanClaro + BannerEnd
	exit()
print('')

def Ma1n():
	global body, to, from_ 
	body = raw_input(cyanClaro + "[*] Digite sua Mensagem > ")
	print('')
	to =   raw_input(cyanClaro + '[*] Digite numero do alvo > ')
	print('')
	img =  raw_input(amarelo + "[*] Deseja enviar uma imagem? [y/N] > ")
	if img == 'y':
		img2 = raw_input(amarelo + '[*] Deseja enviar mais de uma (1) imagens? [y/N] > ')
		print('')
		if img2 == 'n':
			SendImage(to)
		elif img2 == 'y':
			MultipleImages(to)
	elif img == 'n':
		SendMessage(to)
	else:
		print('')
		print(vermelho + '[-] Wrong option...\n')
		main()
	return body, to, from_


def SendMessage(to):
	try:
		message = client.messages.create(
		    body = body, 	
	    	to = to,
	    	from_ = from_,
		)
		print('')
		print(verde +'✉ SMS - Flooder ✉ %s' % to)
		print('')
		print (vermelho + '[*] ID > '+azul+message.sid+end)
		print('')
		time.sleep(25)
	except:
		pass


def SendImage(to):
	print('')
	Animation(" ✉ SMS - Flooder ✉  ")
	print('')
	media_url = raw_input("[*] Digite a url da sua imagem > ")
	message = client.messages.create(	
   		body = body, 
   		to = to,
  	 	from_ = from_,
 	 	media_url = media_url,
	)
	print('')
	print ('[+] '+verde+'✉'+vermelho+' Imagem  Enviada Com Sucesso!' + end)
	print('')

def MultipleImages(to):
	numbers = raw_input(amarelo + '[*] Digite o numero de imagens [2/3] > ')
	print('')
	if numbers == '2':
		media_url1 = raw_input(amarelo + '[*] Digite a url da sua primeira imagem > ')
		media_url2 = raw_input(amarelo + '[*] Digite a url da sua segunda imagem > ')
		print('')
		message = client.messages.create(
			body = body,   # Message body, if any
	    	to = to,	
    		from_ = from_,
    		media_url=[
       		 	media_url1,
        		media_url2,
    		],
		)
		print('')
		print(verde+'✉'+vermelho+'Imagens Enviadas Com Sucesso!...')
		print('')
	elif numbers == '3':
		media_url1 = input('[1] Digite a url da sua Primeira imagem > ')
		media_url2 = input('[2] Digite a url da sua Segunda imagem > ')
		media_url3 = input('[3] Digite a url da sua Terceira imagem > ')
		print('')
		message = client.messages.create(
			body = body,  # Message body, if any
    		to=to,
    		from_=from_,
    		media_url=[
   		   		media_url1,
   		     	media_url2,
        		media_url3,
    		],
		)
		print('')
		print(verde+'[+]'+vermelho+'Imagens Enviadas Com Sucesso!...')		
	else:
		print('')
		print(vermelho + "Digite uma opção valida...")
		print('')

def Retrieving():
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
	for message in client.messages.list():
		Historico = (message.body)
		print ("Historico de mensagens Enviadas > ", Historico )


def SpamNumber():
	global body, to, from_
	body = raw_input(cyanClaro + "[*] Digite sua Mensagem > ")
	print('')
	to =   raw_input(cyanClaro + '[*] Digite numero do alvo > ')
	print('')
	FloodNumber = int(input(verde + "Digite o numero de Flooder > "))
	print('')
	img =  raw_input(amarelo + "[*] Deseja enviar uma imagem? [y/N] > ")
	print('')
	if img == 'y':
		img2 = raw_input(amarelo + '[*] Deseja enviar mais de uma (1) imagens? [y/N] > ')
		print('')
		if img2 == 'n':
			for i in rage(1, FloodNumber+1):
				SendImage(to)
				print purpleClaro + "\r ✉ SMS - Flooder ✉ - Total enviados > %i" % i
				print('')
		elif img2 == 'y':
			for i in rage(1, FloodNumber+1):
				MultipleImages(to)
				print purpleClaro + "\r ✉ SMS - Flooder ✉ - Total enviados > %i" % i
				print('')

	for i in range(1, FloodNumber+1):
		SendMessage(to)
	print purpleClaro + "\r ✉ SMS - Flooder ✉ - Total enviados > %i" % i
	print('')

def SPAM():
	global body, to, from_
	print(vermelho + "+==========================================+")
	print(vermelho + "|              ✉ SPAM MODE ✉               |")
	print(vermelho + "+==========================================+")
	print('')
	options = raw_input(verde+"[+] Deseja Usar uma lista de Numeros (n/Y)?")
	if options == 'n'.lower():
		SpamNumber()
		exit()
	else:
		pass
	print('')	
	body = raw_input(cyanClaro + "[*] Digite sua Mensagem > ")
	print('')
	wordlist =   raw_input(cyanClaro + '[*] Digite Sua Lista de Numeros > ')
	print('')
	to = open(wordlist, 'r').readlines()
	from_ = from_
	FloodNumber = int(input(verde + "Digite o numero de Flooder > "))
	print('')
	img =  raw_input(amarelo + "[*] Deseja enviar uma imagem? [y/N] > ")
	print('')
	if img == 'y':
		img2 = raw_input(amarelo + '[*] Deseja enviar mais de uma (1) imagens? [y/N] > ')
		print('')
		if img2 == 'n':
			for i in rage(1, FloodNumber+1):
				SendImage(to)
				print purpleClaro + "\r ✉ SMS - Flooder ✉ - Total enviados > %i" % i
				print('')
		elif img2 == 'y':
			for i in rage(1, FloodNumber+1):
				MultipleImages(to)
				print purpleClaro + "\r ✉ SMS - Flooder ✉ - Total enviados > %i" % i
				print('')

	for i in range(1, FloodNumber+1):
		for Number in to:
			SendMessage(Number)
		print purpleClaro + "\r ✉ SMS - Flooder ✉ - Total enviados > %i" % i
		print('')


def main():
	if opt == '1':
		try:
			Ma1n()
		except KeyboardInterrupt:
			print(vermelho + '\n \n[-] Exiting...')
			time.sleep(3)
			os.system('clear')
			print cyanClaro + BannerEnd
			exit()
	elif opt == '3':
		try:
			Retrieving()		
		except KeyboardInterrupt:
			print(vermelho + "\n \n[-] Exiting....")
			time.sleep(3)
			os.system('clear')
			print cyanClaro + BannerEnd
	elif opt == '2':
		try:
			SPAM()
		except KeyboardInterrupt:
			print(vermelho+"\n \n[-] Exiting....")
			time.sleep(3)
			os.system('clear')
			print cyanClaro + BannerEnd

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print(vermelho+'\n\n[-] Exiting...')
		time.sleep(3)
		os.system('clear')
		print cyanClaro + BannerEnd
		exit()
