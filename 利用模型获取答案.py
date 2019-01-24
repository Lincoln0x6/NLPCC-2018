from keras.models import Model, load_model
import pickle
import linecache
import os

GENERATED_DIR = 'C:\\Users\\Lincoln\Desktop\\TASK7_20180501重新整理\\TASK7_20180501重新整理\\生成的数据文件'

CANDIDATE_DIR = 'C:\\Users\\Lincoln\Desktop\\TASK7_20180501重新整理\\TASK7_20180501重新整理\\测试数据'

MODEL_NAME = 'D:\\项目资料\\NLPCC2018\\模型\\正确模型\\model_乱序25万数据去实体不去停用词迭代5次\\model_25万数据去实体不去停用词迭代5次\\model_25万数据去实体不去停用词迭代5次.h5'

with open(os.path.join(GENERATED_DIR, 'candidate_left'), 'rb') as file:
    candidate_left = pickle.load(file)

with open(os.path.join(GENERATED_DIR, 'candidate_right'), 'rb') as file:
    candidate_right = pickle.load(file)

with open(os.path.join(GENERATED_DIR, 'candidate_answers'), 'rb') as file:
    candidate_answers = pickle.load(file)

model = load_model(MODEL_NAME)

fp = open(os.path.join(CANDIDATE_DIR, 'ques_entity_num.txt'), encoding='utf-8')
# fp = open(os.path.join(CANDIDATE_DIR, 'candidate_number.txt'),  encoding = 'utf-8')

number_of_problems = []

for i in fp:
    i = i.encode('utf-8').decode('utf-8-sig')
    number_of_problems.append(int(i))

f1 = open(os.path.join(GENERATED_DIR, '答案.txt'), 'w+', encoding="utf-8")

begin = 0

current_left = []
current_right = []
current_answers = []

f2 = open(os.path.join(GENERATED_DIR, '相似度数值.txt'), 'w+', encoding="utf-8")

question_number = 1

for i in number_of_problems:

    # print(i)

    end = begin + i

    if begin == end:
        f1.write('抱歉\n')
        continue

    print(begin, end, i)

    current_left = candidate_left[begin: end]
    current_right = candidate_right[begin: end]
    current_answers = candidate_answers[begin: end]

    # for k in range(i):
    # print(current_left[k], ',', current_right[k], ',', current_answers[k])

    result = model.predict([current_left, current_right], batch_size=32)

    result = [k for row in result for k in row]

    maxid = result.index(max(result))

    # print(begin, end, i, ':', maxid)

    # print(current_answers[maxid])

    f1.write(current_answers[maxid])
    f1.write('\n')

    f2.write('question : ')
    f2.write(str(question_number))
    f2.write(' max_id : ')
    f2.write(str(maxid))
    f2.write('\n')
    for k in result:
        f2.write(str(k) + '\n')
    f2.write('\n')

    begin = end

    question_number += 1

    # os.system('pause')

fp.close()