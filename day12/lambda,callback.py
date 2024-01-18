#lambda
#간결하고 이름이 없는 한줄 함수
plus = lambda a,b: a+b
c = plus(5,6)
print(c)
mul = lambda a,b: a*b
min = lambda a,b: a-b

#callback 함수
#something(add)
#something(add(5,6)) == something(8)

def hello(some):
    print("안녕")
    some()

def bye():
    print("잘가")

hello(bye)

eggs = ['🥚','🥚','🥚']
def cookEggs(eggs,index,recipe):
    recipe(eggs,index)
def makefry(eggs,index):
    eggs[index] = '🍳'
def makesandwich(eggs,index):
    eggs[index] = '🥪'
cookEggs(eggs,0,makefry)
cookEggs(eggs,1,makesandwich)
print(eggs) # ['🍳', '🥪', '🥚']








