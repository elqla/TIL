```python
from itertools import combinations, permutations

print(list(permutations(range(5),3)))
print(list(combinations(range(5),3)))
```

```python
# 순열
from itertools import permutations
for i in permutations([1,2,3], 3):
    print(i, end=" ")

print()


# 조합
from itertools import combinations

for i in combinations([1,2,3,4], 2):
    print(i, end=" ")
print()



# 중복순열
from itertools import product
for i in product([1,2,3],'ab'):
    print(i, end=" ")
print()


for i in product([1,2,3], repeat=2):
    print(i, end=" ")
print()



# 중복 조합
from itertools import combinations_with_replacement

for cwr in combinations_with_replacement([1,2,3], 3):  #10개
    print(cwr, end=" ")


# 출처: https://juhee-maeng.tistory.com/91 [simPLE]
```