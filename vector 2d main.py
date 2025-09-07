from Vector import vector2D

v1=vector2D(6,8)
v2=vector2D(2,6)


print("Vector v1:", v1)  
print("Vector v2:", v2)


print("v1 + v2 =",v1+v2)         #addition of vector

print ("v1 - v2 =",v1-v2)        #subtraction of vector


print ("magnitude of v1 =",v1.magnitude())  #magnitude of v1

print ("direction of v1 =" ,v1.direction())  #degrees

print ("multiplication of v1 : v1 * 5 =" ,v1*5)    #vector ko 5 time bara karna          

print ("dot product v1 . v2 =" ,v1.__dot__(v2))    #dot product of v1 and v2


