import time
import sys

# time_start = time.time()
# i = 0
# while i < 1000000000:
#     # Do nothing
#     i += 1
#
# time_finish = time.time()
# time_span = time_finish - time_start
# print(time_span, 'seconds')


# def eratosthenes_effective(n):
#     numbers = list(range(n + 1))
#     numbers[0] = numbers[1] = False
#     for num in range(2, 3):
#         if numbers[num]:
#             for j in range(num * num, n + 1, num):
#                 numbers[j] = False
#     return numbers
#
#
# def get_least_primes_linear(n):
#     lp = [0] * (n + 1)
#     print(lp)
#     primes = []
#     for i in range(2, n + 1):
#         if lp[i] == 0:
#             lp[i] = i
#             primes.append(i)
#         for p in primes:
#             x = p * i
#             if (p > lp[i]) or (x > n):
#                 break
#             lp[x] = p
#     return primes, lp
#
#
# print(get_least_primes_linear(10))


print(sys.getsizeof(42))  # => 28 байт занимает короткое целое число
print(sys.getsizeof([]))  # => 56 байт занимает пустой массив
print(sys.getsizeof([42]))  # => 64 = (56 + 8) байт занимает массив с одним элементом.
print(sys.getsizeof([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # => 136 = (56 + 8*10) байт занимает массив
                               #          с десятью элементами.
                               # сами данные хранятся отдельно
                               # и добавляют 280 = (28 * 10) байт
