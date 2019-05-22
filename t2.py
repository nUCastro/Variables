import numpy as np
import matplotlib.pyplot as plt

#cefeidas

a=[0.4,-2.4,0.49,2.81,1.41,3.76,0.54,2.2]
b=[0.6,-2.9,0.57,3.05,1.55,3.75,0.61,1.9]
c=[0.8,-3.5,0.66,3.30,1.70,3.74,0.68,1.7]
d=[1.0,-4.1,0.75,3.55,1.85,3.72,0.75,1.5]
e=[1.2,-4.7,0.84,3.80,2.00,3.71,0.82,1.3]
f=[1.4,-5.3,0.93,4.06,2.15,3.70,0.89,1.0]
g=[1.6,-5.8,1.01,4.32,2.29,3.70,0.97,0.8]
h=[1.8,-6.4,1.10,4.58,2.44,3.69,1.04,0.6]

F=[a,b,c,d,e,f,g,h]

Pi=[]
for i in range(len(F)):
	Pi.append(10**(F[i][0])*np.sqrt((10**(F[i][6]))/((10**(F[i][4]))**3)))
print "Valores de Q para cefeidas \nen el mismo orden que la tabla"
for i in Pi:
	print i
print "Promedio de Q: ", np.mean(Pi)
print "Dispersion de Q: ",np.std(Pi)

p=[F[i][0] for i in range(len(F))]
L=[F[i][3] for i in range(len(F))]
r=[F[i][4] for i in range(len(F))]
gg=[F[i][7] for i in range(len(F))]
def linea(x,a):
	return x*a[0]+a[1]
plt.plot(p,L,'bo',label="Periodo luminosidad")
a1=np.polyfit(p,L,1)
print a1
s="$"+str(round(a1[0],2))+"x"+str(round(a1[1],3))+"$"
plt.ylabel("$log(L/L\odot)$")
plt.xlabel("$log(P)$")
plt.title("Relacion periodo luminosidad")
plt.plot(p,[linea(i,a1) for i in p],label=s)
plt.legend()
plt.show()
plt.plot(p,r,'ro',label="$radio R/R\odot$")
plt.plot(p,gg,'bo',label="Periodo gravedad superficial")
plt.xlabel("$log(P)$")
plt.title("Relacion periodo luminosidad")
b1=np.polyfit(p,r,1)
b2=np.polyfit(p,gg,1)
s1="$"+str(round(b1[0],2))+"x+"+str(round(b1[1],3))+"$"
s2="$"+str(round(b2[0],2))+"x+"+str(round(b2[1],3))+"$"
plt.plot(p,[linea(i,b1) for i in p],label=s1)
plt.plot(p,[linea(i,b2) for i in p],label=s2)

plt.legend()
plt.show()

##delta scuti/enanas cefeidas

aa=[-1.4,2.7,0.20,0.90,0.07,3.91,0.21,4.5]
ab=[-1.0,1.7,0.25,1.22,0.37,3.88,0.25,3.9]
ac=[-0.7,0.8,0.29,1.58,0.59,3.86,0.31,3.6]

G=[aa,ab,ac]
Pi2=[]
for i in range(len(G)):
	Pi2.append(10**(G[i][0])*np.sqrt((10**(G[i][6]))/((10**(G[i][4]))**3)))
print "Valores de Q para enanas cefeidas \ny delta scuti \nen el mismo orden que la tabla"
for i in Pi2:
	print i
print "Promedio de Q: ", np.mean(Pi2)
print "Dispersion de Q: ",np.std(Pi2)

##RR Lyrae

ba=[-0.5,0.7,0.20,1.47,0.54,3.86,-0.26,3.1]
bb=[-0.3,0.7,0.25,1.57,0.67,3.82,-0.26,2.8]
bc=[-0.1,0.7,0.38,1.59,0.76,3.78,-0.26,2.7]

K=[ba,bb,bc]
Pi3=[]
for i in range(len(K)):
	Pi3.append(10**(K[i][0])*np.sqrt((10**(K[i][6]))/((10**(K[i][4]))**3)))
print "Valores de Q para RR Lyrae \nen el mismo orden que la tabla"
for i in Pi3:
	print i
print "Promedio de Q: ", np.mean(Pi3)
print "Dispersion de Q: ",np.std(Pi3)

dsp=[G[i][0] for i in range(len(G))]
dsL=[G[i][3] for i in range(len(G))]
dsr=[G[i][4] for i in range(len(G))]
dsgg=[G[i][7] for i in range(len(G))]

rrp=[K[i][0] for i in range(len(K))]
rrL=[K[i][3] for i in range(len(K))]
rrr=[K[i][4] for i in range(len(K))]
rrgg=[K[i][7] for i in range(len(K))]
plt.title("Periodo Luminosidad")
plt.plot(dsp,dsL,'bo',label="Delta scuti/cefeidas enanas")
plt.plot(rrp,rrL,'ro',label="RR Lyrae")
plt.plot([min(dsp+rrp),max(dsp+rrp)],[linea(min(dsp+rrp),a1),linea(max(dsp+rrp),a1)],label="Ajuste lineal")
plt.legend()
plt.ylabel("$log(L/L\odot)$")
plt.xlabel("$log(P)$")
plt.show()
plt.title("Periodo radio")
plt.plot(dsp,dsr,'bo',label="Delta scuti/cefeidas enanas")
plt.plot(rrp,rrr,'ro',label="RR Lyrae")
plt.plot([min(dsp+rrp),max(dsp+rrp)],[linea(min(dsp+rrp),b1),linea(max(dsp+rrp),b1)],label="Ajuste lineal")
plt.legend()
plt.ylabel("$log(R/R\odot)$")
plt.xlabel("$log(P)$")
plt.show()
plt.title("Periodo gravedad superficial")
plt.plot(dsp,dsgg,'bo',label="Delta scuti/cefeidas enanas")
plt.plot(rrp,rrgg,'ro',label="RR Lyrae")
plt.plot([min(dsp+rrp),max(dsp+rrp)],[linea(min(dsp+rrp),b2),linea(max(dsp+rrp),b2)],label="Ajuste lineal")
plt.legend()
plt.ylabel("$log(g)$")
plt.xlabel("$log(P)$")
plt.show()