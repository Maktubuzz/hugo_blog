+++

image = ""
comments = false
share = true
menu= ""		# set "main" to add this content to the main menu
author = "Ti Ｗoo"

date =  "2017-10-29T17:09:04+08:00"
title =  "10/29 - list 的特殊用法、function 的執行"
draft =  false
slug =  ""
tags = ["python", "Udemy"]
type = "posts"

+++

<!--more-->

###  list 的特殊用法
```
list1 = [1,'abc', (2,3)]
list1[len(list1):] = [7]
print(list1)
```
這邊覺得奇妙的地方是他其實是在 list 的尾端加上 7  
因為我有先 `print` 過 `list1[len(list1):]` ，發現是一個空集合  

用法和 `append( )` 有點像，都是在 list 尾端加上東西  
只不過 `append` 用法是 `list1.append(7)`  
而用 `list1[最底位置:]` 要加入 7 需要再加上中括號  
也就是 `list1[len(list1):] = [7]`  

---

#### 為什麼啊？這個還要再查查

一般用位移值替換東西進 list 是直接 `list_name[位移值] = 7` 去替換東西 
 
---

#### 另外在測試 insert 的時候也發現一個很有趣的情形
```
print(list1.insert(len(list1),8))
print(list1)
```

第一個 print 會 print 不出東西，因為他要 print 的不是一個物件，而是一個 function 的執行過程  

---

#### 參考資料：
- https://www.udemy.com/learn-python-3-from-beginner-to-advanced/
