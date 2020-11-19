import math
list = [0 , -5 , 60.5 , 1]
print('Giá trị của phần tử và logarit tương ứng:')
for i in range(len(list)):
  a = float(list[i])
  if a <= 0:                #Kiểm tra điều kiện để tính logarith
    print(a , ', Không có logarit tương ứng.')
  else:
    print(a , ', logarit của' , a , ':' , math.log(a))