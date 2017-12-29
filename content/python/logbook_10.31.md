+++

image = ""
comments = false
share = true
menu= ""		# set "main" to add this content to the main menu
author = "Ti Ｗoo"

date =  "2017-10-31T17:17:47+08:00"
title =  "10/31 - list 的不良值、Data Structure (Set、module)"
draft =  false
slug =  ""
tags = ["python", "Udemy"]
type = "posts"

+++



<!--more-->

#### (1) list 沒辦法使用不良位移值來 slice，跟 string 不同

查一下 lambda 怎麼運作的

---

#### (2)  Set 這個 data structure 基本上就是拿掉 value 的 dictionary
 (只剩下 Key 的意思，因為在 set 裡的東西需要獨一無二跟 Key 一樣)  
可以利用 set(  ) 把其他類型轉換成 set  
也可以利用 my_set.add (arg) 把東西加入已存在的 set 裡面 (在這例子中是加到 my_set 裡面)  

---

##### set 有幾種應用的 function：聯集、交集、互斥或是差集
聯集：print (my_set | my_set1)  
交集：print (my_set & my_set1)  
差集：print (my_set - my_set1)  
互斥：print (my_set ^ my_set1)  

聯集：set.union (self, other)  
交集：set.intersection (self, other)  
差集：set.difference (self, other)  
互斥：set.symmetric_difference (self, other)  

---

#### (3) Module & Package
- import 檔案進來，檔案需要跟現在要執行的檔案在同一位置 (資料夾)  
- 能夠直接 import 之後，使用該檔案的 module，使用方法：file.module (arg)  
- 也能夠單獨 import 一個 module 進來使用：  
```
        from outsideFile import knownModule：  
        knownModule (arg)  
```
- import file 之後，使用 dir( ) 會列出該檔案裡有的 module  
- 也可以把 import 進來的 file 或是 module 另外給定變數 (命名)  
例如：  
```
import file as f  
from file import module as m
```

---

#### 模組搜尋路徑
python 尋找要匯入的檔案時，會按照順序，並使用第一個找到的對象  
```
>>> for place in sys.path:
...     print(place)
...

/Library/Frameworks/Python.framework/Versions/3.5/lib/python35.zip
/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5
/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/plat-darwin
/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/lib-dynload
/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages
```
一開始的那行是空字串 ‘ ‘  ，代表當前的目錄

---

#### 參考資料：
- https://www.udemy.com/learn-python-3-from-beginner-to-advanced/
