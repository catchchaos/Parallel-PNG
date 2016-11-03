import rsaFunctions
from encrypt import encrypt
from decrypt import decrypt

from random import randint
import subprocess as sp

_LIMIT = 10000000
if __name__ == '__main__':
	p = randint(1000, _LIMIT)
	q = randint(1000, _LIMIT)
	
	cmd_p = r'./a.out ' + str(p)
	cmd_q = r'./a.out ' + str(q)
	output_p = sp.check_output(cmd_p, shell=True)
	output_q = sp.check_output(cmd_q, shell=True)
	
	p = int(output_p)
	q = int(output_q)
	

	LLI = (p*q)>(2**31-1) # Check if product of p,q is higher than long long int
	print "Is long: ",LLI
	public, private = rsaFunctions.getKeyPair(p, q)
	print "Public key : ", public ," Private key : ", private
	msg = raw_input("Enter message : ")
	if LLI:
		encMsg = rsaFunctions.encrypt((public[0], public[1]), msg)
	else:
		msgInt = map(lambda x:ord(x),msg)
		encMsg = encrypt(public[0], public[1], msgInt)
	print "Encrypted message : "
	for i in range(len(encMsg)):
		print encMsg[i],
	if LLI:
		dec = rsaFunctions.decrypt((private[0], private[1]), encMsg)
	else:
		decMsg = decrypt(private[0], private[1], encMsg)
		dec = map(lambda x:chr(x),decMsg)
	print "\nDecrypted Message :"
	print dec
