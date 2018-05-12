import math
from string import *
from utility import *


def find_triple(lst):
    for idx in range(0,len(lst)-2,1):
        if lst[idx] == lst[idx+1] == lst[idx+2]:
            return(lst[idx],idx)
    return None

x = [0,1,2,2,3,3,3,4,5]
#print(find_triple(x))

def get_nums(lst):
    result = find_triple(lst)
    if result == None:
        return 'No triples'
    else:
        nlst = list()
        for idx in result:
            nlst.append(result[idx])
        return nlst


"""def get_captials(lst): #take in a list of words and return capital
    nlst = list()
    for word in lst:
        if ord(word[0]) >= 65 and ord(word[0]) <= 90:
            nlst.append(word)
    return nlst

words1 = ['HEllo','Goodbye','etc.']
print get_captials(words1)"""

def get_captials(lst): #take in a list of words and return capital
    nlst = list()
    for word in lst:
        for letter in word:
            if letter.isupper() == True:
                nlst.append(word)
    return nlst

words1 = ['HELLO','Goodbye','etc.']
#print get_captials(words1)

def word_length_filter(list,min,max):
    nlst = list()
    for word in list:
        if len(word) >= len(min) and len(word) < len(max):
            nlst.append(word)
    return nlst

def col_to_list(mat,colnum):
    nlst = list()
    for list in mat:
        if colnum < len(list):
            nlst.append(list[colnum])
        else:
            return None
    return nlst


def get_columns(matrix,entry):
    nlst = list()
    for row in matrix:
        nlst.append(row[entry])
    return nlst

def shift_digits(string):
    nlst = list()
    for char in string:
        if char == "9":
            nlst.append("0")
        elif char.isdigit() == True:
            result = int(char) + 1
            nlst.append(str(result))
        else:
            nlst.append(char)
    return ''.join(nlst)


def add_numbers(str):
    nlst = list()
    for char in str:
        if ord(char) >= 48 and ord(char) <= 55:
            result = int(char)+2
            nlst.append(result)
        elif ord(char) == 56:
            nlst.append(0)
        elif ord(char) == 57:
            nlst.append(1)
        else:
            nlst.append(char)
    return nlst

def add_list_idx(lst1,lst2):
    return [lst1[0]+lst2[0],lst1[1]+lst2[1],lst1[2]+lst2[2]]

def index_of_smallest(lst):
    if len(lst) > 0:
        min = lst[0]
        result = 0
        for idx in range(1,len(lst),1):
            if min > lst[idx]:
                min = lst[idx]
                result = idx
        return result
    else:
        return None

def final3(list):
    for idx in range(0,len(list)-1,1):
        if list[idx] == 1 and list[idx] == list[idx+1]:
            list[idx] = 0
    return list

x = [0,0,1,1]
#print final3(x)


"""def final4(string):
    nlst = list()
    lst = string.split(' ') #lst = ["Hello","World"]
    for word in lst:
        firstLetter = word[0]
        lastLetter = word[len(word)-1]
        for letterIDX in range(0,len(word),1):
            if letterIDX == 0:
                nlst.append(lastLetter)
            elif letterIDX == len(word)-1:
                nlst.append(firstLetter)
            else:
                nlst.append(word[letterIDX])
    return ''.join(nlst)

print final4("Hello World")"""

def final4(string):
    nlst = list()
    lst = string.split() #lst = ["Hello","World"]
    for word in lst:
        firstLetter = word[0]
        lastLetter = word[len(word)-1]
        for letterIdx in range(0,len(word),1):
            if letterIdx == 0:
                nlst.append(lastLetter)
            elif letterIdx == len(word)-1:
                nlst.append(firstLetter)
            elif letterIdx != 0 and letterIdx != len(word)-1:
                nlst.append(word[letterIdx])
            elif letterIdx == word[letterIdx][len([word][letterIdx])-1]:
                nlst.append(' ')

    return ''.join(nlst)

#print final4("Hello World")


def final5(matrix):
    for listIDX in range(0,len(matrix),1):
        for entryIDX in range(0,len(matrix[listIDX]),1):
            if listIDX == entryIDX:
                matrix[listIDX][entryIDX] = 0
    return matrix

mat = [[1,2,3],[4,5,6],[7,8,9]]
#print final5(mat)

