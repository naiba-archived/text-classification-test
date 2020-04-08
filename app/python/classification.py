import logging
import fasttext
import pandas as pd
import codecs

basedir = './data/'
logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# 训练
classifier = fasttext.train_supervised(
    basedir + "raw.train", wordNgrams=3)  # bucket=2000000

# 读取验证集
with open(basedir + 'raw.test', 'r', encoding='utf-8') as infile:
    for line in infile:
        line = line.replace("\n", "")
        logging.info(line)
        # 预测结果
        logging.info(classifier.predict(line, k=2))
