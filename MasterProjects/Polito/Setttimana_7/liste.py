#fare su python tutor
mylist = ["ciao", "a", "tutti"]
mylist.append("quanti")

a = mylist.pop(1)

l1 = [1,2,3]
l2 = [2,4,5]

l3 = l1+l2
l3_alias = l3

l3_copy = list(l3)
l3_boh = l3 + [ ]

l3[1] = 55

uguali = l3_copy == l3_boh
uguali3 = l1 == l3_boh

maggiore  = l3 > l3_copy
maggiore2 = l1> l3_boh

#___________________

l1  = [1,3,5]
l2 = [2,4,6]

#l_tmp = l1 + l2
#l1 = l_tmp
#l1 = l1 + l2

#l1.extend(l2)
l1.append(l2)

print(l1[0])
print(l1[1])
print(l1[2])
print(l1[3])

#l1[2] = 444
massimo = max(l1)

cc = [0,1] * 5

l1_sorted  = list(l1)
l1_sorted.sort(reverse=True)

#v = l1.sort()
l1_ordinata  = sorted(l1)
l1_ordinata_alias = l1_ordianta
l1_ordinata[:] = [33,55,66,77,88,22]

#a = l1_ordinata.pop(1)
#b = l1_ordinata.pop(1)
#c = l1_ordinata.pop(1)
#l1_ordinata[1:len(l1_ordinata)-1] = []
l1_ordinata[1:-1] = []
l1_ordinata[:] = []