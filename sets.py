
# se = set()
#
# se.add(1)
# se.update(2)

l1 = {1, 2, 3, 4, 5, 6, 7,}
l2 = {1, 2, 3, 4, 5, 8 }

#Union
print(l1 | l2)  # {1, 2, 3, 4, 5, 6, 7}

#Intersection
print(l1 & l2) # {1, 2, 3, 4, 5}

#difference
print(l1 - l2) # {6, 7}
print(l2 - l1) # None

#Symetric diff
print(l1 ^ l2) # {6, 7, 8}


