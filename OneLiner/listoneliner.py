# 元リスト
l = [[1,2,3,4,5],[6,7,8,9,10]]

# 二重ループ
la = [x for y in l for x in y]
print(la)

# 二重ループ + if
lb = [x for y in l for x in y if x%2==0]
print(lb)

# 二重ループ + if + else
lc = [x if x%2==0 else 0 for y in l for x in y]
print(lc)

# FizzBuzzワンライナ-
fizzbuzz = ["FizzBuzz" if x%15==0 else "Fizz" if x%3==0 else "Buzz" if x%5==0 else x for x in range(1,100)]
print(fizzbuzz)
