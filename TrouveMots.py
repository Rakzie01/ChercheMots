import time
liste = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

mot = input("entrer un mot à 4 lettres ")
chaine =str()

def test(chaine, mot):
   if chaine == mot:
   	print(mot)
   	print("trouvé ton mot est", mot, "!")
   	print("\33[1;31;40m fin\n")
   	time.sleep(999)
	
for l in liste:
	chaine = l
	test(chaine, mot)

	for l2 in liste:
		chaine = l + l2
		test(chaine, mot)
		
		for l3 in liste:
			chaine = l + l2 + l3 
			test(chaine, mot)
			
			for l4 in liste:
				chaine = l + l2 + l3 + l4
				test(chaine, mot)
				print(chaine)