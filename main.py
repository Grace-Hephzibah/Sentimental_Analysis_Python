postive = ['happy' , 'good', 'terrific']
negative = ['sad' , 'depressed', 'angry']

data = input()
p = 0
n = 0

for i in postive:
    if i in data:
      p+= 1

for j in negative:
    if j in data:
      n-= 1

if(p+n>0):
  print("Positive Statement")
elif(p+n<0):
  print("Negative Statement")
elif(p+n==0):
  print("Neutral Statement")