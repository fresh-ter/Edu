import math
import matplotlib.pyplot as plt

ti=[1,2,3,4,5,6,7]
# ni=[3,4,2,1,1,1,0]
ni=[3,5,2,1,1,1,0]

# ti=[1,2,3,4,5,6,7]
# ni=[5,4,3,2,2,1,0]

flag=True
k=0.0000
kol=7

sum_k_t=int()
sum_exp=int()
sum_nexp=int()
sum_texp=int()
sum_PowExp=int()
sum_total=int()


while(flag==True):
    k=round((k+0.0001),4)

    print(k)

    for i in range(kol):
        sum_nexp+=round(ni[i]*round(math.exp(-k*ti[i]),4),4)
        sum_texp+=round(ti[i]*round(math.exp(-k*ti[i]*2),4),4)
        sum_PowExp+=round(math.exp(-k*ti[i]**2),4)
        sum_total+=round(ni[i]*ti[i]*round(math.exp(-k*ti[i]),4),4)

    check=math.floor(((sum_nexp*sum_texp)/sum_PowExp)-sum_total)

    if check==0 :
        flag=False
        print(sum_nexp)
        print(sum_texp)
        print(sum_PowExp)
        print(sum_total)
        print(k)
    else:
        sum_nexp=0
        sum_texp=0
        sum_PowExp=0
        sum_total=0


#нахождение N
sum_2exp=0

for i in range(kol):
    sum_2exp+=round(math.exp(-2*k*ti[i])*ti[i],2)

print(sum_2exp)


N=math.ceil(sum_total/(k*sum_2exp))
#N=sum_total/(k*sum_2exp)
print(N)


Ni_new=[]
Disrep=[]
Disrep_Pow=[]


for i in range(kol):
    Ni_new.append(N*k*1*math.exp(-k*(ti[i])))
    Disrep.append(ni[i]-Ni_new[i])
    Disrep_Pow.append(Disrep[i]**2)

#print(Ni_new)


print("Значения невязок")

for i in range(kol):
    print(Disrep[i])


print("Значение квадратов невязок")

for i in range(kol):
    print(Disrep_Pow[i])


print("Сумма невязок")
print(sum(Disrep))

print("Количество оставшихся ошибок")
print(math.ceil(N-sum(Ni_new)))


fig1=plt.figure(figsize = (12, 7))
x=[]
y=[]

for i in range(41):
    x.append(i)
    y.append(N*k*math.exp(-k*i))


plt.plot(x,y,label='Модель Джелинского-Моранды')
plt.scatter(ti,ni,label='Начальные значения',color="g")
plt.scatter(ti,Disrep,label='Невязки',color="r")
plt.scatter(ti,Disrep_Pow,label='Квадрат невязок',color="y")
#plt.scatter(ti,Disrep_app,label='Невязки',color="r")
#plt.scatter(ti,Disrep_Pow_app,label='Квадрат невязок',color="y")

plt.grid()

plt.xlabel("t")
plt.ylabel("n")

plt.legend()
plt.show()


#Линейная аппроксимация

a=0
b=0
Mx=0
My=0
Mxy=0
Mx2=0
M2x=0

for i in range(kol):
    Mx+=ti[i]
    My+=ni[i]
    Mxy+=ti[i]*ni[i]
    Mx2+=ti[i]**2

Mx=Mx/kol
My=My/kol
Mxy=Mxy/kol
Mx2=Mx2/kol
M2x=M2x/kol
M2x=Mx**2


a=(Mxy-Mx*My)/(Mx2-M2x)
print('Значение a')
print(a)

b=(Mx2*My-Mx*Mxy)/(Mx2-M2x)
print('Значение b')
print(b)


Ni_new_app=[]
Disrep_app=[]
Disrep_Pow_app=[]

for i in range(kol):
    Ni_new_app.append(a*ti[i]+b)
    Disrep_app.append(ni[i]-Ni_new_app[i])
    Disrep_Pow_app.append(Disrep[i]**2)

print(Ni_new_app)


print("Значения невязок")

for i in range(kol):
    print(Disrep_app[i])


print("Значение квадратов невязок")

for i in range(kol):
    print(Disrep_Pow_app[i])


print("Сумма невязок")
print(sum(Disrep_app))


flag=True
t=0

while(flag):
    P=round(math.pow(1-math.exp(-k*t),N),4)

    if round(P,3)==0.999:
        flag=False
    t+=1

print('Надежность')
print('t= ',t)
print('P= ',P)


fig2=plt.figure(figsize = (12, 7))
x_app=[]
y_app=[]

for i in range(0,11):
    x_app.append(i)
    y_app.append((a*i+b))


plt.plot(x_app,y_app,label='Линия аппроксимации')
plt.scatter(ti,ni,label='Начальные значения',color="g")
plt.scatter(ti,Disrep_app,label='Невязки',color="r")
plt.scatter(ti,Disrep_Pow_app,label='Квадрат невязок',color="y")

plt.grid()

plt.xlabel("t")
plt.ylabel("n")

plt.legend()
plt.show()