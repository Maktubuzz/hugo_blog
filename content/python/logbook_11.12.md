+++

image = ""
comments = false
share = true
menu= ""		# set "main" to add this content to the main menu
author = "Ti Ｗoo"

date =  "2017-11-13T17:01:01+08:00"
title =  "11/12 - pdb debugging、Regular Expressions"
draft =  false
slug =  ""
tags = ["python", "Udemy", "pdb", "debugging", "Regular Expressions"]
type = "posts"

+++

<!--more-->

pdb 是一個可以交互測試 source code 的 package  
精神基本上就是設置 breakpoint 來反覆測試哪邊有 bug  
可參考：  
http://python.jobbole.com/81184/  
http://www.jianshu.com/p/fb5f791fcb18  
http://www.jianshu.com/p/fb5f791fcb18  

---

##### Regular expression

搜尋內功，幾乎我的專案都曾經用到 (我猜有些是直接引援搜尋套件啦，但還是有少部分是自己用 RE 來寫)，派派說過這個要好好練，基本上每個語言的這個寫法都相同

目前的想像中，RE 在之後 data cleansing 上會用上許多

課程丟了很多 syntax 出來，但我跟著寫了一些之後決定還是直接看 python 官方文件比較快：  
https://docs.python.org/3.6/library/re.html  
趕時間的話可以看看繁體中文版本的、別人的筆記：  
http://zwindr.blogspot.tw/2016/01/python-regular-expression.html  

有問題再回來看看人家怎麼寫的  
```
re.search('none', 'Searching for pattern in text’))
match = re.search('pattern', 'Searching for pattern in text')
print(match)

print(match.re.pattern)
print(match.string)
print(match.start())
print(match.end())

regex = re.compile('pattern')
print(regex.search('Searching pattern in text...').start())

print(regex.findall('Searching pattern in text... pattern'))

print(re.match('Match', 'Match function test'))
print(re.match('test', 'Match function test.’)) >>> None
```

.match( ) 只抓一開頭


---

##### 參考資料：
- https://www.udemy.com/learn-python-3-from-beginner-to-advanced/
