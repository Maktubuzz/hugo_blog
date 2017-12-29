+++

image = ""
comments = false
share = true
menu= ""		# set "main" to add this content to the main menu
author = "Ti Ｗoo"

date =  "2017-11-09T17:17:49+08:00"
title =  "11/09 - Numpy 語法"
draft =  false
slug =  ""
tags = ["python", "Udemy", "Numpy"]
type = "posts"

+++

```
import numpy as np  
a4 = np.arange(10,50,10)  
```

第一個 10 是起始值，第二個值 50 是終止值 (不包含這個數)，第三個值 10 是間距  
所以要是 print(a4) 的話會是一個 list  >>> [10, 20, 30, 40]   

<!--more-->

---
```
a8 = np.linspace(3, 8, 9)  
```
第一個 3 是起始值，第二個值 8 是終止值，第三個值 9 是步數  
所以他會在 3 - 8 計算出 9 個等距的點 (包含 3 和 8)  

---
```
o1 = np.ones((2,2,2))  
```
用 1 創造一個 2 X 2 的矩陣，並且創造兩個 (第三個值)  

---
```
o2 = np.zeros ((2,2,2))  
```
用 0 創造一個 2 X 2 的矩陣，並且創造兩個 (第三個值)  

---
```
e1 = np.empty((3,4))  
```
不帶任何值的創造一個 3 X 4 的矩陣  
print (e1) 的話會回吐一堆不明的數字  

---
```
e2 = np.eye(3)  
```
創造一個 3 X 3 的矩陣，並且創造一個 Diagonal matrix  

---
```
r1 = np.random.random((5,5))  
```
創造一個值介於 0.0 到 1.0 之間的 5 X 5 矩陣  

---
```
np.random.random( )  
```
會產出一個介於 0.0 到 1.0 之間的 floating point number  

---

random.something( ) 的用法可參考：  https://docs.python.org/3/library/random.html  

---

##### 參考資料：
- https://www.udemy.com/learn-python-3-from-beginner-to-advanced/
