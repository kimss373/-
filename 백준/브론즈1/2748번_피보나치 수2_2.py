dictionary = {0:0, 1:1}
n=int(input())
def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        dictionary[n] = fibonacci(n-1) + fibonacci(n-2)

        return dictionary[n]
print(fibonacci(n))