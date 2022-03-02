t=int(input())
for i in range(t):
   n=input()
   l=len(n)
   p=l-2
   k=str(p) 
   f=(n[0])
   e=(n[l-1])
   if l<=10:
       print(n)
   else:
       print(f+k+e)
