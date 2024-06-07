import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve
from scipy.optimize import minimize_scalar
from scipy.integrate import odeint


def first():
    def equation(x, N, beta):
        return np.tan(N * x) * np.tan(x / 2) - (1 + 2 * beta * N)**-1

    
    N_value = 25
    beta_value = 0.01
    def f1(x):
        return np.tan(N_value*x) * np.tan(beta_value/2)

    x_interval = np.linspace(0, np.pi, 100)

    roots = []

    for x0 in x_interval:
        root, infodict, flag, mesg = fsolve(equation, x0, args=(N_value, beta_value), full_output=True)

        if flag == 1 and np.allclose(equation(root, N_value, beta_value), 0):

            if not any(np.isclose(root, r) for r in roots):
                roots.append(root[0])

    print("all roots:", roots)

    plt.figure(figsize=(10, 6))
    plt.plot(x_interval, equation(x_interval, N_value, beta_value))
    plt.scatter(roots, equation(np.array(roots), N_value, beta_value), c='red')
    plt.plot(roots[10], f1(roots[10]), 'x')
    plt.title('grafic yravneniya and roots')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.show()


def two():
    N = 25
    betta = 0.01
    x = np.arange(0,1*np.pi,0.01)
    y1 = np.tan(N*x) * np.tan(x/2)
    y2 = x*0*(1+2*betta*N)**(-1)

    def f1(x):
        return np.tan(N*x) * np.tan(x/2)

    plt.plot(x,y1)
    plt.plot(x,y2)
    plt.plot(1.1626788232496978, f1(1.1626788232496978), 'x')
    plt.show()



def three(): 
    N = 25
    betta = 0.01
    def f1(N,x):
        return np.tan(N*x) * np.tan(x/2)
    def f2(betta, N, x):
        return x*0*(1+2*betta*N)**(-1)
    
    def f3(x):
        return f1(N,x) * f2(betta, N, x)

    result = minimize_scalar(f3, bounds=(N/2, N), method='bounded')

    print("min func f1*f2 on [N/2 N]:", result.x)

three()


def four():
    N = 25
    xk = 1.1626788232496978
    betta = 0.01
    x_0 = 2 * np.sin(xk/2)
    def model(x, t):
        return 2 * np.sin(x / 2) + t

    x0 = 2 * N * np.sin(xk / 2)

    t = np.linspace(0, 10, 100) 

    sol = odeint(model, x0, t)

    plt.plot(t, sol[:, 0], label='x(t)')
    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.title('Solution task Koshi')
    plt.grid()
    plt.show()

first()
two()
three()
four()