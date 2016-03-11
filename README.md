# Cyworld Club Picture Crawler
(싸이월드 클럽 사진 크롤러)
Download every pictures in Cyworld club.(싸이월드 클럽의 모든 사진을 다운로드 받는 Python 스크립트)


##Usage
###Install Requirements
```
  pip install requests
```

###Get Club ID
![사진 슬라이드](./imgs/img1.png) 

Click "사진 슬라이드 보기"

![Club ID](./imgs/img2.png) 

Get Club ID from URL



###Edit Club ID
Edit ```cyworldpicture.py```
```
  #-*- coding: utf-8 -*-
  import requests
  import json
  
  club_id = ##Set Club ID
```
Put your Club ID Into ``` ##Set Club ID```


###Execute Script
  python cywordpicture.py

