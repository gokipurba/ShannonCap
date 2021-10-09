import matplotlib.pyplot as plt
import numpy as np
import math

y = []

for i in np.arange(20, 26,0.5):
    ebno = 10**(i/10)
    pb = 15/64*math.erfc(np.sqrt(4/85*ebno))-225/2048*(math.erfc(np.sqrt(4/85*ebno))**2)
    y.append(pb)

fig, ax = plt.subplots()
ax.semilogy(np.arange(20, 26,0.5),y, 'o-')
ax.axis([20,26,0.99e-10,1])
ax.set(xlabel='Eb/No (dB)', ylabel='Bit error rate (BER)',
    title='QAM 256 (Trade Off)')
ax.grid()

plt.show()
    
