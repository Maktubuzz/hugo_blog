+++

image = ""
comments = false
share = true
menu= ""		# set "main" to add this content to the main menu
author = "Ti Ｗoo"

date =  "2017-10-24T17:08:36+08:00"
title =  "10/24 - git、pip、virtualenv"
draft =  false
slug =  ""
tags = ["python", "git", "pip", "virtualenv"]
type = "posts"

+++


VScode 莫名的會一直跳出 `warn The git repository at '/Users/OOOO' has too many active changes, only a subset of Git feature…`  

<!--more-->

看到 git 那邊老是顯示 99+ 我就按下 discard all changes 然後所有檔案就被刪掉了  
我說的是自己的 Desktop  
用起來很可怕啊，還好之前有備份  

持續查不到原因之中，只好先放著  
基本上我應該沒有用 git 追蹤整個電腦裡的檔案才對  
(連 git init 都還沒有執行過)  

轉向安裝 `pip` 和 `virtualenv` 之中  
發現 Django girl 在學習過程中是最幫得上忙的  
因為有白話簡潔的描述、也幾乎考慮了所有初學者會困惑卡住的點  

---

##### 備註：
後來發現會追蹤這麼多檔案  
是因為我第一次安裝 git 的時候不小心 git 整台電腦啦～～～ 超雷  
處理方法就是把到家目錄下面 rm -rf .git/ 把 git 資料夾刪掉  

