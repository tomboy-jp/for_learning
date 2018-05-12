# 元リスト
l = [[1,2,3,4,5],[6,7,8,9,10]]

# 二重ループ
print([x for y in l for x in y])

# 二重ループ + if
print([x for y in l for x in y if x%2==0])

# 二重ループ + if + else
print([x if x%2==0 else 0 for y in l for x in y])

# FizzBuzzワンライナ-
print(["FizzBuzz" if x%15==0 else "Fizz" if x%3==0 else "Buzz" if x%5==0 else x for x in range(1,100)])

# execワンライナー
exec("def test(n):\n\tfor x in range(n):\n\t\tprint(x)"); t = test(100);
