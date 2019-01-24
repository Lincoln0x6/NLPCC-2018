#coding=utf-8
from gensim.models import word2vec
from gensim.models.word2vec import LineSentence

model = word2vec.Word2Vec.load('w2v_chisim.300d.model')

print(model.most_similar('帕尔马足球俱乐部'))
print(model.most_similar('安杰洛'))
L = ['安杰洛·巴隆博','足球','平装','安杰洛·格雷古奇']
result = []
answer = []
for i in range(len(L)):
    result.append(model.similarity(L[i],'安杰洛'))
print(result)
answer.append(L[result.index(max(result))])

print(answer)
print(model['鳞'])



# count = 1
# f_2 = open('kb_info.txt','w',encoding='utf-8')
# with open('nlpcc2018.trainset/knowledge/nlpcc-iccpol-2016.kbqa.kb', 'r',
#           encoding='utf-8') as kb_file:
#     print('...')
#     for line in kb_file.readlines():
#         print(count)
#         count = count + 1
#         tok = line.strip().split('|||',2)
#         for i in range(len(tok)):
#             f_2.write(tok[i] + ' ')
#         f_2.write('\n')
# sentences = []
# f_2 = open('kb_info.txt','r',encoding='utf-8')
# for line in f_2.readlines():
#     sentences.append(line.split(' '))
# f_2.close()
# print(len(sentences))
# print('...')
# model = word2vec.Word2Vec(LineSentence('kb_info.txt'), size=300, window=8, min_count=1, sg=1, workers=4, iter=10)
# print('???')
# model.save('model/kb.w2v.model')
#
# print('!!!')