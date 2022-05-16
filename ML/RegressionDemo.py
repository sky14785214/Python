import numpy as np
import matplotlib as plt

xdata = [ 338., 333., 328., 207., 226., 25., 179., 60., 208., 606.]
ydata = [ 640., 633., 619., 393., 428, 27., 193., 66., 226., 1591.]

x = np.arange(-200,-100,1) # bias
y = np.arange(-5,5,0.1) #weight
z = np.zeros((len(x),len(y)),dtype=object)
# Z = np.zeros((len(x),len(y)))
x, y = np.meshgrid(x,y)
for i in range(len(x)):
    for j in range(len(y)):
        b = x[i]
        w = y[i]
        z[j][i] = 0
        for n in range(len(xdata)):
            z[j][i] = z[j][i] + (ydata[n] - b - w*xdata[n])**2
            
        z[j][i] = z[j][i]/len(xdata)

b = -120
w = -4
lr = 0.0000001
iteration = 100000

b_history = [b]
w_history = [w]

for i  in range(iteration):

    b_grad = 0.0
    w_grad = 0.0
    for n  in range(len(xdata)):
        b_grad = b_grad - 2.0*(ydata[n] - b - w*xdata[n])*1.0
        w_grad = w_grad - 2.0*(ydata[n] - b - w*xdata[n])*xdata[n]

    b = b - lr * b_grad
    w = w - lr * w_grad
    
    b_history.append(b)
    w_history.append(w)
# plt.contourf(x,y,z, 50, alpha = 0.5),camp = plt.get_cmap('jet')