def final5_2(matrix):
    #listIDX = 0 #from 0 - 2
    letterIDX = 2 # from 2 - 0
    for listIDX in range(0,len(matrix),1): #0 - 2
        while letterIDX >= 0:
            matrix[listIDX][letterIDX] = 0
            listIDX += 1
            letterIDX -= 1 # 2- 0
    return matrix


mat = [[1,2,3],[4,5,6],[7,8,9]]
#print final5_2(mat)
# Final7

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        xpt = epsilon_equal(self.x,other.x)
        ypt = epsilon_equal(self.y,other.y)
        return xpt and ypt

    def __repr__(self):
        return 'point,x={0},y={1}'.format(self.x,self.y)

class Circle():
    def __init__(self,point,radius):
        self.point = point
        self.radius = radius

    def __eq__(self,other):
        pt = epilson_equal(self.point,other.point)
        rad = epilson_equal(self.radius,other.radius)
        return pt and rad

    def __repr__(self):
        return 'circle,point ={0},radius={1}'.format(self.point,self.radius)

class Square():
    def __init__(self,point1,point2,point3,point4):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.point4 = point4

    def __eq__(self,other):
        pt1 = epilson_equal(self.pt1,other.pt1)
        pt2 = epilson_equal(self.pt2,other.pt2)
        pt3 = epilson_equal(self.pt3,other.pt3)
        pt4 = epilson_equal(self.pt4,other.pt4)
        return pt1 and pt2 and pt3 and pt4

def final7(list):
    TotalPtX = 0
    TotalPtY = 0
    circleIDX = 0
    while circleIDX <= len(list)-1: #len(list) - 1 = 2
            TotalPtX += float(list[circleIDX].point.x)
            TotalPtY += float(list[circleIDX].point.y)
            AveragePtX = TotalPtX/len(list)
            AveragePtY = TotalPtY/len(list)
            circleIDX += 1
    return Point(AveragePtX,AveragePtY)


list = [Circle(Point(5,5),10), Circle(Point(3,3),10), Circle(Point(6,6),10)]
#print final7(list)

"""def func(n):
    if n>0:
    	return n+1
    else:
		raise myException()
try:
    print ("Good")
except myException():
    print("Bad")

print func(-5)"""

def Rectangle(pt1,pt2,pt3,pt4):
    width = pt2.x - pt1.x
    height = pt3.y - pt1.y
    area = width*height
    return area

#print Rectangle(Point(0,0),Point(4,0),Point(0,4),Point(4,4))

def do_twice(f):
    f()
    f()

def print_spam():
    print 'spam'

string1 = ["A","A","A","B",1,2,3,1]
#print string1.count("A")

def has_duplicates(list):
    for idx in range(0,len(list)-1,1):
        if list[idx] == list[idx + 1]:
            return True
        else:
            return False

#print has_duplicates([1,2,3])

def while_test(x):
    while x<10:
        print x
        x+=1

#print while_test(6)

word = 'banana'
count = 0
for letters in word:
    if letters == 'a':
        count += 1
#print count

def count_letters(word,letter):
    count = 0
    for let in word:
        if let == letter:
            count += 1
    return count

#print count_letters("bananaaa","a")

word1 = 'abcd'
#print word1.isupper()

def in_both(word1,word2):
    for letter in word1:
        if letter in word2:
            print letter

def any_lowercase1(s):
    for letters in s:
        if letters.islower() == True:
            print letters

#print any_lowercase1("Gas")
#text = raw_input("just let it all end")
#print text

def find_repent(lst):
    for idx in range(0,len(lst)-1,1):
        if lst[idx] == lst[idx+1]:
            return [lst[idx],idx]
    return None

#print find_repent([1,2,3,4,4,5])

def col_to_list(nums,colIDX):
    nlst = list()
    for lst in nums:
        if colIDX < len(lst):
            nlst.append(lst[colIDX])
        else:
            nlst.append(None)
    return nlst

#print col_to_list([[1,2,3],[4,6],[7,8,9]],2)

x = [1,323,"hello",5,[3,4]]
y = "HELLO WORLDDDDDDDDDDDDDDDD"
#print y.isupper()

def func(n):
    if n>0:
        return n+1
    else:
        raise NameError('test')


try:
    func(-5)
    print "Good"
except NameError:
    print "Bad"
