def my_range(first=0, last=10, step=1):
    num = first
    while num < last:
        yield num
        num += step
