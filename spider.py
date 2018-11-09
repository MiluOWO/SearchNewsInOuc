#-*- coding：utf-8 -*-
import requests
from lxml import etree
import re
def WriteList(listUrl):
	r = requests.get(listUrl)
	#编码注意一下-print(r.text.encode('utf-8'))
	Page =etree.HTML(r.text).xpath('//*[@id="mainText_Last"]/@href')
	#页码是从0开始的
	ready = re.compile(r'page=\d+')
	page = ready.findall(Page[0])
	pages = page[0].replace('page=','')
	#print(pages)
	contentList = []	
	titleName = []
	titleDic={}
	pageUrl = "http://it.ouc.edu.cn/Display/ClickMore.aspx?more=1&&page="
	filename1 = 'urlAndTitle.txt'
	with open(filename1,'w',encoding='utf-8') as file_write:
		for i in range(0,int(pages)+1):
			newUrl= pageUrl+str(i)
			r = requests.get(newUrl)
			title = etree.HTML(r.text).xpath('//*[@class="clickMore-inforText"]/h3/text()')
			contentUrl = etree.HTML(r.text).xpath('//*[@class="clickMore-inforLine"]/ul/li/a/@href')
			#写新闻列表，名。 title存在吞字情况。比较麻烦。不搞
			for j,z in zip(contentUrl,title):
				if("http" not in j):
					titleName.append(z)
					NewContetUrl = 'http://it.ouc.edu.cn/Display/'+ j
					contentList.append(NewContetUrl)
					file_write.write(z+'\n')
					file_write.write(NewContetUrl+'\n')
	with open('title.txt','w',encoding='utf-8') as file_write:
		for i,j in enumerate(titleName):
			file_write.write(j+'\n')
			titleDic[i]=j
	WriteContent(contentList)
	return titleDic
#不读it.ouc.edu.cn以外的站点，麻烦
def WriteContent(contentList):
	for i in contentList:
		r = requests.get(i)
		title = etree.HTML(r.text).xpath('//*[@class="content-tittle"]/h1/text()')
		content = etree.HTML(r.text).xpath('//*[@class="content-article"]//span/text()')
		if(content==[]):
			content = etree.HTML(r.text).xpath('//*[@class="content-article"]//p/text()')
		title[0] = title[0].replace('"','')
		filename = './article/'+title[0]+'.txt'
		with open(filename,'w',encoding='utf-8') as file_write:
			for j in content:
				file_write.write(j)

def main():
	listUrl = 'http://it.ouc.edu.cn/Display/ClickMore.aspx?more=1' 
	dic={}
	dic=WriteList(listUrl)
	#print(dic)
	print('done')

if __name__ == "__main__":
	main()