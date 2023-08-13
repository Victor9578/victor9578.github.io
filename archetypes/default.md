---
title: "{{ replace .Name "-" " " | title }}" # 日期 #
date: {{ .Date }} # 日期 #
draft: false # 草稿与否 #
tags: [] # 标签 #
categories: [] # 分类 #

summary: "" # 文章简介 #
author: ["Jaywxl"] # 作者 #

cover:
    image: "" # 图片链接 #
    alt: "" # 图片名称 #
    hidden: false # 文章内不显示/显示 #

weight: false # 置顶 一般置顶 10（同weight参考时间）#

katex: false # 数学公式 #
mermaid: true # 流程图 #
hidemeta: false # 隐藏页面元素如：作者、时间等 #
# description: "Desc Text." # 单页面标题 #
---
