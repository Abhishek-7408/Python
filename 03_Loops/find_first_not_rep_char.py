input_str = "teeterddfgkgj"

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("result is:",char)
        # break