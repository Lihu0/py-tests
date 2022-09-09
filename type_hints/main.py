# age = input("How old are you? (in years)")
age = '3'
print(f"Wow that's {age * 12} months")  # dosen't work

# nead pycharm
age: float = '9'
print(f"Wow that's {age * 12} months")

print('--------------------------')

age: float = float(input("How old are you? (in years): "))
print(f"Wow that's {int(age * 12)} months")


def plus_10(x):
    return x + 10


print(plus_10(10))
try:
    print(plus_10('20'))
except:
    print('20 string isn\'t invald')


def plus_10_2(x: float) -> float:
    return x + 10

print('---------------------------')
print(plus_10(10))
try:
    # nead pycharm
    print(plus_10('20'))
except:
    print('20 string isn\'t invald')
