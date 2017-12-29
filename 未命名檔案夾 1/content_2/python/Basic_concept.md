---
title: "Basic Concept"
date: 2017-06-25T17:22:59+08:00
draft: False
---

簡單紀錄 Python 的一些基礎概念  <!--more-->
 
  
#### String
* 要用單引號 (‘) 或是雙引號 (“) 包起來
* 可以相加 
    * “I “ + “have “ + “a “ + “dog.” = I have a dog.
* 可以乘法來多次顯示「並相加」
    * “woo ” * 3 = “woo woo woo”
* len( ) 語法可知字串長度
    * len(“123456”) = 6
* str( ) 把東西轉成字串
    * len( str(123456 ) ) = 6
 
  
#### 變數 (variables)

* pet = “kitty”
    * 意即 “kitty” 這個 “物件” 被標上了一個 pet 標籤
    * 此時 python 執行 pet ，會列出變數內容 “kitty”
    * 可轉換變數內容，直接令 pet = 想改變的內容即可

#### Lists
* [   ] 
* 是列表
* 可放數字和字串
    * 加東西進 list
        * lottery = [4, 12, 13, 15, 23]
    * 取東西出來 lottery [1]
        * 位置標示其實從 0 開始
        * 可使用負數 lottery [-1] 取出來會是 23 
    * 換東西進 list
        * 將該位置直接標示為想換的東西，如 lottery [3] = 1，此時 lottery 會是 [4, 12, 1, 15, 23]


#### dict (Dictionaries)
* {  }
* 儲存 key 和 value 的對應關係 
* 可放數字、字串、list
    * 加東西進 dict
        * my_information = {'name': 'Pusheen the Cat', 'country': 'USA', 'favorite_numbers’: [3, 9] }
    * 找到 key 指向的值
        * 輸入 my_information [’name’] 會出現 ‘Pusheen the Cat’
    * 可用 len ( ) 來查看 dict 裡面有多少資料
        * len (my_information) 會回覆 3
    * 新增 key 和其對應的值
        * my_information[‘favorite_color’] = ‘citrine white’
        * 此時 len (my_information) 會回覆 4
    * 刪除 dict 裡的資料
        * del my_information[‘favorite_number’]
        * 此時 my_information 會是 {'name': 'Pusheen the Cat', 'country': 'USA', 'favorite_color’: ‘citrine white’ }
    * 修改 key 對應的值
        * my_information[’name’] = ‘Pusheen’

#### 比較
* >  
* <
* ==
* >=
* <=

#### Boolean
* True
* False

開頭一定要大寫

#### print
* pet = ‘Pusheen’
    * 此時讓 python 執行 pet 會輸出這個變數的表示式 P u s h e e n 七個字母和前後兩個引號
* print pet 會回應 Pusheen
    * 此時做的是印出 pet 的內容

#### if… elif… else
```
if 3 > 2:
    print( )
elif 3 ==3:
    print( )
else 2 > 5:
    print (2)
```
* 不要忘記在 if / elif / else 條件之後加上冒號
* 沒有 if 的情況下不能使用 elif / else
* 可以有多個 elif 條件設定
    * 但執行到一個條件就不會繼續往下了
* 不能有多個 else 條件

#### def (函示)
```
def hi( ):
    執行 blablabla
hi( )
```
* 不要忘記括號和冒號
* 最後以 ```函示名稱( )``` 來進行執行
* 可加入 argument
```
def hi(name):
    print(‘Hi ‘+ name +’!’)
hi(‘人名’)
* 最後是把該給的 argument 給函示
```

#### 物件 (Objects)
##### 概念：
1、2、3、4 屬於「數字」這種「class」，而 1、2、3、4 是數字這個 class 的 instance (實例)

##### 建立一個貓物件來看看：

```
class Cat:
    def meow(self):
        print (‘Meow !’)
Pusheen = Cat( )
Pusheen.meow( )
```

* Pusheen = Cat( ) 這段是在創建一隻叫做 Pusheen 的貓 (實例)
* 最後使用 「 . 」來呼叫物件裡的方法

##### 為貓物件多加一點性質：

```
class Cat:
    def __init__(self,name):
        self.name = name
    def meow(self):
        print('Meow !’)
```

我們建立了一個 pusheen 的貓物件  
但其實還沒設定名字  
此時想要取名字的話，將名字參數帶入即可：

```
class Cat:
    def __init__(self,name):
        self.name = name
    def meow(self):
        print('Meow !')

pusheen = Cat('Pusheen’)
pusheen.meow()
```

但此時 print(pusheen) 其實得不到什麼資訊
只會給你

```
<__main__.Cat object at 0x101407be0>
```

##### 要幫 pusheen 設定 print 出來資訊的話：
```
class Cat:
    def __init__(self,name):
        self.name = name
    def meow(self):
        print('Meow !')
    def __str__(self):
        return 'Cat: ' + self.name

pusheen = Cat('Pusheen')
print(pusheen)
```
當 python 要 print 東西出來的時候
會使用 __str__ 來「詢問」物件要被轉成什麼樣的字串
針對這樣的詢問我們可用 return 來回答

注意一下 self.name 的用法
不是 name
直接使用 name 的話會有 error 


另外來講一下利用 class 建立新物件的流程
pusheen = Cat(‘Pusheen’)  
這行做的事情是；  

* 查看 Cat 類別的「定義」
    * 這邊的「定義」我還沒完全清楚，目前只知道 __init__ 是類別定義式的一種，或許要查查看有什麼 dunder 可用
* 在記憶體中按照 Cat 類別的定義「實例化」(建立) 一個新物件
    * 呼叫物件裡的 __init__ 方法 (因為是按照 Cat 類別的定義，所以也有相同的 __init__ 方法)，把新物件傳遞給 self，以及把另一個 argument ‘Pusheen’ 傳遞給 name
* 在新物件中儲存 name 的值 (也就是 self.name = name 啦，前面是指該物件的名字，後面的 name 則是傳遞進來的參數)
* 回傳新物件
* 將新物件指派給名稱 pusheen

備註：
我們傳入的 name 值 ‘Pusheen’ 會被當成物件屬性，跟物件一起被儲存，可以直接讀取或寫入他

pusheen.name 會回傳 Pusheen

#### Loop
```
girls = [‘1’, ‘2’, ‘3’, ‘4’, ‘5’, ‘6']

for name in girls:
    print(name) 
```
會輸出 1 2 3 4 5 6 


---

### 參考資料：
- http://freedomknight.me/guan-yu-python-zhong-de-self/
- Lubanovic, Bill. Introducing Python: modern computing in simple packages. " O'Reilly Media, Inc.", 2014.

