N = int(input())
# Считываем в очередь первые 6 чисел
Q = [int(input()) for i in range (6)] #создали очередь
min_even = 1001
beta = 1000001
pos = 0 # вводим позицию числа в списке
for i in range (N-6):
    x = Q[pos%6]
    min_x = min(min_x, x) #проверяем на минимальность
    if x%2 == 0 and x < min_even: # проверяем на четность
        min_even = x
    x = int(input())  #считываем второе значение
    beta = min(beta, x*min_even)
    if x%2 == 0:
        beta = min(beta, x*min_x)


    Q[pos%6] = [x] # возвращаем х в ту же нулевую
        # позицию списка из 6 элементов
    pos += 1 #переходим к следующему элементу

