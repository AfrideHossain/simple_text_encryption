import string
all_chars = string.ascii_letters+string.punctuation+string.digits+" "
all_charslen = len(all_chars)
def encp(str, shifter):
	nstr = ""
	shift = len(shifter)
	for i in str:
		pos = all_chars.index(i) + 1
		npos = pos +shift
		if npos > all_charslen:
			dpos = npos - all_charslen
			nstr += all_chars[dpos-1]
		else:
			#print(all_chars[npos-1])
			nstr += all_chars[npos-1]
	return nstr
	
def decp(dstr, shifter):
	nstr = ""
	shift = len(shifter)
	for i in dstr:
		pos = all_chars.index(i) + 1
		npos = pos -shift
		if npos > all_charslen:
			dpos = npos - all_charslen
			nstr += all_chars[dpos-1]
		else:
			#print(all_chars[npos-1])
			nstr += all_chars[npos-1]
	return nstr
	
	
#str = "asd9 "			
#encp(str, 4)
#dstr = "ewhcd"
#decp(dstr, 4)

if __name__ == "__main__":
	 
	while True:
		print(
	"""
	+------| Encryption |------+
	+------| Decryption |------+
	+-| Author: Afride Hossain |-+
	"""
	)
	
		print("1. Encrypt")
		print("2. Decrypt")
		print("00. Terminate")
		
		ch = input()
		if ch == '1':
			message = input("\n Enter the message you want to Encrypt: \n")
			key = input("Set key: ")
			out_file_name = input("Enter output file\'s name: ")+".txt"
			encp_message = encp(message, key)
			try:
			    out_file = open(out_file_name, "w")
			    out_file.write(encp_message)
			    print(f"Your Encrypted text has been saved at {out_file_name}")
			except:
			    print("An error occured while writing into file.")
			
			print(f"\nYour Encrypted text is: \n{encp_message}")
			out_file.close()
			
		elif ch == '2':
			#message = input("Enter the text you want to Decrypt: \n")
			in_file_name = input("\nEnter the text\'s file you want to Decrypt: ")
			
			try:
				in_file = open(in_file_name, "r")
				message = in_file.readline()
			
			except Exception as e:
				print("\n")
				print(e)
				exit()
				
			key = input("Unlock key: ")
			decp_message = decp(message, key)
			print(f"\nWish to show you:\n{decp_message}")
			in_file.close()
			
		elif ch =="00":
			print("Program Terminated")
			exit()
			
		else:
		    print("Enter a valid choice!")
		uch = input("\nEnter Q to quite and Enter C to continue. ")
		
		if uch == 'Q' or uch =='q':
			exit()
			
		elif uch == 'c' or uch =='C':
			continue

		else: 
			print("Enter a valid option")
			exit()