import numpy as np
import matplotlib.pyplot as plt

def function_to_integrate(x):
    return x**2 #the test

def analytic_integral_of_f(a=None, b=None, h=None):
    return [a:b+h] #this is to show the bounds

def trapezoidal_rule(f, a=None, b=None, n=None):
    points = np.linspace(a, b, n)
    h = points[1]-points[0]
    integral_approx = 0 
    for points in points:
        integral_approx += ((f(point)+f(point+h)) * (h/2))
    return integral_approx

def lefthand_riemann(f, a=None, b=None, n=None):
    #generate linear set of n points starting at a, ending at b
    points = np.linspace(a,b,n)
    h = points[1]-points[0]
    chunks = generate_lefthand_chunks(points)
    integral_approx = 0
    for point in points:
        integral_approx += f(point)*h
    return integral_approx

def simpson_rule(f, a=None, b=None, n=None):
    points = np.linspace(a, b, n)
    h = points[1]-points[0]
    chunks = generate_simpson_chunks(points)
    integral_approx = 0
    for chunk in chunks:
        if len(chunks) == 3:
            prefactor = h/3
            factor = f(chunk[0]) + 4*f(chunk[1]) + f(chunk[2])
            integral_approx += factor*prefactor
        else:
            assert len(chunk)==2
            b1 = f(chunk[0])
            b2 = f(chunk[1])
            area = 0.5*(b1+b2)*h
            integral_approx += area
    return integral_approx

def relative_error(true=None, estimate=None):
    return np.abs((true-estimate)/np.abs(true))*100

def sizing_error(f, a, b, n):
    data = []
    xs = [10,100,1000,10000]
    for x in xs:
        number_of_steps = x
        y = f(function_to_integrate, a=a, b=b, n=x)
        rows = (x, y)
        data.append(rows)
    return np.array(data) #scale for the graph
 
if __name__ == "__main__":
    a = 0
    b = 1  
    n = 10
    print("Lefthand riemann approx to f, between",a,b," steps=",n)
    print(lefthand_riemann(function_to_integrate, a=a, b=b, n=x))

#lets graph it out now
plt.plot(trapezoidal_rule)
plt.plot(lefthand_riemann)
plt.plot(simpson_rule)
plt.xlim(0,10000)
plt.ylim(0,0.5)
plt.legend()
plt.title('Riemann Sums')
plt.xscale-('log')
plt.xlabel('steps')
plt.ylabel('error')
plt.show()