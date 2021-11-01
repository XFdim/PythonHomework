filename = "fizzbuzz"

file_io_wrapper = open(filename, "r")

for line in file_io_wrapper:
    fizz, buzz, finish = line.split()
    fizz = int(fizz)
    buzz = int(buzz)
    finish = int(finish)
    print(line)
    for number in range(1, finish + 1):
        if number % fizz == 0 and number % buzz == 0:
            print("FB", end=" ")
        elif number % fizz == 0:
            print("F", end=" ")
        elif number % buzz == 0:
            print("B", end=" ")
        else:
            print(number, end=" ")
file_io_wrapper.close()

# input_filename = "fizzbuzz"
# open_filename = "output"
#
# with open(input_filename, "r") as input_io_warpper:
#     with open(output_filename, "w") as output_io_warpper:
#         for line in file_io_wrapper:
#             fizz, buzz, finish = line.split()
#             fizz = int(fizz)
#             buzz = int(buzz)
#             finish = int(finish)
#             print()
#             for number in range(1, finish + 1):
#                 if number % fizz == 0 and number % buzz == 0:
#                     print("FB", end=" ")
#                 elif number % fizz == 0:
#                     print("F", end=" ")
#                 elif number % buzz == 0:
#                     print("B", end=" ")
#                 else:
#                     print(number, end=" ")