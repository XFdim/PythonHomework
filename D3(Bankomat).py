# n = int(input('Vvedite summu '))
# cupur = [1000, 500, 200, 100, 50, 20]
# summ = 0
# index = 0
# count = 0
# while index < len(cupur):
#     while (summ + cupur[index]) <= n:
#         summ += cupur[index]
#         count += 1
#     index += 1
#
# print("Poluchite", count, "kupyuri")

denominal = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
amount = 2187

bills = list()
for denomination in denominal:
    denominal_count = amount // denomination
    if not denominal_count:
        continue

    bills.append((denomination, denominal_count))
    amount %= denomination

for denomination, denominal_count in bills:
    print(denomination, "x", denominal_count)