#-*- coding: utf-8 -*-
import requests
import json

club_id = ##Set Club ID

mainurl = "http://club.cyworld.com/club/board/PhotoViewer/index.asp?club_id=%d"%club_id


header = {
	"Content-Type" :"application/x-www-form-urlencoded; charset=utf-8",
	"charset" :	"utf=8",
	"Referer" :	"http://club.cyworld.com/club/board/PhotoViewer/index.asp?club_id=%d"%club_id
}
session = requests.Session()

session.get("http://club.cyworld.com/club/board/PhotoViewer/index.asp?club_id=%d"%club_id)

def download_file(url,local_filename):

    r = session.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: 
                f.write(chunk)
    return local_filename

lastseq = ""

while 1:

	r = session.get("http://club.cyworld.com/CLUB/Board/PhotoViewer/GetPhotoListByDateJson.asp?lastseq="+lastseq+"&imgcount=30", headers =header)

	data = json.loads(r.text)

	if  "msg" in data:
		break

	from collections import OrderedDict

	od = OrderedDict(sorted(data.items(),reverse=True))




	for d in od:
		for img in od[d]["items"]:
			print (download_file(img["photoUrl"],img["writeDate"] +u"_" + img["title"].replace("/","-") +u"_" +str(img["itemSeq"]) +".jpg"))
			lastseq = str(img["itemSeq"])
