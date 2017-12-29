+++

image = ""
comments = false
share = true
menu= ""		# set "main" to add this content to the main menu
author = "Ti Ｗoo"

date =  "2017-10-28T17:23:50+08:00"
title =  "10/28"
draft =  false
slug =  ""
tags = ["python", "Udemy"]
type = "posts"

+++


在學習 file management 的過程中，教學者有用到開檔案之類的會用 ```open (‘file location’,’r+’) ``` 但沒有對於那個 `r+` 多做解釋，後來在使用 ```file.mode``` 的過程中也有 print 出 `r` 或是 `w+` 之類的資訊  <!--more-->

查了一下發現是開啟檔案時要設定的東西，有點像是之前用 terminal 對檔案做權限改變 (也就是 chmod 啦)

像是 w+ 就是會開啟一個檔案 reading and writng，他會 overwrite 已存在相同檔名的檔案，如果設定的檔名不存在，那就會新創建一個檔案來 reading and writng

##### 相關資訊：
https://stackoverflow.com/questions/16208206/confused-by-python-file-mode-w

---

##### 備註：
同一篇文章另外學到一些東西，Udemy 上的講師一直有用到 file.seek(0) 這段 code ，不知道是不是漏聽，我始終不知道這個要用在哪裡，不過這答案也在同篇文章裡找到啦

因為如果沒有使用 file.seek(0) 的話，file.read( ) 就會去讀檔案的最尾端、然後回傳 empty string

當初會這樣設計應該有原因，還沒查之前我記錄一下先。


##### 參考資料：
- https://www.udemy.com/learn-python-3-from-beginner-to-advanced/
