N = int(input())
s = 0
delta_min = bad_delta
for i in range(N):
    x, y = [int(word) for word in input().split()]
    s +=min(x, y)
    if abs(x-y)%k != 0 and < delta_min:
        delta_min = abs(x-y)
if s%k != 0:
    print(s)
elif  delta_min != bad_delta:
    print(s + delta_min)
else:
    print(0)

