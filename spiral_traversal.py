# Cyclically rotate an array by one 

# Given an array, rotate the array by one position in clock-wise direction.

array = [ 9, 8, 7, 6, 4, 2, 1, 3 ]
temp =  array [ -1 ] 
array.pop ( len(array)-1 )
array.insert ( 0 , temp )
print ( array )