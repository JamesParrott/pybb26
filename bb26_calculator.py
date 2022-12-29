from bb26 import BB26_to_int, int_to_BB26

BB26_x = input('Enter first number in Bijective base 26: ')
BB26_y = input('Enter second number in Bijective base 26: ')

x = BB26_to_int(BB26_x)
y = BB26_to_int(BB26_y)

results = {'+' : x+y, 
           '-' : x-y,
           '*' : x*y,
           '//' : x // y, 
           '%' : x % y,
           '^' : x ** y
           }

print('\nResults in bijective base 26: ')
for op, result in results.items():
    print(f'{BB26_x} {op} {BB26_y} == {int_to_BB26(result)}')