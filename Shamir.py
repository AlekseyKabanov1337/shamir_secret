import random

s=42
k=int(input('Vvedite porog: '))
n=k-1
a=[]
a.append(s)
for i in range(n):
	a.append(random.randint(3,5))
print(a)
keyx=[]
keyy=[]
while (len(keyx)!=k):
	y=random.randint(1,1000)
	x=random.randint(1,100)
	#print(x,y)
	for i in range(1,n):
		prav=-y+a[i]*x**i
	if s==prav:
		if y not in keyy:
			if x not in keyx:
				keyx.append(x)
				keyy.append(y)
		
for i in range(k):
	print(keyx[i],':', keyy[i], end=' ')

z = 0
for i in range(len(keyy)):
	p1, p2 = 1, 1
	for j in range(len(keyx)):
		if i != j:
			p1 *= -keyx[j]
			p2 *= (keyx[i] - keyx[j])
	z += keyy[i] * p1 / p2
print('\nOur secret:',int(round(-z)))
