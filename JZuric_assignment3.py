
n = int(input("Define number of points: "))

list_x = []
list_y = []

for i in range (0, n):

    x = float(input(f"{'define x'}{i+1} {'coordinate: '}"))
    y = float(input(f"{'define y'}{i+1} {'coordinate: '}"))

    list_x.append(x)
    list_y.append(y)
    

print(f"{'point'} {'|':2} {'x':5} {'|':2} {'y':5}")
for i in range(0, n):
    print(f"{i+1:5} {'|':2} {list_x[i]:5.2f} {'|':2} {list_y[i]:5.2f}")


#1. calculate Ax
sum = 0
for i in range(0, n-1):
    sum += (list_x[i+1] + list_x[i]) * (list_y[i+1] - list_y[i])
sum += (list_x[n-1] + list_x[0]) * (list_y[n-1] - list_y[0])

Ax = sum / 2

print(f"{'Ax: '} {Ax:.2f}")


#2. calculate Sx
sum = 0
for i in range(0, n-1):
    sum += (list_x[i+1] - list_x[i]) * (list_y[i+1]**2 + list_y[i]*list_y[i+1] + list_y[i]**2)
sum += (list_x[n-1] - list_x[0]) * (list_y[n-1]**2 + list_y[0]*list_y[n-1]+list_y[0]**2)

Sx =  sum / -6

print(f"{'Sx: '} {Sx:.2f}")

#3. calculate Sy
sum = 0
for i in range(0, n-1):
    sum += (list_y[i+1] - list_y[i]) * (list_x[i+1]**2 + list_x[i]*list_x[i+1]+list_x[i]**2)
sum += (list_y[n-1] - list_y[0]) * (list_x[n-1]**2 + list_x[0]*list_x[n-1]+list_x[0]**2)

Sy = sum / 6

print(f"{'Sy: '} {Sy:.2f}")


#4. calculate Ix
sum = 0
for i in range(0, n-1):
    sum += (list_x[i+1] - list_x[i]) * (list_y[i+1]**3 + list_y[i+1]**2 * list_y[i] + list_y[i+1] * list_y[i]**2 + list_y[i]**3)
sum += (list_x[n-1] - list_x[0]) * (list_y[n-1]**3 + list_y[n-1]**2 * list_y[0] + list_y[n-1] * list_y[0]**2 + list_y[0]**3)
Ix = sum / -12

print(f"{'Ix: '} {Ix:.2f}")

#5. calculate Iy
sum = 0
for i in range(0, n-1):
    sum += (list_y[i+1] - list_y[i]) * (list_x[i+1]**3 + list_x[i+1]**2 * list_x[i] + list_x[i+1] * list_x[i]**2 + list_x[i]**3)
sum += (list_y[n-1] - list_y[0]) * (list_x[n-1]**3 + list_x[n-1]**2 * list_x[0] + list_x[n-1] * list_x[0]**2 + list_x[0]**3)
Iy = sum / 12

print(f"{'Iy: '} {Iy:.2f}")


#6. calculate Ixy
sum = 0
for i in range(0, n-1):
    sum += (list_y[i+1] - list_y[i]) * (list_y[i+1] * (3*list_x[i+1]**2 + 2*list_x[i+1] * list_x[i] + list_x[i]**2) + list_y[i] * (3*list_x[i]**2 + 2*list_x[i+1] * list_x[i] + list_x[i+1]**2))
sum += (list_y[n-1] - list_y[0]) * (list_y[n-1]*(3*list_x[n-1]**2 + 2*list_x[n-1] * list_x[0] + list_x[0]**2) + list_y[0] * (3*list_x[0]**2 + 2*list_x[n-1]*list_x[0] + list_x[n-1]**2))
Ixy = sum / -24

print(f"{'Ixy: '} {Ixy:.2f}")

#7. calculate Xt

Xt = Sy / Ax

print(f"{'Xt: '} {Xt:.2f}")

#8. calculate Yt

Yt = Sx / Ax

print(f"{'Yt: '} {Yt:.2f}")


#9. calculate Itx

Itx = Ix - Yt**2*Ax

print(f"{'Itx: '} {Itx:.2f}")


#10. calculate Ity

Ity = Iy - Xt**2*Ax

print(f"{'Ity: '} {Ity:.2f}")


#11. calculate Itxy

Itxy = Ixy + Xt*Yt*Ax

print(f"{'Itxy: '} {Itxy:.2f}")
