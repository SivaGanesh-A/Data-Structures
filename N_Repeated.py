nums = [1,2,3,3]
seen = set()
for i in nums:
    if i in seen:
        print(i)
    seen.add(i)