+++

image = ""
comments = false
share = true
menu= ""		# set "main" to add this content to the main menu
author = "Ti Ｗoo"

date =  "2017-11-03T17:22:35+08:00"
title =  "11/03 - class __init__、private attribute"
draft =  false
slug =  ""
tags = ["python", "Udemy", "Class"]
type = "posts"

+++


<!--more-->

##### (1)
class 在建立的過程中，可以先指定 arg 的值，有帶 arg 進來的會被覆蓋，沒有的則會使用原先的值
```
class Complex:
'this class simulate complex numbers'
def __init__(self, real = 0, imag = 0):
        self.real = real
        self.imag = imag
c = Complex(2)
print (c.real, c.imag)
```

---

##### (2)
如果是 self.__something = something 的話  
就代表這個 __something 是 private 的  

也就是說，要是一個類別裡的 __init__ method 用到 __something 這個 attribute，那我在建立這個類別的物件的時候， call self.__something 會 call 不到東西，因為這個物件不會有該類別 private 的 attribute  

---

##### 參考資料：
- https://www.udemy.com/learn-python-3-from-beginner-to-advanced/
