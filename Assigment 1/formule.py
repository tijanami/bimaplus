# KORISNIH DEFINISE BROJ TACAKA

n = int(input ("How many poligons do you want"))



# KORISNIK UNOSI KOORDINATE

x=[]
y=[]

for i in range (0,n):
    x.append(float(input("enter value of x")))

    y.append(float(input("enter value of y")))


# PRINT KOORDINATA

print ("point    " "x,     " "y")
print ("_ _ _ _ _ _ _ _ _ _ _  ")
for i in range (0,n):      
    print(i+1,":   ", x[i], ",   ", y[i])

# PRORACUN 

listAx=[]
for i in range (0,n):
    listAx.append((x[i]+x[i-1])*(y[i]-y[i-1]))
Ax=0.5*sum(listAx)
print(f"Ax= {Ax:.2f}")

listSx=[]
for i in range (0,n):
    listSx.append((x[i]-x[i-1])*(y[i]*y[i]+y[i-1]*y[i]+y[i-1]*y[i-1]))
Sx=-1/6*sum(listSx)
print(f"Sx= {Sx:.2f}")

listSy=[]
for i in range (0,n):
    listSy.append((y[i]-y[i-1])*(x[i]*x[i]+x[i-1]*x[i]+x[i-1]*x[i-1]))
Sy=1/6*sum(listSy)
print(f"Sy= {Sy:.2f}")

listIx=[]
for i in range (0,n):
    listIx.append((x[i]-x[i-1])*(y[i]*y[i]*y[i]+y[i]*y[i]*y[i-1]+y[i]*y[i-1]*y[i-1]+y[i-1]*y[i-1]*y[i-1]))
Ix=-1/12*sum(listIx)
print(f"Ix= {Ix:.2f}")

listIy=[]
for i in range (0,n):
    listIy.append((y[i]-y[i-1])*(x[i]**3+x[i]**2*x[i-1]+x[i]*x[i-1]**2+x[i-1]**3))
Iy=1/12*sum(listIy)
print(f"Iy= {Iy:.2f}")

listIxy=[]
for i in range (0,n):
    listIxy.append((y[i]-y[i-1])*(y[i]*(3*x[i]**2+2*x[i]*x[i-1]+x[i-1]**2)+y[i-1]*(3*x[i-1]**2+2*x[i]*x[i-1]+x[i]**2)))
Ixy=-1/24*sum(listIxy)
print(f"Ixy= {Ixy:.2f}")

Xt=Sy/Ax
print(f"Xt= {Xt:.2f}")

Yt=Sx/Ax
print(f"Yt= {Yt:.2f}")

Ixt=Ix-Yt**2*Ax
print(f"Ixt= {Ixt:.2f}")

Iyt=Iy-Xt**2*Ax
print(f"Iyt= {Iyt:.2f}")

Ixyt=Ixy+Xt*Yt*Ax
print(f"Ixyt= {Ixyt:.2f}")









