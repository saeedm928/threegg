Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a='aaaa bbbb cccc dddd'
l=a.split()
o=[]
for i in range(len(l)-1,-1,-1):
    o.append(l[i])
w=''
for i in o:
    w+=i+' '
print(w)

    