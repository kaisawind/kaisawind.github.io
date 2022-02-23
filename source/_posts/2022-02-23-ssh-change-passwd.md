---
layout: post
title:  "ssh登陆时一直提示修改密码"
date: 2022-02-23 10:42:16
categories: [linux]
tags: [linux， kernel]
excerpt_separator: <!--more-->
---
ssh登陆时一直提示修改密码
<!--more-->

需要修改/etc/shadow
```bash
root:$6$9w5Td6lg$bgpsy3olsq9WwWvS5Sst2W3ZiJpuCGDY.4w4MRk3ob/i85fl38RH15wzVoom:15775:0:99999:7:10:88888:
```

`root`:用户名
`$6$9w5Td6lg$bgpsy3olsq9WwWvS5Sst2W3ZiJpuCGDY.4w4MRk3ob/i85fl38RH15wzVoom`: 用户密码，无法手动修改
`15775`: 上一次修改密码距离1970-01-01的天数。`date -d "1970-01-01 15775 days"`进行查看
`0`: 最小修改时间间隔，0表示随时可以修改
`99999`: 密码有效期，天数
`7`: 密码需要变更前的警告天数
`10`: 密码过期后的宽限天数,过期10天内仍然可以登陆，-1表示永远不会失效
`88888`: 帐号过期时间


