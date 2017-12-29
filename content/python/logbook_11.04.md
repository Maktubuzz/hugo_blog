+++

image = ""
comments = false
share = true
menu= ""		# set "main" to add this content to the main menu
author = "Ti Ｗoo"

date =  "2017-11-04T17:15:15+08:00"
title =  "11/04 - 運行函式的錯誤猜想、類別繼承、類別內部部分繼承"
draft =  false
slug =  ""
tags = ["python", "Udemy", "Class"]
type = "posts"

+++

(1)

在學 class 的過程中，發現一些之前的錯誤猜想。

<!--more-->

之前我簡單的將 something.fuction( ) 視為對 something 本身執行 function 並改變 something 自身的值 ; 而 function( something ) 則被我視為把 something 當作 arg 帶入 function 並建立一個全新的物件並回傳



class 的學習過程中發現類別本身會內建一些 fucntion，而該類別的所屬物件，在最單純的以類別建立物件的情形下 (沒有繼承) 可以接使用 .function( ) 來使用物件內部的 function

舉例來說： 
```
class Vehicle :
    def __init__(self, VIN, weight, manufacturer):
        self.vin_number = VIN
        self.weight = weight
        self.manufacturer = manufacturer
    def GetWeight(self):
        return self.weight
    def GetManufacturer(self):
        return self.manufacturer
    def VehicleType(self):
        pass
```

這時候如果我建立一個 Vehicale 類別的物件 a 就能使用 GetWeight 等等的 function
```
a = Vehicle(‘VIN;, 10, ‘MAN' )
a.GetWeight( ) >>> 10   
```
也就是說 something.fuction( ) 應該不是直接對自身的值做什麼改變，要看 function 到底是什麼而定

---

(2)   

class 的繼承最簡單的方法，就是直接在括號內帶入父類別的名稱。以剛剛的 Vehicle class 為例，創建一個子類別 Car 的方法是：
class Car(Vehicle):

如此一來 Car 類別就會繼承 Vehicle 類別，只要 function 沒有被覆寫，也都能使用 Vehicle 的內建函式  

而覆寫函式的方法也很簡單，就是直接定義一個名稱一樣的 function 即可，會以後來定義的 function 為主  

而如果只想部分覆寫繼承而來的 function 也有辦法，可以使用 super( ) 來做  

以上面的 Vehicle 和 Car 類別為例，假設想在 Car 類別建立物件的時候多存一個 attribute `seats`，那就是從 __init__ 來加入：
```
class Vehicle :
    def __init__(self, VIN, weight, manufacturer):
        self.vin_number = VIN
        self.weight = weight
        self.manufacturer = manufacturer
    def GetWeight(self):
        return self.weight
    def GetManufacturer(self):
        return self.manufacturer
    def VehicleType(self):
        pass


class Car(Vehicle):
    def __init__ (self, VIN, weight, manufacturer, seats):
        super().__init__(VIN, weight, manufacturer)
        self.seats = seats

g = Car(1, 2, 3, 5)

print (g.vin_number) >>> 1

```

##### 備註：
* 注意要部分繼承的東西要全部寫進 super( ).__init__( ) 裡面  
* 然後 super().method() 是讓我們不用再寫一次 Vechicle 裡定義過的 VIN、weight、manufacturer，只需要補 seats 的定義就行  


---

##### 參考資料：
- https://www.udemy.com/learn-python-3-from-beginner-to-advanced/
- https://taizilongxu.gitbooks.io/stackoverflow-about-python/content/19/README.html
