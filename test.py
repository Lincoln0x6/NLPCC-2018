# -*- coding: utf-8 -*-
#import tensorflow 
#import jieba
data_file_path="data/nlpcc-iccpol-2016.kbqa.change.kb"
import time
#import numpy as np
#from pyemd import emd
#import codecs
#import jieba
#jieba.load_userdict("data/entity.txt")
import random
import json
# import gensim
# from gensim.models import word2vec
#sentences = word2vec.Text8Corpus("data/corpusSegDone.txt")  # 加载语料
#model = word2vec.Word2Vec(sentences, size=200)  # 默认window=5
#model.wv.save_word2vec_format("data/word_model.bin", binary=True)
#word="计算两个向量的点积 "
#word_list=jieba.cut(word)
#print(type(word_list),word_list)
#word_list=list(word_list)
#print(type(word_list),word_list)
# =============================================================================
# train_base_path="data/2018train/"
# 
# ne_file_name="NE_result.txt"
# POS_file_name="POS_result.txt"
# filename="data/word_model_2.bin"
# ne_list=[]
# with open(train_base_path+ne_file_name,"r",encoding="utf-8") as file_1:
#     ne_list=file_1.readlines() 
#     ne_list[0] = ne_list[0].replace("\ufeff","")
# if filename.endswith('.bin'):
#         model = gensim.models.KeyedVectors.load_word2vec_format(filename, binary=True)
#         start=time.time()
#         all=[]
#         count=0
#         word_no_find=[]
#         for line in ne_list:
#             line_split=line.split()
#             result=[]
#             for word in line_split:
#                 try:
#                     result.append(model[word])
#                 except:
#                     word_list=list(jieba.cut(word,cut_all=False))
#                     vector=[0]*200
#                     for new_word in word_list:
#                         try:
#                             word_vec=model[new_word]
#                         except:
#                             word_vec=[random.random()]*200
#                             word_no_find.extend([word,new_word])
#                             count=count+1
#                         vector=[vector[i]+word_vec[i] for i in range(len(word_vec))]
#                     vector=[vector[i]/len(word_list) for i in range(len(vector))]
#                     result.append(vector)
#             all.append(result)
#         print(len(all))
#         print("cost",time.time()-start)
#         print("no find",count)
#         print(word_no_find)
#         with open("data/word_no_fin.txt","w",encoding="utf-8") as  file_1:
#             file_1.write(json.dumps(word_no_find))
#             
#             
# =============================================================================
#        start=time.time()
#        s1="今天 天气 晴朗"
#        s2="天气 预报 表示 今天 阳光 明媚"
##        print(type(model.wv.vectors))
##        array=model.wv.vectors
##        print(array)
##        order = 'F' if np.isfortran(array) else 'C'
#        print(model.most_similar("天气"))
#        print(model.wmdistance(s1, s2))
#        print("cost",time.time()-start)
#        print(len(model.wv.vectors))
#        print(array.dtype,array.shape,np.isfortran(array))
#        new_array=np.memmap(filename, array.dtype, "r",0, array.shape, 'C')
#        model.wv.vectors=new_array
#        print(type(new_array),len(new_array))
#        model.wv.vectors=new_array
#        print("vec",type(model.wv.vectors))
#        print(model.most_similar("朋友"))
#        dict_key=[1, 39315, 2, 20, 12, 34, 61, 181, 2324, 262, 103, 3316, 149, 8362, 32, 29, 24, 5234, 83, 2295, 43458, 2089, 104, 125, 37, 45, 88, 63, 2094, 349, 224, 1003, 2766, 22471, 367, 180, 785, 132258, 77836, 7557, 31012, 62335, 270204, 205675, 96421, 81248, 129115, 982, 175238, 152624, 192001, 131028, 168608, 126931, 9308, 128280, 57059, 163754, 102413, 175235, 92985, 118557, 33087, 139802, 34348, 155057, 60367, 256397, 14887, 189753, 132229, 21694, 151124, 171655, 52279, 47419, 253888, 277011, 94392, 1787, 35089, 213330, 8661, 50205, 6632, 17256, 64028, 166541, 9736, 88421, 5941, 164697, 259005, 10658, 77813, 113904, 197094, 147812, 122385, 103494, 79965, 132035, 37750, 29344, 55726, 164512, 263107, 26318, 141628, 51845, 16538, 186504, 2648, 179825, 41241, 166529, 94660]
#        array=new_array
#        print((array.filename, array.dtype, array.mode,array.offset, array.shape, order))
#        print(array[300000])


