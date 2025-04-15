#acp
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result1 = set1 ^ set2
print("Symmetric Difference using ^", result1)
result2 = set1.symmetric_difference(set2)
print("Symmetric Difference using method :", result2)