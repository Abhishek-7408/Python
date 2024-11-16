x = 99
def fun():
    global x
    x = 88 
fun()
print(x)

# avoid this type of confusion 