#Câu 12: Hàm oscillate
'''
'''
def oscillate(start, count):
    result = []
    x = start
    for i in range(count):
        result.append(x)
        result.append(-x)
        x += 1 if x < 0 else 0
    return result[:count*3]

# Cách khác ngắn gọn hơn (đúng yêu cầu đề)
def oscillate(a, b):
    lst = []
    for i in range(a, b):
        lst.append(i)
        lst.append(-i)
    lst.append(-b)
    return lst

#Kiểm Tra
for n in oscillate(-3, 5):
    print(n, end=' ')
