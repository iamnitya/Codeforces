l=input()
p=l.split(' ')
k=int(p[0]) # bananas cost
n=int(p[1]) #amount he had
w=int(p[2]) #no. of bananas
amount_to_paid=int(w*(w+1)*k/2)
borrowed=amount_to_paid-n
if borrowed<=0:
    print(0)
else:
    print(borrowed)
