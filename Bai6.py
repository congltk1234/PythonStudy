# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 09:28:53 2020

@author: ADMIN
"""

import random
while True: #Xét điều kiện nhập
  n = int(input('Số lượng phần tử trong dãy:'))   #Nhập số lượng phần tử trong dãy
  list = [] #Tạo list rỗng
  if n == 0:
    print(list, 'Dãy không có phần tử nào. Không có giá trị lớn nhất.')
  elif n > 0:
    for i in range(n):
      list.append(random.random())   #Thêm phần tử vào list
    max = list[0]                    #Tạo biến phụ để so sánh
    for i in range(n):
      if max < list[i]:              #So sánh max với từng phần tử được thêm vào, nếu lớn hơn max thì gán giá trị phần tử đó cho max
        max = float(list[i])
    print(list) 
    print('Phần tử lớn nhất trong dãy trên là:' , max)
    #Tiếp tục vòng lặp nếu người dùng muốn nhập tiếp 
    option = input("-Bạn có muốn tiếp tục không?(y/n) ")
    if option == 'n': 
      break  
  print('-Vui lòng nhập số nguyên dương.')