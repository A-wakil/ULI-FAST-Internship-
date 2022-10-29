import numpy as np
import matplotlib.pyplot as plt
# v = a*t +vo (a = -9.8m/s)
x0 = 30
v0 = 6
# h represents the step value, v0 represents the initial velocity while x0 represents the inital position

#Function that returns the velocity at the given time
def v(time, h):
  if time == 0:
    return v0
  else :
    return -9.8*(h) + v(time-h,h)
#Function that returns the position at a given time    
def position(time,h):
  if time == 0:
    return x0
  else:
    return position(time-h,h) + h*v(time-h,h)

#function for the actual value of x, which is an inegration of v
def actual(t):
  return -4.9*t*t + v0*t + x0

domain1 = [i for i in range(0,4,1)]
print(domain1)
domain2 = [j/4 for j in range(0,13)]
print(domain2)
domain_a = np.linspace(0, 3, 100)

range1 = []
for domain in domain1:
  range1.append(position(domain,1))
range2 = []
for domain in domain2:
  range2.append(position(domain,0.25))
print(range1)
print(range2)
actual_range = actual(domain_a)

plt.figure(num = 1, dpi = 65)
plt.plot(domain1, range1, label = "Euler's X(t) : h=1")
plt.plot(domain2, range2, label = "Euler's X(t) : h=0.25")
plt.plot(domain_a, actual_range, label = "Analytical (Actual solution)")
plt.title("Euler's Function (Numerical method) in comparison with the analytical method (Intergration)")
plt.xlabel("time/sec")
plt.ylabel("position (distance)/m")
plt.legend()
plt.show()
    