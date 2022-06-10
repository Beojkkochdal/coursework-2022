import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def F(s,t):
    p1, p2, p3, p4, p5, p6 = 400, 20, 40, 30, 10, 10
    Gb = 400;                                               "s0-dg   s1-dx   s2-di   s3-dt"
    Ib = 150
    dgdt = p1 * (s[0] - Gb)  + 10; "- p3*(s[1] - Ib) * s[0]"
    #dxdt = -p2*s[1] +p3*(s[2] - Ib)
    didt = (p4*(s[0] - p5)) - p6*(s[1] - Ib)
    #D = 0
    #U = 0
    return [dgdt, didt]
t = np.linspace(0,86400)
s0=[5,15]
s = odeint(F,s0,t)
plt.plot(t,s[:,0],'r--', linewidth=2.0,label="g(t)")
plt.plot(t,s[:,1],'b--', linewidth=2.0,label="i(t)")
#plt.plot(t,s[:,2],'g-', linewidth=2.0,label="x(t)")
plt.xlabel("t")
plt.ylabel("g(t), i(t)")
plt.legend()
plt.grid()
plt.show()