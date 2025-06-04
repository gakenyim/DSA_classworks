###used to make single-line comments
"""
Used to make
multiple-line
comments
"""
# str
# int
# float
# bool
# bytes
# tuples
#mutable data types and immutable data types
name="Michelle"
age="20"
exam_mark="89.1"
its_sunny= False
x=(3,2,1)
list_names=["Michelle","Angella"]
nums=[30,78,90,1,5,67]
print(x)
print(name)
print(age)
print(nums)

def get_largest(numbers,n):
    numbers.sort()

    return numbers[-n:]
sorted_list=get_largest(nums,6)
print(sorted_list)


#list
for x in range(10):
    print(x)
    colours=["Red","Blue","Black","Grey"]
    for c in colours:
        print(c)
        if c == "Grey":
            break

        for i in range(2,10):
            print(i)