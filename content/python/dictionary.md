+++

image = ""
comments = false
share = true
menu= ""		# set "main" to add this content to the main menu
author = "Ti Ｗoo"

date =  "2017-07-23T17:03:14+08:00"
title =  "Dictionary"
draft =  false
slug =  ""
tags = ["python",]
type = "posts"

+++

* 跟 list 很像，但不在乎順序，所以沒有使用位移值的方法
* 每個 value 都有獨一無二的 key
* key  可以是任何「類型」
    * 布林、整數、浮點數、tuple、string... etc.

dict 的使用方法也是 CRUD 和其他

<!--more-->

---

### Create
-  用 { } 來建立：用 { } 來包住以逗號分隔的 key:value


#### 用 { } 來建立
建立的方法：用 { } 來包住以逗號分隔的 key:value
```
empty_dict = { }
empty_dict >>> { }

dict_1 = {
... 'day':'Sunday',
... 'Place':'Movie theater'
… }

dict_1 >>> {'Place': 'Movie theater', 'day': 'Sunday’}
```

以逗號分隔這件事情很重要，不過 list、tuple、dict 都可以省略最後一個項目的逗號  
而其實 dict 也可以不用縮排來輸入，只是為了方便閱讀而已  


#### 用 dict( ) 來轉換

使用 dict( ) 函式，將雙值序列轉換到 dict 內  
第一個項目會被當成 key 第二個項目會被當成 value  

可以轉換的例子  
###### (1) list of list  
```
lol = [['a', 'b'], ['c', 'd'], ['e', 'f’]]
dict (lol) >>> {‘a’ : ‘b’ , ‘c’ : ‘d’ , ‘e’ : ‘f’ } 
```
不一定會照原始順序，因為 dict 本來就不是注重順序的資料結構

###### (2) list of tuple 
``` 
lot = [ (‘a’,’b’) , (‘c’ , ‘d’) , (‘e’ , ‘f’)]
dict (lot) >>> {‘c’:’d’ , ‘a’:’b’ , ‘e’:’f’}
```

###### (3) tuple of list
```
tol = ([‘a’,’b’] , [‘c’ , ‘d’] , [ ‘e’ , ‘f’ ])
dict (tol) >>> {'e': 'f', 'a': 'b', 'c': 'd'}
```

###### (4) list of string
```
los = ['ab','cd','ef']
dict(los) >>> {'e': 'f', 'a': 'b', 'c': 'd’}
```

###### (5) tuple of string
```
tos = (‘ab’,’cd’,’ef’)
dict(tos) >>>  {'e': 'f', 'a': 'b', 'c': 'd’}
```

###### 其實基本上就是幾個重點：
* 雙值項目：不論是 ‘ab’  、 (‘a’,’b’) 或是 [‘a’,’b’]
* 與其組成的序列：list 或是 tuple
  
接下來會學到用 zip( ) 迭代多個序列來製作這些雙項目序列  

---

### 參考資料：
Lubanovic, Bill. Introducing Python: modern computing in simple packages. " O'Reilly Media, Inc.", 2014.

