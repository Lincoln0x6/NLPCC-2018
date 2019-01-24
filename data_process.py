#coding=utf-8
import pickle
import random
class Data_Process(object):

    def __init__(self):
        # self.kb_dict_generator()
        pass
    #编辑距离算法
    def edit(self, first, second):
        if len(first) > len(second):
            first, second = second, first
        if len(first) == 0:
            return len(second)
        if len(second) == 0:
            return len(first)
        first_length = len(first) + 1
        second_length = len(second) + 1
        distance_matrix = [list(range(second_length)) for x in range(first_length)]
        for i in range(1, first_length):
            for j in range(1, second_length):
                deletion = distance_matrix[i - 1][j] + 1
                insertion = distance_matrix[i][j - 1] + 1
                substitution = distance_matrix[i - 1][j - 1]
                if first[i - 1] != second[j - 1]:
                    substitution =  substitution + 1
                distance_matrix[i][j] = min(insertion, deletion, substitution)
        return distance_matrix[first_length - 1][second_length - 1]
    #最长公共字串
    def lcsubstr(self,s1, s2):
        m = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
        mmax = 0
        p = 0
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    m[i + 1][j + 1] = m[i][j] + 1
                    if m[i + 1][j + 1] > mmax:
                        mmax = m[i + 1][j + 1]
                        p = i + 1
        return s1[p-mmax:p],mmax
    #最长公共子序列
    def lcs(self,a, b):
        lena = len(a)
        lenb = len(b)
        c = [[0 for i in range(lenb + 1)] for j in range(lena + 1)]
        for i in range(lena):
            for j in range(lenb):
                if a[i] == b[j]:
                    c[i + 1][j + 1] = c[i][j] + 1
                elif c[i + 1][j] > c[i][j + 1]:
                    c[i + 1][j + 1] = c[i + 1][j]
                else:
                    c[i + 1][j + 1] = c[i][j + 1]
        return c[lena][lenb]
    #映射字典生成
    def mention2id_dict_generator(self):
        mention2id_dict = {}
        mention2id_dict_value = []
        with open('nlpcc2018.trainset/knowledge/nlpcc-iccpol-2016.kbqa.kb.mention2id', 'r',
                  encoding='utf-8') as mention2id_file:
            print('mention2id_dict is constructing')
            for line in mention2id_file.readlines():
                tok = line.split('|||', 1)
                if len(tok) != 2:
                    continue
                tok_id = tok[1].strip().split('\t')
                for i in range(len(tok_id)):
                    mention2id_dict_value.append(tok_id[i])
                mention2id_dict.setdefault(tok[0].strip(),tok_id)
            print('mention2id_dict is ready')
        return mention2id_dict,mention2id_dict_value
    #知识库字典生成
    def kb_dict_generator(self):
        kb_dict = {}
        entity2relation = {}
        entity_dict = {}
        line_seen_entity = set()
        line_seen_name = set()
        line_seen_name_entity = set()
        # file_2 = open('entity.txt','w',encoding='utf-8')
        #file_3 = open('entity_dict.txt','w',encoding='utf-8')
        file_4 = open('KB_DICT.txt', 'wb')
        # file_5 = open('name.txt', 'w', encoding='utf-8')
        # file_6 = open('name_entity.txt','w',encoding='utf-8')
        file_7 = open('ENTITY_2_RELATION.txt', 'wb')
        with open('nlpcc2018.trainset/knowledge/nlpcc-iccpol-2016.kbqa.kb', 'r',
                  encoding='utf-8') as kb_file:
            print('kb_dict is constructing')
            for line in kb_file.readlines():
                tok = line.split('|||', 2)
                if len(tok) != 3:
                    continue
                # if tok[1].endswith('名') or tok[1].endswith('称') or tok[1].endswith('名称'):
                #     if tok[1] not in line_seen_name:
                #         file_5.write(tok[1] + '\n')
                #         line_seen_name.add(tok[1])
                #     if not tok[1].endswith('排名') and not tok[1].endswith('职称') and tok[1] != '专辑名称' and tok[1] != '粉丝名称':
                #         if tok[2] not in line_seen_name_entity:
                #             file_6.write(tok[2])
                #             line_seen_name_entity.add(tok[2])
                # if tok[1].endswith('绰号'):
                #     file_6.write(tok[2])
                #     line_seen_name_entity.add(tok[2])
                #
                # if  '(' in tok[0] and not tok[0].startswith('(') and not tok[0].startswith('《'):
                #     tokk = tok[0].split('(')
                #     if tokk[0] not in line_seen_entity:
                #         file_2.write(tokk[0].strip() + '\n')
                #         line_seen_entity.add(tokk[0])
                #     entity_dict.setdefault(tokk[0].strip(),set()).add(tok[0].strip())
                # else:
                #     # entity_dict.setdefault(tok[0].strip(),set()).add(tok[0].strip())
                #     if tok[0] not in line_seen_entity:
                #         file_2.write(tok[0].strip() + '\n')
                #         line_seen_entity.add(tok[0])
                # kb_dict.setdefault(tok[2].strip(), {}) [tok[0].strip()] = tok[1].strip()
                kb_dict.setdefault(tok[2].strip(),[]).append(tok[0].strip())
                kb_dict[tok[2].strip()].append(tok[1].strip())
                entity2relation.setdefault(tok[0].strip(),[]).append(tok[1].strip())
        # file_3.write(str(entity_dict))
        # file_4.write(str(kb_dict))
        # file_7.write(str(entity2relation))
        pickle.dump(kb_dict, file_4)
        pickle.dump(entity2relation, file_7)
        print('kb_dict is ready')
        file_4.close()
        # file_3.close()
        # file_2.close()
        # file_5.close()
        # file_6.close()
        file_7.close()
        # return kb_dict,entity2relation
    def get_entity_id_by_name(self,entity_name):
        if len(entity_name) == 0:
            return []
        result = self.mention2id_dict[entity_name]
        return result
    def get_predicates_by_entity_id(self,entity_id):
        if len(entity_id) == 0:
            return []
        result = (list(self.kb_dict[entity_id].keys()))
        return result
    def get_values_by_entity_predicate(self,entiey_id,predicate):
        result = []
        if len(entiey_id) == 0 or len(predicate) == 0:
            return []
        result.append(self.kb_dict[entiey_id][predicate])
        return result
    #加载训练数据
    def train_set_parser(self):
        questions = []
        answers = []

        stopword = ['麻烦你告诉我一下','谁能告诉我一下','请问','有谁知道','大家知道','谁知道','你知道','有人知道','我想知道','有没有人知道','你们知道',
                    '请告诉我','谁能告诉我','告诉我','比较好的','我想问一下，','我想问问','我想问','我很好奇','有没有人看过'
                    ,'有人认识','学汉语言的，','学化学的，','能告诉我','你听说','我想问一下','有没有','生物大神们','杨洋粉们，','你们清楚','你们了解'
                    ,'体育粉们，','呃我想请教一下','呃……','一下','谁能给我介绍一下','有认识','还有人记得','吗','呀','嘛','呢','啊']
        stopword.sort(key=lambda x:len(x),reverse=True)
        with open('nlpcc2018.trainset/nlpcc2018.kbqa.train', 'r', encoding='utf-8') as train_set:
            print('trainset is loading')
            for line in train_set.readlines():
                if "question" in str(line):
                    question_line = line.split('>', 1)
                    question_line[1] = question_line[1].replace('？','').replace('（','(').replace('）',')').replace(' ','').replace('，',',').replace("：",":").replace('。','.').replace('·','#卍#')
                    for i in range(len(stopword)):
                        if stopword[i] in question_line[1]:
                            question_line[1] = question_line[1].replace(stopword[i],'')
                    question_line[1] = question_line[1].strip().lower()
                    questions.append(question_line[1])
                if "answer" in str(line):
                    answer_line = line.split('>', 1)
                    answer_line[1] = answer_line[1].replace('（','(').replace('）',')').replace(' ','').replace('，',',').replace("：",":").replace('。','.').replace('“','"').replace('”','"').replace(' ','')
                    answers.append(answer_line[1].strip().lower())
            print('trainset is ready')
        return questions,answers
    #加载测试数据
    def test_set_parser(self):
        questions = []
        answers = []
        stopword = ['麻烦你告诉我一下', '谁能告诉我一下', '请问', '有谁知道', '大家知道', '谁知道', '你知道', '有人知道', '我想知道', '有没有人知道', '你们知道',
                    '请告诉我', '谁能告诉我', '告诉我', '比较好的', '我想问一下，', '我想问问', '我想问', '我很好奇', '有没有人看过', '有人认识', '学汉语言的，',
                    '学化学的，', '能告诉我', '你听说', '我想问一下', '有没有', '生物大神们', '杨洋粉们，', '你们清楚', '你们了解',
                     '体育粉们，', '呃我想请教一下', '呃……', '一下', '谁能给我介绍一下', '有认识', '还有人记得']
        stopword.sort(key=lambda x: len(x), reverse=True)
        with open('C:\\Users\\Lincoln\\PycharmProjects\\NLPCC2018_KBQA\\nlpcc2018.testset\\nlpcc2018.kbqa.test','r',encoding='utf-8') as test_set:
            print('testset is loading')
            for line in test_set.readlines():
                if 'question' in str(line):
                    tok = line.split('>',1)
                    tok[1] = tok[1].replace('？','').replace(' ','').replace('·','#卍#').replace('“','').replace('”','')
                    for i in range(len(stopword)):
                        if stopword[i] in tok[1]:
                            tok[1] = tok[1].replace(stopword[i],'')
                    questions.append(tok[1].strip().lower())
                if "answer" in str(line):
                    answer_line = line.split('>', 1)
                    answer_line[1] = answer_line[1].replace('（','(').replace('）',')').replace(' ','').replace('，',',').replace("：",":").replace('。','.').replace('“','"').replace('”','"').replace(' ','')
                    answers.append(answer_line[1].strip().lower())
            print('testset is ready')
        return questions,answers
    #一些处理
    def solution_to_kb(self):
        pass
        # 对知识库的若干处理
        # file_2 = open('name_new.txt','w',encoding='utf-8')
        # with open('name.txt','r',encoding='utf-8') as f_1:
        #     for line in f_1.readlines():
        #         if  '排名'not in line and '职称' not in line and '/' not in line:
        #             file_2.write(line)
        #
        # file_2.close()

        # entity_list = []
        # with open('entity.txt','r',encoding='utf-8') as file_1:
        #     for line in file_1.readlines():
        #         entity_list.append(line.strip().replace('·','').replace('《','').replace('》',''))
        #
        # print(len(entity_list))
        #
        # entity_list = list(set(entity_list))
        # entity_list.sort(key=lambda x:len(x),reverse=True)
        #
        # with open('entity.txt','w',encoding='utf-8') as f_1:
        #     for i in range(len(entity_list)):
        #         if len(entity_list[i]) <= 20 and len(entity_list[i]) >= 2:
        #             if  '、' in entity_list[i]:
        #                 tok = entity_list[i].split('、')
        #                 for k in range(len(tok)):
        #                     f_1.write(tok[k].strip() + '\n')
        #             else:
        #                 f_1.write(entity_list[i] + '\n')
    #载入字典
    def get_two_dict(self):
        # 用pickle保存和读取
        print('kb dict is uploading')
        kb_dict_file = open('KB_DICT.txt', 'rb')
        kb_dict = pickle.load(kb_dict_file)
        kb_dict_file.close()
        print('kb dict unload complete')

        print('entity2relation is unloading')
        entity2relation_file = open('ENTITY_2_RELATION.txt', 'rb')
        entity2relation = pickle.load(entity2relation_file)
        entity2relation_file.close()
        print('entity2relation unload complete')

        return kb_dict,entity2relation
        # 使用write(str(dict)) eval的方式存储和读取字典
        # print('kb dict is uploading')
        # kb_dict_file = open('kb_dict.txt','r',encoding='utf-8')
        # a = kb_dict_file.read()
        # kb_dict = eval(a)
        # print('kb dict unload complete')
        # kb_dict_file.close()
        #
        # print('entity2relation is unloading')
        # entity2relation_file = open('entity2relation.txt', 'r', encoding='utf-8')
        # b = entity2relation_file.read()
        # entity2relation = eval(b)
        # print('entity2relation unload complete')
        # entity2relation_file.close()

        # 直接生成
        # kb_dict,entity2relation = self.kb_dict_generator()


    #1.获得模型的原始训练数据
    def get_gold_entity_and_relation(self):
        f1 = open('训练数据1.txt', 'w', encoding='utf-8')
        f2 = open('bad_answer.txt', 'w', encoding='utf-8')
        f3 = open('训练数据2.txt', 'w', encoding='utf-8')
        kb_dict,entity2relation = self.get_two_dict()
        question,answer = self.train_set_parser()
        # LCS_result = []
        count1 = 0
        # question = question[0:30]
        # answer = answer[0:30]
        for question_id in range(len(answer)):
            print('question No.',question_id + 1)
            try:
                entity_relation_list = kb_dict[answer[question_id]]
            except KeyError:
                print('Key is NOT found')
                f2.write('No.' + str(question_id) + '\n')
                f2.write(question[question_id] + '\n')
                f2.write(answer[question_id] + '\n')
                count1 = count1 + 1
                continue

            entity = []
            relation = []
            for i in range(len(entity_relation_list)):
                if i % 2 == 0:
                    entity.append(entity_relation_list[i])
                else:
                    relation.append(entity_relation_list[i])
            if len(entity) == 1:
                print('only one')
                gold_entity = entity[0]
                gold_relation = relation[0]
                # relation_all.append(entity2relation[entity[0]])
                relation_all = entity2relation[gold_entity]

                try:
                    relation_all.remove(gold_relation)
                except:
                    f2.write('No.' + str(question_id) + '\n')
                    f2.write(question[question_id] + '\n')
                    f2.write(answer[question_id] + '\n')
                    count1 = count1 + 1
                    continue

                f1.write('1' + '|||' + question[question_id] + '|||' + gold_entity + ' ' + gold_relation + '\n')
                for n in range(len(relation_all)):
                    f1.write('0' + '|||' + question[question_id] + '|||' + gold_entity+ ' ' + relation_all[n] + '\n')
            else:
                print('more than one')
                for entity_id in range(len(entity)):
                #     length = self.lcs(question[question_id], entity[entity_id])
                #     LCS_result.append(length/len(entity[entity_id]) * 1.0)
                # print(LCS_result)
                # max_index = LCS_result.index(max(LCS_result))
                # LCS_result = []
                    if entity[entity_id] in question[question_id]:
                        gold_entity = entity[entity_id]
                        gold_relation = relation[entity_id]
                        # relation_all.append(entity2relation[entity[entity_id]])
                        relation_all = entity2relation[gold_entity]
                        break

                try:
                    relation_all.remove(gold_relation)
                except:
                    f2.write('No.' + str(question_id) + '\n')
                    f2.write(question[question_id] + '\n')
                    f2.write(answer[question_id] + '\n')
                    count1 = count1 + 1
                    continue

                f3.write('1' + '|||' + question[question_id] + '|||' + gold_entity + ' ' + gold_relation + '\n')
                for n in range(len(relation_all)):
                    f3.write('0' + '|||' + question[question_id] + '|||' + gold_entity + ' ' + relation_all[n] + '\n')
        f1.close()
        f2.close()
        f3.close()
        print(count1)
        # return gold_entity,gold_relation,relation_all
    #2.打乱训练数据并将正例加倍
    def shuffle_label(self):
        array = []
        array1 = []
        array0 = []
        EXPANSION = 1
        f2 = open('保留实体_正例乘1.txt', 'w', encoding='utf-8')
        with open('训练数据原始版本.txt', 'r', encoding='utf-8') as f1:
            for line in f1.readlines():
                line = line.strip()
                if line.startswith('1'):
                    array1.append(line)
                if line.startswith('0'):
                    array0.append(line)
        print(len(array1))
        print(len(array0))
        random.shuffle(array0)
        # new_len = len(array0)/2
        # array0 = array0[0:int(new_len)]

        for k in range(EXPANSION):
            for i in range(len(array1)):
                array.append(array1[i])
        print(len(array1))
        print(len(array))
        random.shuffle(array1)
        for i in range(len(array0)):
            array.append(array0[i])

        random.shuffle(array)
        for i in range(len(array)):
            f2.write(array[i] + '\n')
        print('ok')
        f2.close()
    #3.对训练数据句子进行分词
    def split_sentence(self):
        import jieba
        jieba.load_userdict('2018训练集小词典.txt')
        f = open('保留实体_正例乘12_句子分词.txt', 'w', encoding='utf-8')
        with open('保留实体_正例乘12.txt', 'r', encoding='utf-8') as file1:
            for line in file1.readlines():
                line = line.strip()
                tok1 = line.split('|||')
                tok2 = tok1[2].split()
                sentence = tok1[1]

                sub_str, _ = self.lcsubstr(sentence, tok2[0])
                entity_cut = ' '.join(jieba.cut(sub_str))

                sentence_cut = ' '.join(jieba.cut(sentence))
                line = line.replace(sentence, sentence_cut)
                line = line.replace(entity_cut, sub_str)
                line = line.replace('《', '').replace('》', '')
                f.write(line + '\n')
        f.close()
    #4.模型训练数据去除实体
    def get_rid_of_entity_1(self):
        count = 0
        f = open('不保留实体_正例乘12_句子分词.txt', 'w', encoding='utf-8')
        with open('保留实体_正例乘12_句子分词.txt', 'r', encoding='utf-8') as file1:
            for line in file1.readlines():
                count = count + 1
                tok1 = line.split('|||')
                tok2 = tok1[2].strip().split()
                print(count)
                print(len(tok2))
                try:
                    substr, _ = self.lcsubstr(tok1[1], tok2[0])
                    question_change = tok1[1].replace(substr, '').replace('《', '').replace('》', '').strip()
                    f.write(tok1[0] + '|||' + question_change + '|||' + tok2[1].strip() + '\n')
                except:
                    print(line)
                    break
        f.close()
    def get_rid_of_entity_2(self):
        count = 0
        f = open('my_test_answer_without_entity.txt', 'w', encoding='utf-8')
        with open('my_test_answer.txt', 'r', encoding='utf-8') as file1:
            for line in file1.readlines():
                count = count + 1
                tok = line.split('|||')
                print(count)
                substr, _ = self.lcsubstr(tok[0].strip(), tok[1].strip())
                question_change = tok[0].replace(substr, '').replace('《', '').replace('》', '')
                f.write(question_change + '|||' + tok[1] + '|||' + tok[2].strip() + '|||' +tok[3].strip() +'\n')
            f.close()
    #5.将训练数据的句子再分词
    def split_more_thoroughly(self):
        import jieba
        f2 = open('不保留实体_正例乘12_句子分词_属性分词.txt', 'w', encoding='utf-8')
        with open('不保留实体_正例乘12_句子分词.txt', 'r', encoding='utf-8') as f1:
            for line in f1.readlines():
                new_sen = ''
                new_relation = ''
                tok = line.strip().split('|||')
                old_relation = tok[2].strip()
                old_sen = tok[1]
                old_sen_tok = tok[1].split()
                new_relation = new_relation + ' '.join(jieba.cut(old_relation))
                for i in range(len(old_sen_tok)):
                    new_sen = new_sen + ' '.join(jieba.cut(old_sen_tok[i])) + ' '
                line = line.replace(old_sen, new_sen.strip()).replace(old_relation,new_relation.strip())
                f2.write(line)
                print(new_sen)
        f2.close()
    #6.将属性换成'的 relation 是'的形式
    def change_relation(self):
        file_input = '不保留实体_正例乘5_句子分词_属性分词_后添加实体.txt'
        file_output = '不保留实体_正例乘5_句子分词_属性分词且加工_后添加实体.txt'
        f = open(file_output, 'w', encoding='utf-8')
        with open(file_input, 'r', encoding='utf-8') as file1:
            for line in file1.readlines():
                tok1 = line.strip().split('|||',2)
                tok2 = tok1[2].strip().split('|||')
                print(len(tok2))
                if len(tok2) == 1:
                    relation_change = '的 '+ tok2[1] + ' 是'
                    line = line.replace(tok2[1],relation_change)
                    f.write(line)
                if len(tok2) == 2:
                    relation_change ='的 ' + tok2[1] + ' 是'
                    line = line.replace(tok2[1], relation_change)
                    f.write(line)
        f.close()
    #7.将实体加入到训练数据上
    def add_entity(self):
        entities = []
        count = 0
        f = open('不保留实体_正例乘12_句子分词_属性分词_后添加实体.txt','w',encoding='utf-8')
        with open('保留实体_正例乘12_句子分词.txt','r',encoding='utf-8') as f1:
            for line in f1.readlines():
                print(line)
                tok = line.split('|||')
                entity,relation = tok[2].strip().split(' ',1)
                entities.append(entity)
        entity_id = 0
        with open('不保留实体_正例乘12_句子分词_属性分词.txt','r',encoding='utf-8') as f2:
            for line in f2.readlines():
                count  = count + 1
                print('已完成:',count/len(entities) * 100,'%')
                tok = line.strip().split('|||')
                f.write(tok[0].strip() + '|||' + tok[1].strip() + '|||'
                        + entities[entity_id].strip() + '|||' + tok[2].strip() + '\n')
                entity_id = entity_id + 1
    #8.在训练数据中抽取测试数据
    def get_test_from_train(self):
        f = open('1.txt', 'w', encoding='utf-8')
        count = 0
        with open('C:\\Users\\Lincoln\\Desktop\\1.txt', 'r', encoding='utf-8') as f1:
            for line in f1.readlines():
                count = count + 1
                tok = line.strip().split('|||')
                sub_str,_ = self.lcsubstr(tok[0],tok[1])
                tok[0] = tok[0].replace(sub_str,'').replace('《','').replace('》','')
                print(tok[0])
                import jieba
                new_sen = ' '.join(jieba.cut(tok[0]))
                f.write(new_sen + '|||' + tok[1] + '|||' + tok[2].strip() + '|||' + str(count) + '\n')
    #错误算法
    def get_repeated_number_of_question(self):
        f = open('2.txt', 'w', encoding='utf-8')
        count = 0
        num = 0
        flag = ''
        with open('1.txt', 'r', encoding='utf-8') as f1:
            for line in f1.readlines():
                count = count + 1
                tok = line.strip().split('|||',1)
                if count == 1:
                    flag = tok[0]

                if flag == tok[0].strip():
                    num = num + 1
                    flag = tok[0]
                else:
                    f.write(str(num+1) + '\n')
                    flag = tok[0]
                    num = 0


    #生成最后的提交文件
    def insert_answer_into_testset(self):
        answer_list = []
        first = []
        second = []
        third = []
        with open('答案.txt','r',encoding='utf-8') as f1:
            for line in f1.readlines():
                answer_list.append(line.strip())
        print(len(answer_list))
        with open('nlpcc2018.kbqa.withquestion.test','r',encoding='utf-8') as f2:
            for line in f2.readlines():
               if  'question' in line:
                   first.append(line.strip())
               if  'answer' in line:
                   second.append(line.strip())
               if '=============' in line:
                   third.append(line.strip())
        print(len(first))
        print(len(second))
        print(len(third))
        with open('nlpcc2018.kbqa.withquestion.test', 'w', encoding='utf-8') as f3:
            for i in range(len(first)):
                f3.write(first[i] + '\n')
                f3.write(second[i] + ' ' + str(answer_list[i]) + '\n')
                f3.write(third[i] + '\n')
    #求出准确率
    def get_acc(self):
        predicted_answer = []
        real_answer = []
        count = 0
        f = open('答案不对的集合.txt','w',encoding='utf-8')
        with open('D:\\项目资料\\NLPCC2018\\TASK7_20180527再整理\\生成的数据文件\\答案双向LSTM5迭代12正例不重训.txt',
                  'r', encoding='utf-8') as predicted_answer_file:
            for line in predicted_answer_file:
                predicted_answer.append(line.strip())
        print('候选答案个数:',len(predicted_answer))

        with open('nlpcc2018.kbqa.test.with_answer', 'r', encoding='utf-8') as real_answer_file:
            for line in real_answer_file:
                if 'answer' in line:
                    tok = line.split('>', 1)
                    real_answer.append(tok[1].strip().lower())
        print('真实答案个数:',len(real_answer))

        for i in range(len(real_answer)):
            predicted_answer[i] = predicted_answer[i].replace('#卍#', '·').replace(' ', '')
            max_len = max(len(predicted_answer[i]), len(real_answer[i]))
            lcs_len = self.lcs(predicted_answer[i], real_answer[i])
            if lcs_len / max_len * 1.0 > 0.55:
                count = count + 1
                print('问题No.',i+1)
                print(count,predicted_answer[i])
                print(real_answer[i])
            else:
                f.write('问题No.' + str(i+1) + '\n')
                f.write('预测答案:' + predicted_answer[i] + '\n')
                f.write('正确答案:' + real_answer[i] + '\n')
        print('正确个数',count)
        print('正确率',count / len(real_answer) * 1.0)
        f.close()
    #针对测试集生成小的词典
    def small_dict_generator(self):
        f2 = open('2018训练集小词典.txt','w',encoding='utf-8')
        L = []
        with open('D:\\项目资料\\NLPCC2018\\分词结果和词性标注结果\\2018train新\\NE_result.txt','r',encoding='utf-8') as f1:
            for line in f1.readlines():
                tok = line.strip().split()
                for i in range(len(tok)):
                    L.append(tok[i])
        print(len(L))
        L = list(set(L))
        L.sort(key=lambda x:len(x), reverse=True)
        print(len(L))
        for i in range(len(L)):
            if len(L[i]) >=2:
                f2.write(L[i] + '\n')
        f2.close()
    #处理未登录词
    def avg_all_vector(self):
        import numpy as np
        from decimal import Decimal
        vec_all = []
        count = 1
        f2 = open('未登录词词向量.vec','w',encoding='utf-8')
        with open('D:\\BaiduYunDownload\\10G训练好的词向量\\newsblogbbs.vec','r',encoding='utf-8') as f1:
            for line in f1.readlines():
                if count >=2:
                    name,vec = line.split(' ',1)
                    print(count)
                    # print(type(name))
                    # print(type(vec))
                    temp = np.fromstring(vec,sep=' ')
                    # print(type(temp))
                    vec_all.append(temp)
                count = count + 1
            avg = list(np.mean(vec_all,axis=0))
            #print(type(avg))
            for i in range(len(avg)):
                avg[i] = Decimal(avg[i])
                avg[i] = round(avg[i],6)
                f2.write(str(avg[i]) + '\n')
            print(avg)
            f2.close()

    def get_answer_by_LCS(self):
        number = []
        score = []
        all_answer = []
        f = open('答案.txt','w',encoding='utf-8')
        with open('三元组个数.txt','r',encoding='utf-8') as f1:
            for line in f1.readlines():
                number.append(int(line.strip()))
        with open('候选三元组.txt','r',encoding='utf-8') as f2:
            for i in range(len(number)):
                if number[i] == 0:
                    f.write('找不到三元组啊大哥' + '\n')
                    continue
                for j in range(number[i]):
                    line = f2.readline()
                    question,triple = line.strip().split('|||',1)
                    entity,relation,answer = triple.split('|||')
                    all_answer.append(answer)
                    sub_str,_ = self.lcsubstr(question,relation)
                    score.append(_)
                print(score)
                max_index = score.index(max(score))
                f.write(all_answer[max_index] + '\n')
                score = []
                all_answer = []
dp = Data_Process()

dp.get_acc()
# dp.get_answer_by_LCS()
# dp.get_acc()
# array = []
# array1 = []
# array0 = []
# EXPANSION = 5
# f = open('不保留实体_正例乘5_句子分词_属性分词_后添加实体.txt','w',encoding='utf-8')
# with open('不保留实体_正例乘1_句子分词_属性分词_后添加实体.txt','r',encoding='utf-8') as f1:
#     for line in f1.readlines():
#         line = line.strip()
#         if line.startswith('1'):
#             array1.append(line)
#         if line.startswith('0'):
#             array0.append(line)
# for k in range(EXPANSION):
#     for i in range(len(array1)):
#         array.append(array1[i])
# print(len(array1))
# print(len(array))
# random.shuffle(array0)
# for i in range(EXPANSION * len(array1)):
#     array.append(array0[i])
# random.shuffle(array)
# for i in range(len(array)):
#     f.write(array[i] + '\n')
# print('ok')
# f.close()













