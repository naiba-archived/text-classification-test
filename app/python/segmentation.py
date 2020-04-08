import sys
import jieba
import codecs
import math
import random


stopwords_set = set()
basedir = './data/'

# 分词结果文件
train_file = codecs.open(basedir + "raw-"+sys.argv[2]+".train", 'w', 'utf-8')
test_file = codecs.open(basedir + "raw-"+sys.argv[2]+".test", 'w', 'utf-8')

# 停用词文件
with open(basedir + 'hit_stopwords.txt', 'r', encoding='utf-8') as infile:
    for line in infile:
        stopwords_set.add(line.strip())

index = 1
with open(sys.argv[1], 'r', encoding='utf-8') as infile:
    for line in infile:
        # 结巴分词
        seg_text = jieba.cut(line.replace("\t", " ").replace("\n", " "))
        outline = " ".join(seg_text)
        outline = " ".join(outline.split())

        # 去停用词与HTML标签
        outline_list = outline.split(" ")
        outline_list_filter = [
            item for item in outline_list if item not in stopwords_set]
        outline = " ".join(outline_list_filter)

        outline = "__label__"+sys.argv[2]+" " + outline + "\n"

        if index % 5 == 0:
            test_file.write(outline)
            test_file.flush()
        else:
            train_file.write(outline)
            train_file.flush()

        index = index+1

train_file.close()
test_file.close()
