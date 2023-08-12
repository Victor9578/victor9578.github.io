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
    hidden: true # 文章内不显示/显示 #

ShowToc: true #显示toc目录树 #
TocOpen: true # toc目录树展开 #
katex: true # 数学公式 #
mermaid: true # 流程图 #
weight: false # 置顶 #
hidemeta: false # 隐藏页面元素如：作者、时间等 #
# description: "Desc Text." # 单页面标题 #
---
