

def even_sum_1(arr:list):
    return sum([i for i in arr if i % 2 == 0])

def even_sum(arr:list):
    total = 0
    for num in arr:
        if num%2 == 0:
            total += num 
        
    return total

print(even_sum_1([1,2,3,4,5,6]))
print(even_sum([1,2,3,4,5,6]))

