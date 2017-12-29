+++

image = ""
comments = false
share = true
menu= ""		# set "main" to add this content to the main menu
author = "Ti Ｗoo"

date =  "2017-11-05T17:23:17+08:00"
title =  "11/05 - anaconda、conda"
draft =  false
slug =  ""
tags = ["python", "Udemy", "anaconda"]
type = "posts"

+++

<!--more-->

anaconda 是一個用於科學計算的多合一 python 安裝程式，自帶很多 lib (或許還有 IDE 和編輯器)，而 conda 是用於 package 管理 + 環境管理，跟 pip + virtualenv 很像，但兩個我都沒用過，到底多像也沒個底

主要是 anaconda 安裝好之後，發現沒辦法像查到的資料一樣直接使用 conda 指令，花了大概一個多小時才搞定，其實就是 PATH 要改的問題，如：https://stackoverflow.com/questions/18675907/how-to-run-conda

```
for anaconda 3 :
export PATH=~/anaconda3/bin:$PATH
```

改成這樣就 OK 了 (自學有時候就是比較花費時間啊… )

另外觀察到一件事情，以往我用 terminal 運行 python 會 default 運行 python 2.7 ，想要用 python 3 的話要輸入 python 3。在安裝完 anaconda 並改過 PATH 之後，現在不論是打 python 或是 python3 都是基於 anaconda 開啟的，另外輸入 python 2.7 則會運行 python 2.7 

本來在擔心會不會有什麼問題，想想覺得概念上應該不會，先記錄下來吧




---

##### 參考資料：
- https://www.udemy.com/learn-python-3-from-beginner-to-advanced/
