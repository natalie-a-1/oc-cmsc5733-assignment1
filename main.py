import numpy


def sum_list(numbers):
    return sum(numbers)


def product_list(numbers):
    return numpy.product(numbers)


def main():
    numbers = []
    n = int(input("Enter the list size: "))
    for i in range(0, n):
        numbers.append(int(input("Enter number at index " + str(i) + ": ")))
    print("The sum is " + str(sum_list(numbers)) + ".")
    print("The product is " + str(product_list(numbers)) + ".")


if __name__ == '__main__':
    main()
