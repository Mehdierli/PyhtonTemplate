# -*- coding: utf-8 -*-

"""
The pickle module:
    It translates almost any type of object into a string 
suitable for storage in a database, 
and then translates strings back into objects.

pickle.dumps:   
    takes an object as a parameter and returns a string representation (dumps is
short for “dump string”)
    
pickle.loads (“load string”):
    reconstitutes the object
"""
import pickle

t = [1,2,3]
print(pickle.dumps(t))

t1 = [1,2,3]
s = pickle.dumps(t1)
print(s)
t2 = pickle.loads(s)
print(t2)

i1 = pickle.dumps("he.jpg")
i2 = pickle.loads(i1)