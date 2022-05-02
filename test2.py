"""
com1 == random.randint(1,9)
com2 == ramdom.randint(1,9)
com3 == random.randint(1,9)
while(com1 != com2 | com2 != com3 | com1 != com3):
    if ( com1 == com2):
        com1 = random.randint(1,9)
    if ( com1 == com3):
        com1 = random.randint(1,9)
    if ( com2 == com3):
        com2 = random.randint(1,9)
    if(com1 != com2 and com1 != com3 and com2 != com3):
        break

print(com1,com2,com3)
cnt = 1

while(True):
    str = 0
    bal = 0
    usr = int(input("첫번째 수:"))
    usr = int(input("두번째 수:"))
    usr = int(input("세번째 수:"))

    if ( com1 == usr1 and com2 == usr2 and com3 == usr3):
        print("정답입니다.%d번만에 맞추셨어요"%cnt)
        break
    if ( com1 == usr1):
        str += 1
    if ( com2 == usr2):
        str += 1
    if ( com3 == usr3):
        str += 1

    if ( com1 == usr2):
        bal += 1
    if ( com1 == usr3):
        bal += 1
    if ( com2 == usr3):
        bal += 1
    if ( com2 == usr1):
        bal += 1
    if ( com3 == usr1):
        bal += 1
    if ( com3 == usr2):
        bal += 1

    cnt += 1

    print("스트라이크:%d 볼: %d"%(str,ball))
    """
"""
fruits = ["사과","오렌지","딸기","포도","감","키위","멜론","수박"]
list1 = [5,10,2,"탁구,",True,[4,5,6]]
numbers = list(range(1,10,2))

print(fruits)
print(list1)
print(numbers)
  """
"""
a = ["red","green","blue"]
a.append("yellow")
print(a)

a.insert(1,"black")
print(a)

b = ["purple","white"]
a.extend(b)
print(a)

c=a+b
print(c)
    """
"""
a = [10,20,30,40,50,60,70,80,90,100]

x = a.index(30)
print(x)

a.pop(x)
print(a)

a.remove(90)
print(a)

a.clear()
print(a)
"""
"""
list1 = ["a","bb","c","d","aaa","c","ddd","aaa","b","cc","d","aaa",]
length = list1.count("aaa")

print(length)
"""
"""
list2 = [-7,1,5,8,3,9,11,13]
list2.sort()
print(list2)

list2.sort(reverse=True)
print(list2)
"""
"""
color = ["red","green","blue","black","white"]

print(color[0])
print(color[-4])
print(color[1:4])
"""
"""
num = list(range(1,20,2))
print(num)
"""
"""
person1 = ["kim",24,"kim@naver.com"]
person2 = ["lee",35,"lee@hanmail.net"]

person = person1.extend(person2)
print(person1)
"""
"""
scores = [88,75,90,95,77,69,80,92]

sum = 0
for score in scores:
    sum += score

avg = sum/8
print("총점:%d,평균:%.2f"%(sum,avg))
"""
"""
animals = ["토끼","거북이","사자","호랑이"]

i = 0
while i < len(animals):
    print(animals[i])

    i+=1
"""
"""
s = [64,89,100,85,77,58,79,67,96,87,87,36,82,98,84,76,63,69,53,22]
count_su =0
count_wu =0
count_mi =0
count_yang =0
count_ga =0
i = 0
while i<len(s):
    if s[i]>=90 and s[i]<=100:
        count_su = count_su + 1
    if s[i]>=80 and s[i]<=89:
        count_wu = count_wu + 1
    if s[i]>=70 and s[i]<=79:
        count_mi = count_mi + 1
    if s[i]>=60 and s[i]<=69:
        count_yang = count_yang + 1
    if s[i]>=0 and s[i]<=59:
        count_ga = count_ga + 1
    i=i+1
print("수:%d명"%count_su)
print("우:%d명"%count_wu)
print("미:%d명"%count_mi)
print("양:%d명"%count_yang)
print("가:%d명"%count_ga)
"""

questions = ["tr_in","b_s","_axi","air_lane"]
answers = ["a","u","t","p"]
for i in range(len(questions)):
    q = "%s 에서 밑줄(_) 안에 들어갈 알파벳은?"%questions[i]
    ans = input("%s 에서 밑줄(_) 안에 들어갈 알파벳은?"%questions[i])
    if ans == anwsers[i]:
        print("정답입니다!")
    else:
        print("틀렸습니다!")
