from hashlib import md5
from hashlib import sha256
from getarg import *
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
logo = '''
 ____        ____ __  __           _            
|  _ \  ___ / ___|  \/  | __ _ ___| |_ ___ _ __ 
| | | |/ _ \ |   | |\/| |/ _` / __| __/ _ \ '__|
| |_| |  __/ |___| |  | | (_| \__ \ ||  __/ |   
|____/ \___|\____|_|  |_|\__,_|___/\__\___|_|   
                                              
'''
print(B+logo+W)
print("Type decmaster --help to get information")
if isset_arg("--help"):
	print(G+"Basic Using:"+W)
	print(R+'Help\nUsing: decmaster --type [md5 or sha256] --wordlist [wordlist] --hash [md5 or sha256 hash]'+W)
	print(O+'-'*50+W)
	print(O+'-'*50+W)
	print(B+"Generating wordlist: "+W)
	print(R+"Using: decmaster --type [md5 or sha256] --hash [hash] --gen-wordlist [0-99999]")
	print(O+'A dictionary of 1 to 99999 numbers will be generated'+W)
if isset_arg('--type'):
	if parse_arg('--type').lower() == 'sha256':
		if isset_arg('--hash'):
			hash_to = parse_arg('--hash')
			if isset_arg('--wordlist'):
				pass
			elif isset_arg('--gen-wordlist'):
				passlist = []
				dats = parse_arg('--gen-wordlist').strip().split('-')
				try:
					ot = int(dats[0])
					dos = int(dats[1])
				except ValueError:
					print(R+"[-] From and to must be integers"+W)
					exit()
				for jj in range(ot, dos):
					print("Generated {}".format(jj), end="\r")
					passlist.append(str(jj))
				for hashh in passlist:
					if sha256(hashh.encode('utf-8')).hexdigest() == hash_to:
						print(G+'\nHash Found!\nOriginal: {0}\nDecoded: {1}\n'.format(hash_to, hashh))
			else:
				print(R+'[-] Wordlist not specifed!')
				exit()
			if not isset_arg('--gen-wordlist'):
				try:

					f = open(parse_arg('--wordlist'))
				except FileNotFoundError:
					print(R+"[-] File not Found"+W)
					exit()
				passlist = f.read().split('\n')
				f.close()
				for c_passwd in passlist:
					if sha256(c_passwd.encode('utf-8')).hexdigest() == hash_to:
						print(G+'Hash found!\nOriginal hash: {0}\nUncoded hash: {1}'.format(hash_to, c_passwd))
						break
						exit()
			else:
				#print(len(passlist))
				#input()
				for c_passwd in passlist:
					if md5(c_passwd.encode('utf-8')).hexdigest() == hash_to:
						print(G+'\nHash found!\nOriginal hash: {0}\nUncoded hash: {1}'.format(hash_to, c_passwd))
						break
						exit()
	if parse_arg('--type').lower() == 'md5':
		if isset_arg('--hash'):
			hash_to = parse_arg('--hash')
			if isset_arg('--wordlist'):
				pass
			elif isset_arg('--gen-wordlist'):
				passlist = []
				dats = parse_arg('--gen-wordlist').strip().split('-')
				try:
					ot = int(dats[0])
					dos = int(dats[1])
				except ValueError:
					print(R+"[-] From and to must be integers"+W)
					exit()
				for jj in range(ot, dos):
					print("Generated {}".format(jj), end="\r")
					passlist.append(str(jj))
			else:
				print(R+'[-] Wordlist not specifed!')
				exit()
			if not isset_arg('--gen-wordlist'):
				try:

					f = open(parse_arg('--wordlist'))
				except FileNotFoundError:
					print(R+"[-] File not Found"+W)
					exit()
				passlist = f.read().split('\n')
				f.close()
				for c_passwd in passlist:
					print("trying {} ".format(c_passwd), end="\r")
					if md5(c_passwd.encode('utf-8')).hexdigest() == hash_to:
						print(G+'Hash found!\nOriginal hash: {0}\nUncoded hash: {1}'.format(hash_to, c_passwd))
						break
						exit()
			else:
				#print(len(passlist))
				#input()
				for c_passwd in passlist:
					if md5(c_passwd.encode('utf-8')).hexdigest() == hash_to:
						print(G+'\nHash found!\nOriginal hash: {0}\nUncoded hash: {1}'.format(hash_to, c_passwd))
						break
						exit()


		else:
			print(R+'Get Arg --hash error'+W)
			exit()