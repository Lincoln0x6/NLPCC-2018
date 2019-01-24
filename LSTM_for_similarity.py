#训练数据及校验数据来自gold_entity_relation.txt
#比第三版多了一层卷积、dropout和池化
'''
train score: 0.269994482027373
train accuracy: 0.919980664715719
Test score: 0.27892340698986134
Test accuracy: 0.9173881233995854
lstm 数据集为20万
train score: 0.5044129102481011
train accuracy: 0.9449257951744956
Test score: 0.5678149813823338
Test accuracy: 0.933822557187878
'''

from keras.layers import Input, LSTM, Dense, merge, Conv1D, MaxPooling1D, Flatten, Embedding, Dropout,SpatialDropout1D
from keras.models import Model
from keras.layers.merge import Concatenate
from keras import regularizers

import numpy as np
import pickle
from keras.utils.np_utils import to_categorical
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import pdb
from keras import backend as K
'''
import tensorflow as tf  # tensor
from theano import function  # function
from keras.engine.topology import Layer
'''
import os
import jieba

#jieba.load_userdict("./science")

#input_train = sys.argv[1]  # s_label_zfli

BASE_DIR = '.'
GLOVE_DIR = 'D:\\BaiduYunDownload\\10G训练好的词向量'  # 预训练词向量的地址
# GLOVE_DIR1 = 'D:\\BaiduYunDownload\\10G训练好的词向量'  # 预训练词向量的地址
#GLOVE_DIR2 = 'D:\\项目资料\\NLPCC2018\\打分模型训练数据\\答案唯一的测试数据(有实体或无实体)-去停用词后\\答案唯一的测试数据(有实体或无实体)' #训练文件
#GLOVE_DIR2 = 'D:\\项目资料\\NLPCC2018\\打分模型训练数据\\所有答案的测试数据(有实体或无实体)-去停用词后'
MAX_SEQUENCE_LENGTH = 200
MAX_NB_WORDS = 200000
EMBEDDING_DIM = 200
VALIDATION_SPLIT = 0.3

print('Indexing word vectors.')

embeddings_index = {}

f = open(os.path.join(GLOVE_DIR, 'newsblogbbs.vec'), encoding='utf-8')  # 预训练的词向量，可使用Word2vec自行训练，下面几行就是依次读入词向量
f2 = open(os.path.join('打乱顺序后的25万去实体去停用词.txt'), encoding='utf-8')
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    embeddings_index[word] = coefs
    
f.close()

print('Found %s word vectors.' % len(embeddings_index))

print('Processing text dataset')


texts = []  # list of text samples

labels_index = {}  # dictionary mapping label name to numeric id

labels = []  # list of label ids

train_left = []
train_right = []

# 下面几行是读入训练集，训练集每行格式：相似标签(1/0)|||问句|||实体 属性

for line in f2:  # train，读入训练集
    line = line.strip()
    line = line.split('|||')

    if len(line) < 3:
        continue

    label_id = line[0]
    label_id = label_id.encode('utf-8').decode('utf-8-sig') #针对文件首字符无法正确编码问题
    question = line[1]
    title = line[2]
    
    seg_list_question = jieba.cut(question)
    seg_list_title = jieba.cut(title)
    
    text_left = (' '.join(seg_list_question)).strip ()
    text_right = (' '.join(seg_list_title)).strip ()
    
    # print text_left
    # print text_right

    texts.append(text_left)
    texts.append(text_right)
    labels.append(float(label_id))
    
    train_left.append(text_left)
    train_right.append(text_right)
    

print ('Found %s left.' % len (train_left))
print ('Found %s right.' % len (train_right))
print ('Found %s labels.' % len (labels))

# finally, vectorize the text samples into a 2D integer tensor
tokenizer = Tokenizer(num_words=MAX_NB_WORDS) 
tokenizer.fit_on_texts(texts) #生成token词典

sequences_left = tokenizer.texts_to_sequences(train_left) #转换为word下标的向量形式
sequences_right = tokenizer.texts_to_sequences(train_right)

# for item  in sequences_left:
#    print item

word_index = tokenizer.word_index #dict，保存所有word及对应的编号id，从1开始,格式为：{词：编号，词：编号,......}
print ('Found %s unique tokens.' % len (word_index))


#pad_sequences: 转化为2D numpy array
#padding/truncating：‘pre’或‘post’，确定当需要补/截断0时，在序列的起始还是结尾补/截断
data_left = pad_sequences(sequences_left, maxlen=MAX_SEQUENCE_LENGTH, padding='pre', truncating='post')
data_right = pad_sequences(sequences_right, maxlen=MAX_SEQUENCE_LENGTH, truncating='post')

labels = np.array(labels) #节省空间？



fp = open('data_left_1.txt','wb')
print('1........')

pickle.dump(data_left, fp)

fp.close()

fp = open('data_right_1.txt','wb')
print('2........')

pickle.dump(data_right, fp)

fp.close()



# split the data into a training set and a validation set
indices = np.arange(data_left.shape[0])
np.random.shuffle(indices)

data_left = data_left[indices]
data_right = data_right[indices]

labels = labels[indices]
nb_validation_samples = int(VALIDATION_SPLIT * data_left.shape[0])  # create val and sp, VALIDATION_SPLIT=0.3

