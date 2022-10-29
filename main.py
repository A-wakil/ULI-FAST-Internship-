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
def position(time, h):
  if time == 0:
    return x0
  else:
    return position(time-h,h) + h*v(time-h,h)
#print(position(2,0.5))
print(position(0,1))
print(position(1,1))
print(position(2,1))
print(position(3,1))
print()
print('******************************')
print()
print('*',position(0,0.25))
print('*',position(1,0.25))
print('*',position(2.0,0.25))
print('*',position(3.0,0.25))


#function for the actual value of x, which is an inegration of v
def actual(t):
  return -4.9*t*t + v0*t + x0
print('****************************')


for i in range(4):
  print(actual(i))
    