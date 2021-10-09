#pakai venv base
import matplotlib.pyplot as plt
import numpy as np
import math

fig, ax = plt.subplots()
y = []
for i in range (0,30,2):
    ebno = 10**(i/10)
    pb = 15/64*math.erfc(np.sqrt(4/85*ebno))-225/2048*(math.erfc(np.sqrt(4/85*ebno))**2)
    y.append(pb)

ax.semilogy(range(0,30,2),y, 'o-')
ax.axis([0,30,0.99e-10,1])
ax.set(xlabel='Eb/No (dB)', ylabel='Bit error rate (BER)',
    title='QAM 256 (Trade Off)')
ax.grid()

plt.show()
    
