#coding=utf-8
# import re
# import json
# import time
# file_1_name="nlpcc2018.trainset/knowledge/nlpcc-iccpol-2016.kbqa.kb"
# file_2_name="nlpcc2018.trainset/knowledge/nlpcc-iccpol-2016.kbqa.change.kb"
# start = time.time()
# file_2=open(file_2_name,"w",encoding="utf-8")
# new_word_list=[]
# bad_word_list=[]
# with open(file_1_name,"r",encoding="utf-8") as file_1:
#     word_item=file_1.readline()
#     count=1
#     bad_num=0
#     while word_item :
#         is_well=True
#         word_place=0
#         for word in word_item.split("|||",2):
#             word=word.strip(" ")
#             word_place=word_place+1
#             if word=="":
#                 is_well=False
#                 print(word_item)
#                 bad_word_list.append(word_item)
#                 break
#             if word.strip(word[0])=="":
#                 new_word_list.append(word)
#                 continue
#             if word=="[]":
#                 new_word_list.append(word)
#                 continue
#             word=word.replace("■","").replace("ˇ","").replace("：",":").\
#                       replace("◎","").replace("，",",").replace("。",".").\
#                       replace("“","\"").replace("”","\"").replace("（","(").\
#                       replace("）",")")
#             #if word_place==2:
#                 #对第二维进行去空格，大写转小写操作
#             word=word.replace(" ","")
#             word=word.lower()
#             pattern=re.compile(r'(\[\d{1,3}\])')
#             word=word.strip("-*|•,.")
#             word=re.sub(pattern, "", word)
#             new_word_list.append(word)
#             if word=="":
#                 is_well=False
#                 bad_word_list.append(word_item)
#                 print(word_item)
#                 break
#         if is_well:
#             file_2.write("|||".join(new_word_list))
#         else:
#             bad_num=bad_num+1
#         new_word_list.clear()
#         count=count+1
#         if count%1000000==0:
#             print("have transform ",count/10000,"万 cost time ",time.time()-start,"bad_num is ",bad_num)
#         word_item=file_1.readline()
# with open("bad_word_json_list.txt","w",encoding="utf-8") as file_3:
#     file_3.write(json.dumps(bad_word_list))
# file_2.close()
# end=time.time()
# print("cost:",end-start)
#
# file_1_name="nlpcc2018.trainset/knowledge/nlpcc-iccpol-2016.kbqa.change.kb"
# file_2_name="nlpcc2018.trainset/knowledge/nlpcc-iccpol-2016.kbqa.new.kb"
#
# f_2 = open(file_2_name,'w',encoding='utf-8')
# count = 0
# with open(file_1_name,'r',encoding='utf-8') as f_1:
#     for line in f_1.readlines():
#         count = count + 1
#         tok = line.split('|||',2)
#         if tok[1].strip() == tok[2].strip():
#             print(count,"行删除")
#         else:
#             f_2.write(line)
#
#         if count%100000 ==  0:
#             print(count%10000,"万行")
# f_2.close()

# file_1_name="nlpcc2018.trainset/knowledge/nlpcc-iccpol-2016.kbqa.kb.mention2id"
# file_2_name="nlpcc2018.trainset/knowledge/nlpcc-iccpol-2016.kbqa.kb.new.mention2id"
# f_2 = open(file_2_name,'w',encoding='utf-8')
# count = 0
# with open(file_1_name,'r',encoding='utf-8') as f_1:
#     for line in f_1.readlines():
#         count = count + 1
#         line = line.replace('（','(').replace('）',')').replace('：',':').replace('，',',').replace('？','?').replace('！','!')
#         line = line.lower()
#         f_2.write(line)
#         if count%10000 ==  0:
#             print(count%10000,"万行")
# f_2.close()
#
file_1_name="nlpcc2018.trainset/knowledge/nlpcc-iccpol-2016.kbqa.kb"
file_2_name="nlpcc2018.trainset/knowledge/nlpcc-iccpol-2016.kbqa.new.kb"

f_2 = open(file_2_name,'w',encoding='utf-8')
count = 0
with open(file_1_name,'r',encoding='utf-8') as f_1:
    for line in f_1.readlines():
        count = count + 1
        tok = line.split('|||',2)
        tok[1] = tok[1].replace('【','').replace('】','')
        line = tok[0].strip() + '|||'+tok[1].strip()+ '|||'+ tok[2].strip() + '\n'
        f_2.write(line)
        count = count + 1
        if count%100000 ==  0:
            print(count%10000,"万行")
f_2.close()
