#map(어떻게,무엇을) - 변경, 치환해주는 함수

nlist = [1,2,3,4,5]

a = map(lambda x:x**2,nlist)
print(list(a)) #[1, 4, 9, 16, 25]
b = map(lambda x:x+100,nlist)
print(list(b)) #[101, 102, 103, 104, 105]
c = map(lambda x:x**2+100,nlist)
print(list(c)) #[101, 104, 109, 116, 125]

coffeePriceList = [2000,3000,4000,5000]
d = map(lambda x: str(x+1000)+'원',coffeePriceList)
print(list(d)) #['3000원', '4000원', '5000원', '6000원']

fruits = ['apple','banana','mango']
e = map(lambda x:len(x),fruits)
print(list(e)) #[5, 6, 5]


#filter(어떻게, 무엇을) 컷/필터

numlist = [1,2,3,4,5,6,7,8,9,10]

f = filter(lambda x:x>5,numlist)
print(list(f)) #[6, 7, 8, 9, 10]
g = filter(lambda x:x%2==0,numlist)
print(list(g)) #[2, 4, 6, 8, 10]

fruits = ['apple','banana','mango','avocado']
h = filter(lambda x:'o'in x,fruits)
print(list(h)) #['mango', 'avocado']

i = filter(lambda x:len(x)>5,fruits)
j = map(lambda x:'🤣' + str(x),i)
print(list(j)) #['🤣banana', '🤣avocado']



