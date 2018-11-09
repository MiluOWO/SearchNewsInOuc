import jieba
import jieba.analyse
def main():
    count=0
    for line in open("title.txt","r",encoding='utf-8'):
        count=count+1
    #新建字典title_dict,键对应（1-5294）的数字，值是对应的新闻标题
        
    title_dict={}
    url_dict={}
    
    with open('url.txt',"w",encoding='utf-8') as file_write:
        i=1
        for line in open("urlAndTitle.txt","r",encoding='utf-8'):
            if(i%2!=0):
                i +=1
                pass
            else:
                i +=1
                file_write.write(line)

                
    f=open("title.txt","r",encoding='utf-8')
    i=1
    #将文字的每行标题存入字典
    for line in open("title.txt","r",encoding='utf-8'):
        #添加一个删除字符串末尾/n的操作
        title_dict[i]=line
        i=i+1
       # print(line)

    f=open("url.txt","r",encoding='utf-8')
    i=1
    #将文字的每行标题存入字典
    for line in f:
        #添加一个删除字符串末尾/n的操作
        url_dict[i]=line
        i=i+1
     
    #将字典title_dict中的值分别进行分词操作
    seg_list={}
    tags={}
    #将分词存入tags字典，值为对应的分词组成的列表
    for j in range(1,count+1):
        #搜索引擎模式
        seg_list[j] =jieba.cut_for_search(title_dict.get(j))
        #精确模式
        #seg_list[j]=jieba.cut(title_dict.get(j),cut_all=True)
        tags[j]=jieba.analyse.extract_tags(title_dict.get(j), topK=40)
        
    # print(tags)
     
     
    #将分词后的结果存入词项字典
    word_dict={}
    for k in range(1,count+1):
        for z in range(0,int(len(tags.get(k))-1)):   #字典中每个值中，元素的个数
            word_dict.setdefault(tags.get(k)[z])
            if(word_dict.get(tags.get(k)[z])==None):
                word_dict[tags.get(k)[z]]=[]
                word_dict[tags.get(k)[z]].append(k)
            else:
                word_dict[tags.get(k)[z]].append(k)
     
    #print(word_dict)
    #print(title_dict)
    return(word_dict,title_dict,url_dict)

if __name__ == '__main__':
    main()




