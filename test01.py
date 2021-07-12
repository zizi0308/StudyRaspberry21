n = 1
name = 'Jo'
n =  n + 2
value = 1.2 * n

print('{0} = 1.2 * {1}'.format(value, n))
print(name)

greeting = 'Hello World'
# print(greeting[0])    # H
# print(greeting[2:5])  # llo
# print(greeting[:2])     # l
# print(greeting[-2:])    # ld

numbers = [0, 1, 2, 3]
# print(numbers)
# print(numbers[2])
# print(numbers[2:3])
names = ['kim', 'jo', 'ha']
array = numbers + names
# print(array)
# print(array[-1])
# print(array*2)
array[3] = 7
# print(array)

#Tuple
person = ('Kim', 24, 'male')
print(person)
print(person[1])
# person[1] = 45    # 이미있는 값은 변경이 불가능(튜플의 특성)
name, age, gender = person
print(gender)