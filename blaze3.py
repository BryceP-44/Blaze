#blaze AI
#Bryce Patteson 10-7-2021

from mathmod import *
import matplotlib.pyplot as plt

#diverging dataset
x=[4,1,2,3,4,3,2,3,4,1,2,1,3,4,2]
y=[7,8,9,5,6,7,8,7,6,7,8,9,6,5,7]

x=[45,34,46,37,36,46,34,64,6,36,36,45,96]
y=[12,42,25,34,52,54,52,35,45,43,43,43,45]
z=[12,23,57,78,69,54,34,65,69,87,53,72,78]

x=[190,200,210,195,240,250,230,200,205,195,210,205,230,220,110,120,115,95,90,140,150,120,130,140,120,135,140,95] #weight
y=[2.2,2.1,2.5,2.0,2.1,2.3,2.6,2.0,1.8,1.7,2.0,2.8,1.7,1.1,3.8,3.7,3.4,4.0,3.9,3.5,3.8,3.9,3.9,3.7,3.9,3.4,3.7,3.5] #Gpa
z=[4,3,4,5,4,3,4,5,3,5,5,3,5,3,1,3,2,3,3,2,2,3,2,3,1,3,1,3] #meals per day

#skinny smart people who dont eat a lot versus the opposite

print(len(x))
print(len(y))
print(len(z))

#fig, (ax1, ax2,ax3) = plt.subplots(3,1)
fig = plt.figure()
ax1 = fig.add_subplot(211, projection='3d')
#ax2 = fig.add_subplot(312, projection='3d')
ax3 = fig.add_subplot(221, projection='3d')

ax1.plot3D(x,y,z,"*")
#ax2.plot3D(x,y,z,"*")

xnew=x
ynew=y
znew=z



""""""
""""""
for k in range(1000):
    for j in range(len(x)):
        D=[]
        for i in range(len(x)):
            D.append(((y[i]-y[j])**2+(x[i]-x[j])**2+(z[i]-z[j])**2)**.5)
        for i in range(len(D)):
            if D[i]==nzmin(D):
                xnew[j]=(x[j]+x[i])/2
                ynew[j]=(y[j]+y[i])/2
                znew[j]=(z[j]+z[i])/2
""""""
""""""



        
ax3.plot3D(xnew,ynew,znew,"*")

ax1.set_title('Raw Data')
#ax2.set_title('Movement')
ax3.set_title('Result')

"""
ax1.set_xlim([0, 100])
#ax2.set_xlim([0, 100])
ax3.set_xlim([0, 100])
ax1.set_ylim([0, 100])
#ax2.set_ylim([0, 100])
ax3.set_ylim([0, 100])"""

plt.show()


