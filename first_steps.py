# Exercise 1
# Answers to questions that ask for non-code answers can simply be added as comments.

# 1) The following line causes a SyntaxError. Please correct the line so that it's output is 'Hallo Welt!' [1P]
print('Hallo Welt!')
#%%
# 2) Calculate the difference between a and b and assign the result to a variable called 'v_1'. What are the datatypes of a, b and 'v_1'? [2P]
a = 976.543
b = 345
v_1 = a-b
print(v_1)
#631.543

for i in [a,b,v_1]:
    print(type(i))

#<class 'float'>
#<class 'int'>
#<class 'float'>

#%%

# 3) Calculate the remainder of the division 100/17 by only using one operator and save the result in v_2 (look into the Python docs for help) [1P]
v_2 = 100%17
#15
#%%
# 4) The speed of light is about 300'000 km/s. Calculate the wavelength (in nanometers) of a light wave with a frequency of 5.0E+14 per second. Can we see this light? [4P]
#    Save the result in v_3.
#h=c/f
v_3 = 300000/5.0E+14
#v_3 in [km]
v_3 = v_3 * 1E12
#600nm, ja
# #c94000 "Diese Farbe hat eine ungefähre Wellenlänge von 600 nm"
# https://encycolorpedia.de/c94000

import matplotlib
import matplotlib.pyplot as plt
        
fig = plt.figure()
ax = fig.add_subplot(111)
rect1 = matplotlib.patches.Rectangle((-200,-100), 400, 200, color=('#c94000'))
ax.add_patch(rect1)
plt.xlim([-250, 250])
plt.ylim([-200, 200])
plt.show()
#%%
# 5) Print the following string to the console using the format-function and the variables 'n' and 'pi': "Pi rounded to the first 10 decimals is: 3.1415926536" [2P]
n  = 10
pi = 3.14159265358979323846264338
print("Pi rounded to the first {0} decimals is: {1}".format(n,round(pi,n)))

#%%
# ------------------------------------
# - Don't change stuff below this line
# ------------------------------------

print(v_1)
print(v_2)
print(v_3)
