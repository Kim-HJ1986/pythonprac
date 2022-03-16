#리스트
a_list = ['사과', '배', '감']

a_list.append('수박')

print(a_list)

#딕셔너리
a_dict = {
    'name': 'bob',
    'age': 28
}

print(a_dict['name'])

#함수
def sum(a, b):
    print('sum result:')
    return a+b

result = sum(1, 2)
print(result)

#조건문
# 콜론은 그 다음 내용이 자신의 내용물로 정의하는 것.
def is_adult(age):
    if age > 20:
        print('성인 입니다.')
    else:
        print('성인이 아닙니다.')

is_adult(25)

#반복문_리스트
fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

count = 0
for fruit in fruits:
    if fruit == '배':
        count += 1

print(count)

#반복문_딕셔너리
people = [{'name': 'bob', 'age': 20},
{'name': 'carry', 'age': 38},
{'name': 'john', 'age': 7},
{'name': 'smith', 'age': 17},
{'name': 'ben', 'age': 27}]

for person in people:
    if person['age'] > 20:
        print(person)