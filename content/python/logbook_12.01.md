+++

image = ""
comments = false
share = true
menu= ""		# set "main" to add this content to the main menu
author = "Ti Ｗoo"

date = "2017-12-01T17:01:00+08:00"
title = "12/01 - 階層算法"
draft = false
slug =  ""
tags = ["python", "Udemy", "Algorithm"]
type = "posts"

+++

factorial 算法：

<!--more-->

```
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(7))
```
