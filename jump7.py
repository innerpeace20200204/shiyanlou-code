start = 1
end = 100

for i in range(start, end + 1):
    if 0 == i % 7 or 7 == i % 10 or 7 == i // 10:
        continue
    else:
        print(i)