input_train_left = data_left[:-nb_validation_samples]
input_train_right = data_right[:-nb_validation_samples]

val_left = data_left[-nb_validation_samples:]
val_right = data_right[-nb_validation_samples:]

labels_train = labels[:-nb_validation_samples]
labels_val = labels[-nb_validation_samples:]

print ('Preparing embedding matrix.')

# prepare embedding matrix
nb_words = min(MAX_NB_WORDS, len(word_index))

# print type(word_index)
# for  item in word_index:
#     print item + '\t' + str(word_index[item])

embedding_matrix = np.zeros((nb_words + 1, EMBEDDING_DIM)) #EMBEDDING_DIM=200

for word, i in word_index.items(): #word_index，dict保存所有word及对应的编号id
    if i > MAX_NB_WORDS:
        continue
    
    embedding_vector = embeddings_index.get(word) 
    
    if embedding_vector is not None:
        # words not found in embedding index will be all-zeros.
        embedding_matrix[i] = embedding_vector  # word_index to word_embedding_vector ,<20000(nb_words)
# load pre-trained word embeddings into an Embedding layer
# note that we set trainable = False so as to keep the embeddings fixed

''''' 
embedding_layer = Embedding(nb_words + 1, 
                            EMBEDDING_DIM, 
                            input_length=MAX_SEQUENCE_LENGTH, 
                            weights=[embedding_matrix], 
                            trainable=True) 
'''

print ('Training model.')

# train a 1D convnet with global maxpoolinnb_wordsg
# left model


''''' 
data_1 = np.random.randint(low = 0, high = 200, size = (500, 140)) 
data_2 = np.random.randint(low = 0 ,high = 200, size = (500, 140)) 
labels = np.random.randint(low=0, high=2, size=(500, 1)) 
#labels = to_categorical(labels, 10) # to one-hot 
'''

tweet_a = Input(shape=(MAX_SEQUENCE_LENGTH,)) #张量
tweet_b = Input(shape=(MAX_SEQUENCE_LENGTH,))

tweet_input = Input(shape=(MAX_SEQUENCE_LENGTH,))

# 下面这些行是神经网络构造的内容，可参见上面的网络设计图

embedding_layer = Embedding(nb_words + 1, EMBEDDING_DIM, input_length=MAX_SEQUENCE_LENGTH, weights=[embedding_matrix],
                           trainable=True)(tweet_input)
dropout_1 = SpatialDropout1D(0.2)(embedding_layer)
#dropout_1 = Dropout(0.2)(embedding_layer)
out_1 = LSTM(128, activation='tanh', dropout=0.2, recurrent_dropout=0.2)(embedding_layer)
#out_1 = Bidirectional(LSTM(128, activation='tanh', dropout=0.2, recurrent_dropout=0.2))(embedding_layer)
#conv1 = Conv1D(128, 3, activation='tanh') (embedding_layer)
#drop_1 = Dropout (0.2) (conv1)
#max_1 = MaxPooling1D (3) (drop_1)

#conv2 = Conv1D (128, 3, activation='tanh') (max_1)
#drop_2 = Dropout (0.2) (conv2)
#max_2 = MaxPooling1D (3) (drop_2)
# conv2 = Conv1D(128, 3, activation='tanh')(max_1)
# max_2 = MaxPooling1D(3)(conv2)

#out_1 = Flatten ()(max_2)
#out_1 = Flatten ()(max_1)
#out_1 = LSTM(128)(max_1)

model_encode = Model(tweet_input, out_1)  # 500(examples) * 5888
encoded_a = model_encode (tweet_a)
encoded_b = model_encode (tweet_b)

merged_vector = Concatenate()([encoded_a, encoded_b])  # good
dense_1 = Dense (128, activation='relu') (merged_vector)
dense_2 = Dense (128, activation='relu') (dense_1)
dense_3 = Dense (128, activation='relu') (dense_2)

predictions = Dense(1, activation='sigmoid') (dense_3)
#predictions = Dense(len(labels_index), activation='softmax')(merged_vector)

model = Model(inputs=[tweet_a, tweet_b], outputs=predictions)
#model.compile (optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])

model.compile (optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])

# 下面是训练程序
model.fit([input_train_left, input_train_right], labels_train, epochs=5)

#print ('train score:', score[0])  # 训练集中的loss
#print ('train accuracy:', score[1])  # 训练集中的准确率

'''
json_string=model.to_json ()  # json_string = model.get_config()
open ('my_model_architecture.json', 'w').write (json_string)

model.save_weights ('my_model_weights.h5')
'''

model.save('model_25万数据去实体去停用词迭代5次.h5')


result = model.predict([val_left, val_right], batch_size=1)

fp = open('model_6_output.txt', 'w+')
for i in result:
    fp.write(str(i))

fp.close()


# 下面是训练得到的神经网络进行评估
score = model.evaluate ([input_train_left, input_train_right], labels_train, verbose=0)
print ('train score:', score[0])  # 训练集中的loss
print ('train accuracy:', score[1])  # 训练集中的准确率
score = model.evaluate ([val_left, val_right], labels_val, verbose=0)
print ('Test score:', score[0])  # 测试集中的loss
print ('Test accuracy:', score[1])  # 测试集中的准确率


