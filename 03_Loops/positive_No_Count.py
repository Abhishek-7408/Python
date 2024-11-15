number = [1,2,-5,99,-66,-8,22,-7,22,88,99,-6,-2,-22,-88,100]

positive_Number_count = 0
for num in number:
    if num > 0:
        positive_Number_count+=1
print("Final count of positiuve number is ",positive_Number_count)