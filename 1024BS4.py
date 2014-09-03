from bs4 import BeautifulSoup
import urllib2

respon=urllib2.urlopen("http://ruai.lesile.net/thread0806.php?fid=7")
soup=BeautifulSoup(respon.read(),from_encoding="gb18030")


for tdlist in soup.find_all('td'):
    print tdlist.name,"    ",tdlist.attr,"\n"
    if tdlist.get("style")!='None' :# and tdlist['style']=="text-align:left;padding-left:8px":
	h3_tag=tdlist.contents[0]
	print h3_tag.name

	



