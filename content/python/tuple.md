+++

image = ""
comments = false
share = true
menu= ""		# set "main" to add this content to the main menu
author = "Ti Ｗoo"

date =  "2017-07-19T17:03:14+08:00"
title =  "Tuple"
draft =  false
slug =  ""
tags = ["python",]
type = "posts"

+++


* 跟 List 很像，都是一系列的任意項目
* 但不可變，定義之後就無法添加、刪除、或更改裡面的項目 

既然如此，那 Tuple 就只有建立的方法啦

<!--more-->

---

### 建立空 Tuple
empty_tuple = ( )  

---

### 建立一個元素的 Tuple
one_marx = ‘one’,   
最後的 ',' 不能被省略  

---

### 建立多個元素的 Tuple
```
marx_tuple = ‘one’, ‘two’, ‘three’
marx_tuple >>> (‘one’, ‘two’, ‘three’)
```
print 出 Tuple 的時候，Python 會自動加上括號  
真正定義 Tuple 的是元素後的括號  

---

### Tuple unpacking (開箱)
把 Tuple 內的元素一次指派給多個變數  
```
marx_tuple = ‘one’, ‘two’, ‘three’
a, b, c = marx_tuple
a >>> ‘one’
b >>> ‘two’
c >>> ‘three’
```

---

### 使用 Tuple 轉換函式來把其他東西做成 Tuple
```
marx_list = [‘one’, ‘two’, ‘three’]
tuple( marx_list ) >>> (‘one’, ‘two’, ‘three’)
```

---

### 特殊用法：在陳述式中直接用 Tuple 來交換值 ( 因為是由 "," 來定義 Tuple )
```
a = ‘one’
b = ‘two’
a, b = b, a
a >>> ‘two’
b >>> ‘one’
```

---

### 既然 Tuple 跟 List 那麼接近，那為什麼不乾脆直接用 List 取代 Tuple 呢

* tuple 佔用空間比較少  
* tuple 不會不小心被我們破壞  
* 可將 tuple 當成 dict 的 key  
* 可將具名 tuple 當成簡化物件的替代品 (這個我還沒弄懂，應該之後會學到)  
* 函式引數是以 tuple 的形式傳入的 (這個 cool，在看了那麼多函式之後)  

---

### 參考資料：
Lubanovic, Bill. Introducing Python: modern computing in simple packages. " O'Reilly Media, Inc.", 2014.


