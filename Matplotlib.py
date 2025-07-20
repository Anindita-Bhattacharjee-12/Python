import matplotlib.pyplot as plt
#x=[1,2,3,4,5,6,7]
#y=[45,56,78,34,23,12,10]
#plt.xlabel('Day')
#plt.ylabel('Temperature')
#plt.title('Weather')
#plt.plot(x,y)
#plt.plot(x,y, color='green',linewidth=10,linestyle='dotted')
#plt.plot(x,y,'b+--')
#plt.plot(x,y,color='blue',marker='+',linestyle='',markersize=20)
#plt.plot(x,y,'r<',alpha=1.0)
#plt.show()

import numpy as np
#x=np.arange(-10,10,0.1)
#y1=np.sin(x)
#y2=np.cos(x)
#plt.figure()
#plt.plot(x,y1)
#plt.plot(x,y2)
#plt.legend(['sine','cosine'])
#plt.show()
#plt.figure(figsize=(10,5))
#plt.subplot(1,2,1)
#plt.plot(x,y1)
#plt.legend(['sine'])
#plt.subplot(1,2,2)
#plt.plot(x,y2)
#plt.legend(['cosine'])
#plt.savefig('test.pdf',transparent=True)
#plt.show()


from IPython import display
sin=[]
X=[]
plt.figure()
for i in range(-50,50,1):
    X.append(i)
    sin.append(np.sin(i))
    display.clear_output(wait=True)
    plt.plot(X,sin)
    plt.show()