#model = word2vec.load('data/corpusWord2Vec.bin')
#print(len(model.vectors))
#print(type(model.vectors))
#array=model.vectors
#order = 'F' if np.isfortran(array) else 'C'
#print(array.dtype, array.offset, array.shape, order)
#print(model.vocab[10000])
#filePath='data/corpusSegDone.txt'
#word2vec.word2vec(filePath, 'data/corpusWord2Vec.bin', size=150,verbose=True)
#with open(data_file_path,"r",encoding="utf-8")as file_1:
#    text=file_1.readline()
#    last_entity=""
#    while(count<1000000):
#        text_split=text.split("|||",2)
#        
#        text=file_1.read_line()



global start_time
def start_work(work_name):
    global start_time
    start_time=time.time()
    try:
        print("start to execute part ",work_name," now time is ",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    except:
        print("wrong")
def finish_work(work_name):
    global start_time
    try:
        print(work_name," finish now is ",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())," \ncost time: ",time.time()-start_time)
    except:
        print("function finish_word can't work")
#start_work("jieba_cut")
#filePath='data/nlpcc-iccpol-2016.kbqa.change.kb'
#fileSegWordDonePath ='data/corpusSegDone_1.txt'
## read the file by line
#fileTrainRead = []
# #fileTestRead = []
#with open(filePath,"r",encoding="utf-8") as fileTrainRaw:
#    line=fileTrainRaw.readline()
#    while line:
#        line_split=" ".join(line.split("|||",2))
#        fileTrainRead.append(line_split)
#        line=fileTrainRaw.readline()
#
## define this function to print a list with Chinese
#def PrintListChinese(list):
#    for i in range(len(list)):
#        print(list[i])
## segment word with jieba
#fileTrainSeg=[]
#print("start jieba cut")
#stopword = ['是', '在', '什么', '的', '为','曾','《','》','，','吗','呀','嘛','呢','啊','是什么', '了']
#for i in range(len(fileTrainRead)):
#    pre_list=list(jieba.cut(fileTrainRead[i],cut_all=False))
#    after_list=[]
#    for word in pre_list:
#        if word not in stopword:
#            after_list.append(word)
#    fileTrainSeg.append(' '.join(after_list))
#    if i % 100000 == 0 :
#        print(i)
#
#with open(fileSegWordDonePath,'w',encoding="utf-8") as fW:
#    for i in range(len(fileTrainSeg)):
#        try:
#            if "\n" not in fileTrainSeg[i]:
#                fW.write(fileTrainSeg[i]+"\n")
#            else:
#                fW.write(fileTrainSeg[i])
#        except:
#            print(fileTrainSeg[i])
#fileTrainSeg=None
#fileTrainRead=None
#finish_work("jieba_cut")
# =============================================================================
# word="lll(这个是)111"
# import re
# pattern=re.compile(r'(?<=[(])[^()]+.[^()]+(?=[)])')
# word=pattern.sub("",word).replace("()","")
# 
# print(word)
# 
# file_name="data/corpusSegDone_1.txt"
# word2df={}
# first_entity_dict={}
# count=0
# with open(file_name,"r",encoding="utf-8") as file_1:
#     line=file_1.readline()
#     while line:
#         word_set=set()
#         line=line.encode('utf-8').decode('utf-8-sig')
#         line=line.replace("\n","").strip()
#         line_split=line.split()
#         entity=line_split[0]
#         clean_entity=pattern.sub("",line_split[0]).replace("()","")
#         if clean_entity not in first_entity_dict:
#             first_entity_dict[clean_entity]={}
#             first_entity_dict[clean_entity]["relate_entity_dict"]={}
#         first_entity_dict[clean_entity]["relate_entity_dict"][entity]=first_entity_dict[clean_entity]["relate_entity_dict"].get(entity,0)+1
#         
#         for word in line_split:
#             if (word not in word_set):
#                 word_set.add(word)
#                 word2df[word]=word2df.get(word,0)+1
#         line=file_1.readline()
#         count=count+1
#         if count%5000000==0:
#             print("deal ",count)
# 
# train_base_path="data/2018test/"
# ne_file_name="NE_result.txt"
# POS_file_name="POS_result.txt"
# type_set=set(["n","nd","nh","ni","nl","ns","nt","nz","i","j"])
# 
# with open(train_base_path+ne_file_name,"r",encoding="utf-8") as file_1:
#     ne_list=file_1.readlines()
# with open(train_base_path+POS_file_name,"r",encoding="utf-8") as file_1:
#     pos_list=file_1.readlines()
# start=time.time()
# result_list=[]
# count=0
# no_find_set=set()
# file_2=open("data/info_entity.txt","w",encoding="utf-8")
# line_length=20
# for ne_line,pos_line in zip(ne_list,pos_list):
#     info_dict={}
#     ne_line=ne_line.encode('utf-8').decode('utf-8-sig').replace("\n","")
#     pos_line=pos_line.encode('utf-8').decode('utf-8-sig').replace("\n","")
#     possible_entity=[]
#     info_dict["line"]=ne_line
#     ne_line_split=ne_line.strip().split()
#     pos_line_split=pos_line.strip().split()
#     ques_entity_info={}
#     for word,pos in zip(ne_line_split,pos_line_split):
#         if pos in type_set:
#             if word in word2df:
#                 ques_entity_info[word]={}
#                 ques_entity_info[word]["df"]=word2df[word]
#             else:
#                 ques_entity_info[word]={}
#                 ques_entity_info[word]["df"]=0
#                 no_find_set.add(word)
#             if word in first_entity_dict:
#                 ques_entity_info[word]["found_in_dict"]=True
#                 ques_entity_info[word]["entity_info"]=first_entity_dict[word]
#             else:
#                 ques_entity_info[word]["found_in_dict"]=False
#                 
#     info_dict["entity_info"]=ques_entity_info
#     info_dict["pos_line"]=pos_line
#     count=count+1
#     file_2.write(ne_line+" ".join(str(x)+"\t"+str(y) for x,y in ques_entity_info.items())+" \n")
#     if(count%10==0):
#         print("has count",count," cost",time.time()-start)
#     #tuple=(ne_line,line_vector)
#     info_dict["poss_entity_list"]=possible_entity
#     result_list.append(info_dict)
# with open("data/length_idf.txt","w",encoding="utf-8") as file_1:
#     file_1.write(json.dumps(result_list))
# with open("data/entity_related_info.txt","w",encoding="utf-8") as file_1:
#     file_1.write(json.dumps(first_entity_dict))
# file_2.close()
# with open("data/no_find_word.txt","w",encoding="utf-8") as file_1:
#     file_1.write(" ".join(list(no_find_set)))
# 
# =============================================================================
# =============================================================================
# start_work("build train data")
# stopword = ['是', '在', '什么', '的', '为','曾','《','》','，','吗','呀','嘛','呢','啊','是什么', '了']
# base_data_dir="data/train_with_entity/"
# file_name="gold_entity_relation_new.txt"
# result_dict={}
# flag=True
# count=0
# def get_max_len_word(words):
#     result=""
#     max_len=0
#     for word in words:
#         if len(word) >max_len:
#             max_len=len(word)
#             result=word
#     return result
#             
# with open(base_data_dir+file_name,"r",encoding="utf-8") as file_1:
#     lines=file_1.readlines()
#     for line in lines:
#         temp_dict={}
#         line_split=line.split("|||",2)
#         if not len(line_split)==3:
#             print("line:",line)
#             continue
#         question=line_split[1].strip()
#         ans_entity=""
#         try:
#             ans_entity=line_split[2].split()[0]
#         except:
#             print(line_split[2])
#             ans_entity=str(line_split[2])
#         if ans_entity in result_dict:
#             continue
#         vector=[0]*20
#         word_part_list=list(jieba.cut(question,cut_all=False))
#         new_word_part_list=word_part_list
#             
#             #flag=False
#         if count<=100:
#             print(word_part_list,ans_entity)
#         
#         count=count+1
#         poss_entity=[]
#         pre_pos=0
# #        for word in word_part_list:
# #            if word not in stopword:
# #                new_word_part_list.append(word)
#         for word in new_word_part_list[:20]:
#             if (word in ans_entity) or (ans_entity in word):
#                 word_pos=new_word_part_list.index(word)
#                 if (word_pos-pre_pos)==1 or (word_pos==0):
#                     pre_pos=word_pos
#                     vector[word_pos]=1
#                 #poss_entity.append(word)
#         #topic_entity= get_max_len_word(poss_entity)
# #        try:
# #            vector[new_word_part_list.index(topic_entity)]=1
# #        except:
# #            print("wrong",line,poss_entity)
# #            continue
# #                    vector[new_word_part_list.index(word)]=1
#         temp_dict["ans_entity"]=ans_entity
#         temp_dict["vector"]=vector
#         temp_dict["word_part_list"]=new_word_part_list
#         temp_dict["jieba_cut"]=str(" ".join(new_word_part_list)).strip()
#         result_dict[question]=temp_dict
# with open("data/json_final_1.txt","w",encoding="utf-8") as file_1:
#     file_1.write(json.dumps(result_dict))
# result_list=[]
# count=0
# for question,info_dict in result_dict.items():
#     count=count+1
#     if count<10:
#         print(info_dict["jieba_cut"],info_dict["vector"])
#     temp_dict={}
#     temp_dict["line"]=info_dict["jieba_cut"]
#     temp_dict["tag_vector"]=info_dict["vector"]
#     temp_dict["question"]=question
#     result_list.append(temp_dict)
# 
# with open("data/json_final_4.txt","w",encoding="utf-8") as file_1:
# 
#     file_1.write(json.dumps(result_list))
# finish_work("build train data")
# =============================================================================
# =============================================================================
# sentences = word2vec.Text8Corpus("data/corpusSegDone_1.txt")
# start_work("word2vec") 
# model = word2vec.Word2Vec(sentences, size=200,min_count=3)  # 默认window=5
# model.wv.save_word2vec_format("data/word_model_2.bin", binary=True)
# model=None
# finish_work("word2vec")
# 
# =============================================================================

