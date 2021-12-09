a = 10
print(f"a is {type(a)}")
b = 10.1
print(f"b is {type(b)}")
c = 3.14j
print(f"c is {type(c)}")

int_math = a * 2
float_math = a + b
complex_math = c + a

print(f"1st example result is {int_math} and it is {type(int_math)}")
print(f"2nd example result is {float_math} and it is {type(float_math)}")
print(f"3rd example result is {complex_math} and it is {type(complex_math)}")

# Difference between human math and "computer"
print(f"{1.1 + 2.2}")  # Result will be 3.3000000000000003 !


