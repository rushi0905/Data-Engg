thistupple = ("Orange","Apple","Banana")
listnew= list(thistupple)
listnew.append("Keal")
listnew.remove("Apple")
thistupple = tuple(listnew)
del thistupple
# print(thistupple)

acessories = ("mouse","laptop","Keyboard")
new_acessories = ("SSD",)
acessories += new_acessories
# new_acessories.remove("SSD",)
print(acessories)

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green.upper())
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

thistuple1 = ("apple", "banana", "cherry")
for i in range(len(thistuple1)):
  print(thistuple1[i])