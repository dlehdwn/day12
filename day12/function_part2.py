def add(x,y):
    return x+y
#가변 매개변수
def makepizza(*toppings):
    print("다음 피자는 아래의 토핑이 들어갑니다")
    for i in toppings:
        print(i)
makepizza("pineapple")
makepizza("pineapple","mushroom")

def zodiac(*years):
    sign = ['닭', '개', '돼지', '쥐']
    return [sign[i-1993] for i in years]
a = zodiac(1993,1994,1995)
print(a) # ['닭', '개', '돼지']




