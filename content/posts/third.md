---
title: "XUST 自动打卡"
date: 2021-02-17T13:31:44+08:00
draft: false
tags: ['xust','打卡']
categories: ['post']

featuredImage: ""
featuredImagePreview: ""

hiddenFromHomePage: false
hiddenFromSearch: false
twemoji: true
lightgallery: true
ruby: true
fraction: true
fontawesome: true
linkToMarkdown: true
rssFullText: false

toc:
  enable: true
  auto: true

  # ...
---
# xust实现全自动打卡
***
>这是个令人激动的时刻对于我们来说\
>这个项目让我们告别了每天繁琐的五点打卡\
>导员的催促、班委的通知\
>却也还是总让我们忘记，从而得到导员温柔的问候

## <font color = 'pink'>接下来开始正体 </font>
所需软体和条件  
* 一个可以手机抓包的软件(<font color ='	#87CEFA'>ps:还没看pc版的西科e站包在哪里，后续可能回更新</font>)  
* 你需要你个登录了西科e站的微信app  
* 需要一个富强的环境(ps:当然GitHub也可以不，会很慢🤣🤣)  
  
***
### 1.首先打开抓包软体,找到如下图所示的包 获uid!  
![uidpc](https://tu.yaohuo.me/imgs/2021/02/d914926b9fd343d0.png "uidpc")
![uid1](https://tu.yaohuo.me/imgs/2021/02/5c9aef7ecd88ad2f.png "uid1")
![uid2](https://tu.yaohuo.me/imgs/2021/02/ff5296304a1ddd79.png "uid2")
### 2.电脑登入西科e站,f12,点打卡提交后,找到如下的包,获得最下边的payload!  
![payload](https://tu.yaohuo.me/imgs/2021/02/d4276c8006dd7b78.jpg "payload")
### 3.有了上边两个步骤之后,访问我的项目地址,并且fork我的仓库[Checkin](https://github.com/Victor9578/checkin),并替换python文件里的uid,payload,自此今后的打卡就会上传你payload的信息!  
![GitHub](https://tu.yaohuo.me/imgs/2021/02/4c1536854078e033.png "github")
>><font color='#FFE4C4'>ps:当然你可以替换文件里的sckey,从此获得消息推送,如出现{}字符,即为打卡成功</font>

***


# 感谢你的观看<font color='red'>❤</font>😁

<!--

