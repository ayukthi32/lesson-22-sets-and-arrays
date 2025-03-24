#activity3
import array as arr
array_num = arr.array( 'i' , [ 1 , 3 , 5 , 7 , 8 ])
print ("Original array : "+str(array_num))
print("The number of occurences of the number 3 in this above array:" +str(array_num.count(3)))
array_num.reverse()
print("Reverse dorder the item")
print(str(array_num))