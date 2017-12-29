---
date: "2017-06-30T17:17:09+08:00"
title: "String"
draft: false
slug: ""
tags: ["python",]
type: posts
author: "Ti Ｗoo"
---

Python 的 string 及其使用方法
<!--more-->

#### 使用單、雙引號
* 目的是讓你能在引號中使用引號
    * “ ’Nay,’ said the naysayer.”
* 三引號是用在互動式解譯器中、包住長 & 換行字串用的
* print ( ) 會將字串引號去除 

---

#### 用 str ( ) 來轉換資料類型
str(98.6)
>>> ’98.6’

---

#### 用 \ 來轉義
\ 的作用：  

* 用 \t 來對齊文字 (t 的由來是因為 tab)
    * print (‘a\tbc’) >>> a    bc
    * 用 \’ 或 \” 來維持 print 後的單雙引號
        * ‘ \”I did nothing! ”\ ” >>> “I did nothing!”
    * 同理，需要 print 後的反斜線就用 \\ 就行

---

#### 用 + 來結合常值字串 & 字串變數  

* “1” + “2” >>> “12”
* a = “1” , b = “2” , a + b = “12”

注意一下字串變數也可以用來相加

---

#### 可用 * 來複製字串

start = ‘Na’ * 4 + ‘\n’  
middle = ‘Hey’ * 3 + ‘\n’  
end = ‘Goodbye.’  
print( start + middle + end )  
>>> Na Na Na Na 
        Hey Hey Hey 
        Goodbye.

備註：
注意一下兩個有引號的物件相加後，引號會融合(? XD)
‘Na’ + ‘Hey’ >>> ‘NaHey’

---

#### 用 [   ] 來擷取字元
letters = 'abcdefghijklmnopqrstuvwxyz'
letters[1] = b

括號內的 0、1、2、3…etc 用位移值會比較好想像

超出字串長度會顯示顯示 indexError
例如： letters[100]

---

#### Slice
* [開始 : 結束 : 間隔]
* letters[3: 18 : 2]
    * 從 d 開始 (第 4 位)
    * 到字母 r 結束
(第 18 位，這邊很容易誤解，因為 letters[18] 的值其實是 s ，也就是第 19 位數，end 的點會在你選擇的值的「前一位數」)
    * 以 2 的位移值來取值
* letters[3: 18 : 2] >>> ‘dfhjlnpr’
* 可以用負數
    * letters[-1:] >>> ‘z’
    * letters[:-1:-1] >>> ‘ ‘
    * letters[-1::-1] >>> ‘zyxwvutsrqponmlkjihgfedcba’
* 容許不良位移值
    * letters[-50] >>> error
    * letters[-50:] >>> ‘abcdefghijklmnopqrstuvwxyz’

話說容許不良位移值這件事情我沒有很懂  
目前測試是 letters[-26] >>> ‘a’  
letters[-27] 以下都是 error  
letters[-50:] 、letters[-51] 和 letters[-52] 一樣都是 >>> ‘abcdefghijklmnopqrstuvwxyz’ 

---

###### 目前推斷是說：
1. -26 達到字串逆順序的底了，再往下就顯示 error ，所以一個字串以位移值來取值，其實擁有自己的兩倍長度的擷取範圍
2. letters[-27:] 開始不論 - 到多少，吐回來的都會是 >>> ‘abcdefghijklmnopqrstuvwxyz’ (letters[-26:] 的值本來就是 >>> ‘abcdefghijklmnopqrstuvwxyz’ 所以不算)

---

###### 邏輯上：
* 從哪裡開始
* 在哪裡結束
* 用什麼順序抓 (沒用負數的話就是順向抓取資料)

---

#### 使用內建函式來處理字串
函式的使用方法：字串名稱.函式(引數)

---

###### 用 len( ) 來取得字元數量
len(letters) >>> 26

備註：
len( ) 可與其他序列類型一起使用 

---

###### 用 split( ) 來分割
分割完後的值會變成一個 list

* todos = ‘get gloves,get mask,give cat vitamins,call ambulance’
todos.split(‘,’) 
 “”” 以 ‘,’ 為分隔標準 “”“
* 使用 split 時如果沒有帶入引數，會直接使用空白字元做分隔

---

###### 用 join( ) 來結合 list 成為字串
和 split( ) 相反，會把 list 裡的複數個字串成為一個字串

使用方式：
要接起來拿掉的字串.join(串列)

* crypto_list = [‘Yeti’, ‘Bigfoot’, ‘Lincoln’]
crypto_string = ‘,’.join(crypto_list)

---

###### 把玩字串的各種方法
這個就看對字串專用的函式熟不熟了，我先瞄過而已，沒有認真看

---

###### 用 replace( ) 來替換
使用方式：  

* 要被替換的東西.replace (舊的字串, 新的字串, 要替換掉幾個）  
* 如果沒說要替換幾個的話他只會替換第一個

備註：
在確定要替換的字串的時候很好用，要替換全部的字串的時候還是用正規表達式會比較好

---

### 參考資料：
Lubanovic, Bill. Introducing Python: modern computing in simple packages. " O'Reilly Media, Inc.", 2014.


