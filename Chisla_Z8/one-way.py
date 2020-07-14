N = 4
m1_found = False
for i in range (N):
    x = int(input())
    if (not m1_found or x > m1):
        """если написать if (x > m1 or not m1_found),
        то будет ошибка"""
        m1 = x
        m1_found = True
print(m1)
