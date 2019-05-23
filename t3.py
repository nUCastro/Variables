import numpy as np
#f=open("mainsq.txt","r")
f=open("giant.txt","r")
x=f.readline()
x=f.read()
f.close()
x=x.split()
star=[]
M=[] #en masas solares
R=[] #en radios solares
T=[] #en temperaturas solares, se asume sol G5
Tsol=5560.0
Helm=[]
for i in range(len(x)/6):
	star.append(x[6*i])
	M.append(float(x[6*i+1]))
	R.append(float(x[6*i+2]))
	T.append(float(x[6*i+5])/Tsol)

for i in range(len(star)):
	tmp=10e-12
	tmp1=R[i]/M[i]
	tmp1=tmp1**(2.5)
	tmp=tmp*tmp1
	tmp=tmp*(R[i]**2*T[i]**4) #luminosidad
	Helm.append(tmp)

for i in range(len(star)):
	print star[i] ," & " , R[i] ," & ",M[i] ," & ",T[i]," & ",Helm[i] ," \\"
