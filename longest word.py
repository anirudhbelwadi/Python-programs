def flw(a):
               lw=''
               for b in a:
                   if len(b)>len(lw):
                       lw=b
               print("Longest word : "+lw)
c=input("Enter some words : ")
a=c.split()
flw(a)
