---
date: "2017-06-28T17:11:00+08:00"
title: "Numeric Types"
draft: false
slug: ""
tags: ["python",]
type: posts
author: "Ti Ｗoo"
---


Python 內的數字類型
<!--more-->

#### 類別：####
* 整數
* 浮點數

---

#### 運算：####

1. 除法

    * / 算出浮點 (十進位) 除法
    * // 算出整數 (捨去) 除法
    * 分母不能為 0 
  
2. 其他

    * ％ 只取餘數
    * 同時取得商數跟餘數的方法
        * divmod (9, 5) 會得到 (1,4)

---

#### 類型轉換
###### 整數
* 用 int 函數來把其他的資料類型轉換成整數

```
(疑問：說好的強類型語言呢)

說實話我實在太好奇了所以查了一下強弱類型：
 https://www.zhihu.com/question/19918532
但這東西我暫時看了沒 fu 看一下結論有個 sense 就行
大抵就是說強類型不容忍隱式的類型轉換

而同樣的這篇也有提到，強類型容忍在一定條件下、一定規則的類型轉換：http://www.jianshu.com/p/bc57ad6f35c4
```
---

#### 整數類型轉換有幾個有趣的點：
* int(True)  >>> 1    同理也可以轉成浮點數 float(True)
* int(False) >>> 0    
* 直接用 True + 2 >>> 3 

也有不能轉換的時候：  

* 像 int( ’98.6’ ) 就不能被成功轉換
    * 但 int(’98’) 可以 >>> 98
* int(1.0e4) 是不行的， 1.0e4 是 >>> 10000.0
    * 另外補充一個命名規則 10 * 10 * 10 * 10 = 10**4 = 1.0E4 (值啦，但在 python 內會是浮點數呈現)
* int( 各式文字 ) 這就不用說啦絕對不行的

---

#### 浮點數
* 用 float( ) 來轉換
* 可轉換 int( ’98.6’ ) >>> 98.6
    * 我的想法是 int 不能轉換的原因純粹因為他只執行一次轉換，換成 98.6 之後就停了，但同時 98.6 不符合 int 的整數輸出值，所以 error

---

### 參考資料：
Lubanovic, Bill. Introducing Python: modern computing in simple packages. " O'Reilly Media, Inc.", 2014.


