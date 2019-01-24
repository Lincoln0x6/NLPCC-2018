# coding=utf-8
import data_process
import jieba
import pynlpir
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import NamedEntityRecognizer

class KeyWordExtraction(object):
    def __init__(self):
        dp = data_process.Data_Process()
        self.questions,_ = dp.train_set_parser()
        qu_len = len(self.questions)
        self.questions_unchanged = self.questions[0:qu_len]
        self.questions = self.questions[0:qu_len]
        jieba.load_userdict('entity.txt')

    def jieba_extraction(self):
        jieba_extraction_each = []
        jieba_extraction_all = []
        pos_all = []
        stopword = ['《','》','，','吗','呀','嘛','呢','啊', '了']
        for i in range(len(self.questions)):
            tok = '='.join(jieba.cut(self.questions[i])).split('=')
            for j in range(len(tok)):
                if tok[j] not in stopword:
                    jieba_extraction_each.append(tok[j])
            print('No.',i)
            jieba_extraction_all.append(jieba_extraction_each)
            jieba_extraction_each = []
        for i in range(len(jieba_extraction_all)):
            pos_all.append(self.posttagger(jieba_extraction_all[i]))
        return jieba_extraction_all,pos_all

    # #词性标注
    def posttagger(self,words):
        postagger = Postagger()
        postagger.load('D:\\BaiduYunDownload\\ltp_data_v3.4.0\\pos.model')  # 加载模型
        postags = postagger.postag(words)  # 词性标注
        postagger.release()
        return list(postags)

    # pyltp实体识别
    def ner(self,words, postags):
        recognizer = NamedEntityRecognizer()
        recognizer.load('D:\\BaiduYunDownload\\ltp_data_v3.4.0\\ner.model')
        netags = recognizer.recognize(words, postags)  # 命名实体识别
        recognizer.release()  # 释放模型
        return list(netags)

    def output2file(self):
        jieba_extraction_all,pos_all = self.jieba_extraction()
        with open('NE_result.txt', 'w', encoding='utf-8') as file_1:
            for i in range(len(jieba_extraction_all)):
                for j in range(len(jieba_extraction_all[i])):
                    file_1.write(jieba_extraction_all[i][j] + ' ')
                file_1.write('\n')
        with open('POS_result.txt', 'w', encoding='utf-8') as file_2:
            for i in range(len(pos_all)):
                for j in range(len(pos_all[i])):
                    file_2.write(pos_all[i][j] + ' ')
                file_2.write('\n')
                print(i+1)
                print(jieba_extraction_all[i])
                print(pos_all[i])


KeyWordExtraction().output2file()

# pynlpir.open()

# entity_list = []

#加载entity列表和entity字典
# with open('entity.txt','r',encoding='utf-8') as file_1:
#     for line in file_1.readlines():
#         entity_list.append(line.strip())
# print('entity upload complete')

# entity_dict_file = open('entity_dict.txt','r',encoding='utf-8')
# entity_dict = eval(entity_dict_file.read())
# print('entity dict unload complete')

# entity_list.sort(key=lambda x:len(x),reverse=True)
# entity_dict_file.close()

# for i in range(len(questions)):
#     print(i+1)
#     print(questions[i])
#     # print(pynlpir.segment(questions[i],pos_tagging=False))
#     # print(pynlpir.get_key_words(questions[i],weighted=False))
#     # print(' '.join(jieba.cut(questions[i])))
#     print()

#pyltp分词

# def segmentor(sentence):
#     segmentor = Segmentor()
#     # segmentor.load_with_lexicon('D:\\BaiduYunDownload\\ltp_data_v3.4.0\\cws.model',
#     #                'C:\\Users\\Lincoln\\PycharmProjects\\NLPCC2018_KBQA\\entity.txt')  # 加载模型
#     segmentor.load('D:\\BaiduYunDownload\\ltp_data_v3.4.0\\cws.model')
#     words = segmentor.segment(sentence)
#     words_list  = list(words)
#     result = []
#     for i in range(len(words_list)):
#         if words_list[i] not in stopword_1:
#             result.append(words_list[i])
#     segmentor.release()
#     return result
#

# L = []
# L_in = []
# for i in range(qu_len):
#     print('i = ',i+1)
#     s = segmentor(questions[i])
#     print(s)
#     p = posttagger(s)
#     print(p)
#     n = ner(s,p)
#     print(n)
#     for j in range(len(n)):
#         if n[j] != 'O':
#             L_in.append(s[j])
#     L.append(L_in)
#     L_in = []
# f = open('test_result.txt','w',encoding='utf-8')
# for i in range(len(L)):
#     for j in range(len(L[i])):
#         f.write(L[i][j] + ' ')
#     f.write('\n')
# f.close()

