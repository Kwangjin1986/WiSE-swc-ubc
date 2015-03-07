
# coding: utf-8

# In[11]:

# writing a function in python

#defines that it is a function. Note that indent is important after you define your function
#converting temp from fahr to kelvin
def fahr_to_kelvin(temp):
    return (((temp - 32.0)*(5.0/9.0))+273.15) 
#note that you need the .0 on the 5 and 9 because python uses integer divsion. See below for testing on 'float' (numbers) versus integers


# In[20]:

print 'freezing point of water:', fahr_to_kelvin(32)
print 'boiling point of water:', fahr_to_kelvin(212)


# In[7]:

print"212-32:", 212-32


# In[8]:

print"180*(5/9):", 180*(5/9)


# In[9]:

5/9 # this is zero because python treats these as integers!


# In[10]:

5.0/9.0 #this works!


# In[14]:

print 'float(5)/0 is:', float(5)/9 #also works. Float makes python recognize as a number (float)


# In[15]:

5/9.0


# In[19]:

a = 5
b = 9
print 'a/b is:', a/b
print 'float(a)/b is:', float(a)/b


# In[21]:

# calling functions within other functions

def kelvin_to_celsius(temp):
    return (temp - 273.15)


# In[23]:

print "absolute zero in Celsius:", kelvin_to_celsius(0)


# In[30]:

# function for going fahr to celsius

def fahr_to_celsius(temp):
    temp_k = fahr_to_kelvin(temp)
    result = kelvin_to_celsius(temp_k)
    return(result)

print "freezing point of water in celsius:", fahr_to_celsius(32) # test


# In[41]:

fahr_to_celsius(5) #test 2


# In[46]:

# Exercies

#1. 
def fence(a,b):
    return (b + a + b)

print "wrapper + original + wrapper:", fence('original', 'wrapper')
print fence("*", "name")

#2. return the first and last element of a string

def outer(s):
    return s[0]+s[-1]

print outer('helium')


# In[2]:

import numpy as np


# In[3]:

#function for recentering data around a known value

def center(data, desired):
    return (data - data.mean()) + desired


# In[4]:

#test function by creating a small array of zeros
z = np.zeros((2,2))
print (center(z,3))


# In[5]:

z.mean()


# In[7]:

x = center(z,3)
print(x.mean())


# In[8]:

data = np.loadtxt(fname = 'inflammation-01.csv', delimiter = ',')

print center(data,0 )


# In[9]:

def center(data, desired):
    ''' Return a new array containing the original data centered around a desired value.'''
    return (data - data.mean())+ desired
#note that the ''' will allow you to annotate the function in a way that is returned when you use help()


# In[10]:

help(center)


# In[25]:

# Exercise

get_ipython().magic(u'matplotlib inline')
## prevents figures from being opened in another window and instead
#prints them in the ipython notebook. If you don't type this, a new window opens for each
#figure.

from matplotlib import pyplot as plt #matplotlib is a sublibrary

#
def analyze(filename):
    
    ''' function for plotting data in the form of patients versus inflammation. Note that file name must be in quotes'''
    data = np.loadtxt(fname = filename, delimiter = ',')
    
    plt.figure(figsize = (15, 15)) # also increased the size of the plots

    plt.subplot(4,1,1) #four row, one columns, first axis. where the program will put the figure
    plt.ylabel('average')
    plt.plot(data.mean(axis = 0))

    plt.subplot(4,1,2)#four row, one columns, second axis. where the program will put the figure
    plt.ylabel('max')
    plt.plot(data.max(axis = 0))

    plt.subplot(4,1,3)#four rows, one columns, third axis. where the program will put the figure
    plt.ylabel('min')
    plt.plot(data.min(axis = 0))

    # add st dev plot. St dev in numpy is std
    plt.subplot(4,1,4)#four rows, one columns, fourth axis. where the program will put the figure
    plt.ylabel('standard deviation')
    plt.plot(data.std(axis = 0))

    plt.tight_layout()

    return(plt.show())


# In[26]:

help(analyze)


# In[27]:

analyze('inflammation-09.csv')


# In[30]:

# for loops

def print_characters(element):
    print element[0]
    print element[1]
    print element[2]
    print element[3]
    
print_characters('lead')

#doing something this way is inefficient!
#this way is better as you don't need to know the number of elements and it will automatically go through all

def print_characters2(element):
    for char in element:
        print char

    


# In[32]:

print_characters2('jfjhdskjfhksdhfkhasdkfjhkdjshf')


# In[36]:

# for loop example number 2

length = 0
for letters in 'aeiou':
    length = length +1
    print length
    print letters
    
print "There are", length, 'fun'


# In[38]:

print len('aeiou') # function in python for looking at the length


# In[43]:

#challenge
#def expo(base, exp):
#    for test in exp:
        
      
        
#def rev(test):
#    for char in test:
#        new[char] = test[-char]
#        return new
#    print char

#ANSWER!

#Awesome answer to the loops challenge (Thanks, Vanessa)
def reverse(string):
    rs=''
    n=0
    for b in string:
        rs=rs+string[len(string)-1-n]
        n=n+1
        
    print rs
    
reverse('Vanessa')    


# In[44]:

print rev("newton")


# In[45]:

a = 'test' 
   


# In[46]:

b = a[-1]


# In[47]:

b


# In[52]:

b =a[-1]
c =a[-2]
d =a[-3]
e =a[-4]

new =[bcda]


# In[ ]:



