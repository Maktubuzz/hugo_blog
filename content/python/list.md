---
date: "2017-07-08T17:19:35+08:00"
title: "List"
draft: false
slug: ""
tags: ["python",]
type: posts
author: "Ti Ｗoo"
---

List in Python
<!--more-->

## 串列 (List)

- list 很適合用來追蹤東西的順序，特別是其順序跟內容很容易改變的時候  
- 跟 string 不同的是，list 是可變的  
- 在 list 中，同樣的值很可能出現不只一次  
- list 可容納各種類型的元素，包括其他的 list  

List 這邊會學到怎麼 CRUD 和其他  
(list 就是一種資料結構，使用 CRUD 並不奇怪)

---

心得：  
* 每個類別的函式不能共用 (但有通用函式庫)  
* list 可以 CRUD  
* list 可以搜尋值  
* list 可以排序  
    * 影響本身值的排序  
    * 建立複本的排序方式  

* 問題：  
為什麼用 sorted_marxes = sorted(marxes) 可以  
但 sorted_marxes = marxes.sorted( ) 不行   
而要用 marxes.sort( )  

解答：https://goo.gl/67WngK  
簡單來說：  
sorted( ) 方法能接受 list 當引數，而且有回傳值  
sort( ) 方法沒有回傳值，他是直接排序序列內容  
所以要用 sorted( list ) 並且命名給某個變數  
而 list_name.sort( ) 就行，因為它會直接改變原本的那個 list_name 的序列  

---

#### 重點摘要

###### 1. Create：
- 用[  ] 或 list( ) 來建立串列
- 用 list( ) 來將其它的資料類型轉換成 list
- 之前學的 split( ) 在分割之後會把資料儲存成 list

###### 2. Read：
- 用位移值來取值
- list 裡的 list
- 使用 slice 來取出一個範圍的 list

###### 3. Update：
- 用位移值來更改一個項目
- 用 append( ) 將項目附加到結尾
- 使用 extend( ) 或是 += 來結合串列
- 用 insert ( ) 與位移值來加入一個項目

###### 4. Delete
- 用 del 與位移值來刪除一個項目
- 用 remove( ) 與值來刪除項目
- 可以用 pop( ) 與位移值來取得一個項目，並且刪除它
 
###### 5. 其他：
- 用 index( ) 和值來尋找某個項目的位移值
- 用 in 來測試在 list 中，值是否存在
- 用 count( ) 來算出某個值的出現次數
- 用 join( ) 來轉換成字串
- 用 sort( ) 來排序項目
- 用 len( ) 來取得 list 長度
- 用 = 來指派 / 用 copy 來複製


---



## Create / 創建 或 新增
- 用[  ] 或 list( ) 來建立串列
- 用 list( ) 來將其它的資料類型轉換成 list
- 之前學的 split( ) 在分割之後會把資料儲存成 list

---

### 用[  ] 或 list( ) 來建立串列
* 用 [  ] 來建立串列 
    * empty_list = [  ]
        *   建立空字串
    * weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday']
* 用 list( ) 來建立串列
    * another_empty_list = list( )
    * list(‘cat’) >>> [‘c’, ‘a’, ’t’]

---

### 用 list( ) 來將其它的資料類型轉換成 list
*  list(‘cat’) >>> [‘c’,’a’,’t’ ]
* 將 tuple 轉換成 list
a_tuple = (‘a’,’b’,’c’)
list (a_tuple) = [‘a’,’b’,’c’]

---

### 之前學的 split( ) 在分割之後會把資料儲存成 list

* birthday = ‘1/6/1952’
birthday.split(‘/‘) = [‘1’, ’6’, ’1952’]

---

## Read / 取值
- 用位移值來取值
- list 裡的 list
- 使用 slice 來取出一個範圍的 list

---

### 用位移值來取值
marxes = [‘a’, ‘b’, ‘c’, ‘d’, ‘e’]
marxes[0] >>> ‘a’
marxes[4] >>> ‘e’
marxes[-3] >>> ‘c’

