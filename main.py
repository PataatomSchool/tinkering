a = int(input("A> "))
b = int(input("B> "))
c = int(input("C> "))
sumarum = 0
most = 1
mylist = [a, b, c]
for x in mylist:
    if x >= most:
        most = x

mylist.remove(most)
for x in mylist:
    sumarum += x
if sumarum >= most:
    print("it is triangle")
else:
    print("It is not aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
          "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa triangle")