start_work("test entity predict")
global no_match
no_match=["哪年","多少人","国脚","国家队","队长","巴西足球"]
data_file_path="'nlpcc2018.trainset/knowledge/nlpcc-iccpol-2016.kbqa.kb'"
big_dict={}
with open(data_file_path,"r",encoding="utf-8")as file_1:
    text=file_1.readline()
    last_entity=""
    temp_list=[]
    count=0
    while(text):
        text=text.strip("\n").strip()
        text_split=text.split("|||",2)
        if(text_split[0]==last_entity):
            big_dict[last_entity][text_split[1]]=text_split[2]
        else:
            #file_2.write(last_entity+"\t"+(" ".join(temp_list))+"\n")
            last_entity=text_split[0]
            if last_entity not in big_dict:
                    big_dict[last_entity]={}
            big_dict[last_entity][text_split[1]]=text_split[2]
        text=file_1.readline()
        count=count+1
        if(count%1000000==0):
            print("have deal",count)
print("finish")
ne_file_name="NE_result.txt"
def get_min_df_word(target_dict):
    global no_match
    result=""
    min=1000000
    for word,info in target_dict.items():
        if word not in no_match:
            if info["df"]<min:
                result=word
                min=info["df"]
    return result
type_set=set(["n","nd","nh","ni","nl","ns","nt","nz","i","j"])
result_list=[]
count=0
start=time.time()