# nlpir_extraction_each = []
# nlpir_extraction_all = []

# for i in range(len(questions)):
#
#     print('i = ',i)
#     for k in range(len(entity_list)):
#         if entity_list[k] in questions[i] and len(entity_list[k]) >= 2:
#             questions[i] = questions[i].replace(entity_list[k],'')
#             nlpir_extraction_each.append(entity_list[k])
#
#     # tok = pynlpir.segment(questions[i],pos_tagging=False)
#     for j in range(len(tok)):
#         if tok[j] not in stopword:
#             nlpir_extraction_each.append(tok[j])
#     nlpir_extraction_each.append(tok)
#     nlpir_extraction_all.append(nlpir_extraction_each)
#     nlpir_extraction_each = []

# for i in range(len(jieba_extraction_all)):
#
#     print(jieba_extraction_all[i])
#     p = posttagger(jieba_extraction_all[i])
#     print(p)
#     n = ner(jieba_extraction_all[i],p)
#     print(n)

# pynlpir.close()

# for i in range(qu_len):
#     # print('jieba:', jieba_tool_result[i])
#     # print('nlpir:', nlpir_tool_result[i])
#     # print('jieba:',jieba_extraction_all[i])
#     print(i+1,nlpir_extraction_all[i])
#     print()

# file_output = open('trainset_result.txt','w',encoding='utf-8')
# for i in range(qu_len):
#     for j in range(len(nlpir_extraction_all[i])):
#         file_output.write(nlpir_extraction_all[i][j] + ' ')
#     file_output.write('\n')
#
# file_output = open('testset_result.txt','w',encoding='utf-8')
# for i in range(qu_len):
#     for j in range(len(nlpir_extraction_all[i])):
#         file_output.write(nlpir_extraction_all[i][j] + ' ')
#     file_output.write('\n')


# L = [['《机械设计基础》', '这本书', '作者', '是谁'],['《高等数学》', '出版社', '哪个', '出版'],['时间是什么', '线性代数', '这本书', '出版', ]
#      ,['安德烈', '国家', '哪个'],['李明', '哪里', '老家'],['大学计算机基础', '这本书', '多少'],['《毛泽东》', '一本', '怎样', '装订']
#      ,['总裁', '周迅', '公司'],['是什么', '李军', '医生', '学校'],['陈平', '国家', '哪个', '来自'],['和平村', '哪个'],['少数民族', '是什么', '杨明']]
#
# question = [['《机械设计基础》这本书的作者是谁'],['《高等数学》是哪个出版社出版的'],['《线性代数》这本书的出版时间是什么'],['安德烈是哪个国家的人呢']
#             ,['李明的老家是哪里'],['大学计算机基础这本书多少钱啊'],['有一本叫《毛泽东》的书是怎样装订的'],['周迅是哪家公司的总裁']
#             ,['李军医生是什么学校毕业的'],['陈平来自于哪个国家'],['和平村在哪个省市县镇'],['杨明是什么少数民族的人']]

# for i in range(len(extraction_all)):
#     min_each = []
#     can_add = True
#     for j in range(len(extraction_all[i])):
#         try:
#             min_each.append(questions_unchanged[i].index(extraction_all[i][j]))
#         except:
#             print(questions_unchanged[i],extraction_all[i][j])
#         if '《' in extraction_all[i][j] and can_add == True:
#             extraction_all[i][j] = extraction_all[i][j] + '1ok'
#             can_add = False
#     min_index = min_each.index(min(min_each))
#     if  not extraction_all[i][min_index].endswith('1ok') and can_add == True:
#         extraction_all[i][min_index] = extraction_all[i][min_index] + '1ok'
#
# keyword = []
#
# for i in range(len(extraction_all)):
#     keyword_each = []
#     for j in range(len(extraction_all[i])):
#         if extraction_all[i][j].endswith('1ok'):
#             keyword_each.append(extraction_all[i][j][:-3])
#     keyword.append(keyword_each)
#
#
# keyword_all = []
# count = 0
# for i in range(len(keyword)):
#     try:
#         keyword_all.append(entity_dict[keyword[i][0]])
#     except:
#         count = count + 1
#         print('no key number',count)
#
# for i in range(10):
#     print(questions_unchanged[i])
#     print(extraction_all[i])
#     print(keyword_all[i])
#     print()