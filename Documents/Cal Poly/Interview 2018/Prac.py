#print ("Hello World")


file1 = open("File1.txt")
file2 = open("File2.txt")

lst1 = []
lst2 = []

for word1 in file1:
	lst1.append(word1)
for word2 in file2: 
	lst2.append(word2)

print (lst1) 
print (lst2)

def compar(lst1,lst2):
	idx1 = 0
	idx2 = 0
	lst3 = []

	while lst1[idx1] != None and lst2[idx2] != None:
		if lst1[idx1] < lst2[idx2]:
			print (lst1[idx1])
			idx1+=1
		else:
			print (lst2[idx2])
			idx2+=1
	while lst1[idx1] != None:
		print (lst1[idx1])
		idx1+=1
	while lst2[idx2] != None:
		print (lst2[idx2])
		idx2+=1



#lst1 = ['Bob\n', 'Juliette\n', 'Michael\n', 'Susan']
#lst2 = ['Allison\n', 'Kevin\n', 'Lewis\n', 'Teresa']

print (compar(["a","c","e","g"],["b","d","f","h"]))