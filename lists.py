sample= ['apple',5,False,"first",True]

print(sample)
print(sample[0]) # irst
print(sample[-1]) # last
print(sample[1:])# 2nd to last
print(sample[1:2])# 2nd to 3rd

sample[1]="banana"

print(sample)

sample.extend(["cherry", 6])
sample.append("dragonfruit")
sample.insert(0,"blueberry")
sample.remove("first")
print(sample)
sample.pop()
print(sample)
# print(sample.sort()) only available for same data types 
print(sample.count("banana"))
print(sample.index("banana"))
print(sample.reverse())
sample2=sample.copy()
print(sample2)
sample.clear()
print(sample)