with open("length_idf.txt","r",encoding="utf-8")as file_1:
    
    question_info_list=json.loads(file_1.read())         
    for question_info in question_info_list:
        count=count+1
        if count%2==0:
            print("deal",count,"cost_time",time.time()-start)
        temp_dict={}
        match_num=0
        question_line=question_info["line"]
        temp_dict["line"]=question_line
        possible_entity=[]
        entity_dict=question_info["entity_info"]
        real_entity=get_min_df_word(entity_dict)
        for key in big_dict.keys():
            if match_num>15:
                break
            if real_entity in key:
                match_num=match_num+1
                possible_entity.append([key,big_dict[key]])
        temp_dict["poss_entity"]=possible_entity
        result_list.append(temp_dict)
with open("get_entity_by_idf_2.txt","w",encoding="utf-8")as file_1:
    file_1.write(json.dumps(result_list))

finish_work("test_entity predict")


file_4=open("ques_entity_num.txt","w",encoding="utf-8")
file_3=open("my_test_answer.txt","w",encoding="utf-8")
with open("get_entity_by_idf.txt","r",encoding="utf-8") as file_1:
    result_list=json.loads(file_1.read())
    for ques_info in result_list:
        count=0
        question_line=ques_info["line"]
        entity_info_list=ques_info["poss_entity"]
        for entity_info in entity_info_list:
            key_entity=entity_info[0]
            entity_info=entity_info[1]
            for key,value in entity_info.items():
                file_3.write(question_line+"|||"+key_entity+"|||"+key+"|||"+value+"\n")
                count=count+1
            file_4.write(str(count)+"\n")