備註：
list 的位移值必須是有效的，在 string 裡可以有無效的位移值且會吐出對應資訊，但 list 裡不會

---

### list 裡的 list 元素
要取 list 中、某個 list 元素裡的某個值的時候 (超拗口)
使用兩個位移值來取

words = [‘a’, ‘b’, ‘c']
mix_words = [ ‘d’, ‘e’, words]
mix_words[2][2] >>> ‘b'

---

### 用一個範圍的位移值，以 slice 取出項目

slice 在字串中是可以直接擷取一段字串
以 [開始：結束：間隔] 的方式來做
同樣也可以應用在 list 上

marxes = [‘a’, ‘b’, ‘c’, ‘d’]
marxes[0 : 2]  >>> [‘a’, ‘b’]

---

## Update / 修改
- 用位移值來更改一個項目
- 用 append( ) 將項目附加到結尾
- 使用 extend( ) 或是 += 來結合串列
- 用 insert ( ) 與位移值來加入一個項目

---

### 用位移值來更改一個項目
直接指定就行

marxes = [‘a’, ‘b’, ‘c’, ‘d’]
marxes[1] = ‘1’
marxes >>> [‘a’, ‘1’, ‘c’, ‘d’]

---

### 用 append( ) 將項目附加到結尾

marxes = [‘a’, ‘b’, ‘c’, ‘d’]
marxes.append(‘e’)
marxes >>> [‘a’, ‘b’, ‘c’, ‘d’, ‘e']

---

### 使用 extend( ) 或是 += 來結合串列

marxes = [‘a’, ‘b’, ‘c’, ‘d’]
other = [1, 2, 3]

* marxes.extend(other)
marxes >>> [‘a’, ‘b’, ‘c’, ‘d’, 1, 2, 3] 
* marxes += other
marxes >>> [‘a’, ‘b’, ‘c’, ‘d’, 1, 2, 3] 
但此時 other 還是 [1, 2, 3] 喔，有改變的只有 marxes

備註：
上面的例子使用 append 的話，會把 other 當成一整個元素加入 marxes 中，而不是合併兩個 list 中的項目

marxes.append(other)
marxes >>> [‘a’, ‘b’, ‘c’, ‘d’, [1, 2, 3] ]

---

### 用 insert ( ) 與位移值來加入一個項目

insert(位移值, 加入的項目)

marxes = [‘a’, ‘b’, ‘c’, ‘d’]
marxes.insert(2, ‘o’ )
marxes >>> [‘a’, ‘b’, ’o’, ‘c’, ‘d’]
 
---

## Delete / 刪除
- 用 del 與位移值來刪除一個項目
- 用 remove( ) 與值來刪除項目
- 可以用 pop( ) 與位移值來取得一個項目，並且刪除它

---

### 用 del 與位移值來刪除一個項目
知道某個元素的位移值的時候可以直接刪除它

marxes = [‘a’, ‘b’, ‘c’, ‘d’]
del marxes[-2]
marxes >>> [‘a’, ‘b’, ‘d’]

---

### 用 remove( ) 與值來刪除項目
如果不確定某個項目的位置、但知道他的值的時候，可以用 remove( ) 來刪除

marxes = [‘a’, ‘b’, ‘c’, ‘d’]
marxes.remove(‘b’)
marxes >>> [‘a’, ‘c’, ‘d’]

---

### 可以用 pop( ) 與位移值來取得一個項目，並且刪除它
呼叫 pop( ) 並使用一個位移值，他會回傳該項目，並且刪除它

marxes = [‘a’, ‘b’, ‘c’, ‘d’]
marxes.pop(1) >>> ‘b’
marxes >>> [‘a’, ‘c’, ‘d’]

備註：
沒有給出位移值的時候 pop ( ) 會使用 -1
簡單來說 pop(0) 會回傳 list 開頭並且刪除
pop( ) 和 pop(-1) 會回傳 list 的結尾並且刪除

---

## 其他
- 用 index( ) 和值來尋找某個項目的位移值
- 用 in 來測試在 list 中，值是否存在
- 用 count( ) 來算出某個值的出現次數
- 用 join( ) 來轉換成字串
- 用 sort( ) 來排序項目
- 用 len( ) 來取得 list 長度
- 用 = 來指派 / 用 copy 來複製

---

### 搜尋 / 用 index( ) 和值來尋找某個項目的位移值
```
marxes = [‘a’, ‘b’, ‘c’, ‘d’]
marxes.index(‘c’) >>> 2
```

---

### 用 in 來測試在 list 中，值是否存在
```
marxes = [‘a’, ‘b’, ‘c’, ‘d’]

‘a’ in marxes >>> True
0 in marxes >>> False
```

###### 備註：
list 中可能相同的值會出現多次，只要有出現一次， in 就會回傳 True

---

### 用 count( ) 來算出某個值的出現次數
```
marxes = [‘a’, ‘b’, ‘c’, ‘d’]
other = [‘a’,’a’]
marxes += other
marxes = [‘a’, ‘b’, ‘c’, ‘d’, ‘a’, ‘a']

marxes.count(‘a’) >>> 3
marxes.count(‘x’) >>> 0 
```

---

### 用 join( ) 來轉換成字串
```
marxes = [‘a’, ‘b’, ‘c’, ‘d’]
‘,’.join(marxes) >>> ‘abcd’
```

###### 備註：
1.
join 是 string method，不是 list method  
所以其實我們不能使用 marxes.join(‘,’)  

2.
join 只會回傳字串  
回顧一下 join  
>>> (要拿掉、並且組合起來的字串).join(串列)  

3.
可以直接記憶 join( ) 是 split( ) 的相反即可  

join( ) 將 list 合併成 string  
split( ) 將 string 分解成 list  

---

### 用 sort( ) 來排序項目
*  list 函式 sort( ) 會就地排序 list 本身，也就是 list 本身的值會被改變 (但沒有回傳值)  
* 通用函式 sorted( ) 會排序串列之後回傳複本  

預設情形下會升冪排序  
數字由小到大  
string 就是按照字母順序  
```
marxes = [1, 3, 4, 5, 2]
sorted_marxes = sorted(marxes) 
sorted_marxes >>> [1,2,3,4,5]
marxes >>> [1, 3, 4, 5, 2]
```
此時的 sorted_marxes 是一個複本，不會改變原本的 list

```
marxes = [1, 3, 4, 5, 2]
marxes.sort( ) 
marxes >>> [1,2,3,4,5]
```
此時是對著 marxes 來呼叫 list 函式 sort( )，所以會改變 marxes  

###### 備註：  
1.
串列的類型都相同時會正確動作  
有時也可混合使用多種類型 (整數與浮點數) Python 會先將他們轉換、排序之後再換回原值回傳  

2.
預設排序是昇冪
但可加入引數 reverse = True 來轉換成降冪

```
marxes = [1, 3, 4, 5, 2]  
marxes.sort(reverse = True)  
marxes >>> [5,4,3,2,1]  
```

---

### 用 len( ) 來取得 list 長度
```
marxes = [1, 3, 4, 5, 2]
len(marxes) >>> 5
```

---

### 用 = 來指派 / 用 copy 來複製

當我將 list 指派給多個變數的時候，只要在其中一處改變了 list ，其他變數的 list 值也會改變，其實很簡單，就是標籤跟物品的概念  
```
a = [1,2,3]  
b = a  
b >>> [1,2,3]  

a[0] = ‘a’  
b >>> [‘a’,2,3]  
```
但如果此時我們採用 copy( ) 、list( )、slice( ) 來製作序列，各個物品就會是新的  
```
a = [1,2,3]  
b = a.copy( )  
c = list(a)  
d = a[:]  
```

---

### 參考資料：
Lubanovic, Bill. Introducing Python: modern computing in simple packages. " O'Reilly Media, Inc.", 2014.


