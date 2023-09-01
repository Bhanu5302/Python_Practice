# -----list multiply& create new list for that
l1 = [1, 2, 3, 4, 5]
l2 = []
for i in l1:
    l2.append(i * 5)
print(l2)
# ---------------------------------------

# list comprehension for above
l3 = [value * 5 for value in l1]
print(l3)
# ---------------------------

# ------Even & odd list---------
even_list = [value for value in range(20) if value % 2 == 0]
odd_list = [value for value in range(20) if value % 2 != 0]
print(f"Even list: {even_list}")
print(f"Odd list: {odd_list}")
# ---------------------------
