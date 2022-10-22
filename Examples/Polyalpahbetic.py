# Author Jatin Jain

# Implementation of Polyalphabetic cipher Technique
from itertools import cycle
def Polyalphabetic_cipher():
	s = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
	finale =''
	Text = "MY NAME IS LELOUCHE VI BRITANNIA" 
	Text = Text.replace(" ", '')
	key = 'ZERO'
	count = 1
	n = len(Text) - len(key)
	
	for i in cycle(key):
		key +=  i
		count+=1
		if count == n:
			break 

	t = [ord(i) - 65  for i in Text]
	K = [ord(i) - 65  for i in key]
	l = s.split()
	map = list([l])
	for i in range(25):
		l = list(l)
		l.append(l[0])
		l.remove(l[0])
		map.append(l)
	for i, j in zip(t, K):
		finale += map[j][i]

	print(f"Plain Text = {Text} \nCipher Text= {finale} \nKey = {key}")

if __name__ == '__main__':
	Polyalphabetic_cipher()