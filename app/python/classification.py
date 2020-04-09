import logging
import fasttext
import pandas as pd
import codecs


class Classification(object):

    classifier = object

    def train(self, filePath="./data/raw.train"):
        logging.basicConfig(
            format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
        # 训练
        self.classifier = fasttext.train_supervised(
            filePath, wordNgrams=3)  # bucket=2000000

    def test(self, filePath="./data/raw.test"):
        # 读取验证集
        with open(filePath, 'r', encoding='utf-8') as infile:
            for line in infile:
                line = line.replace("\n", "")
                logging.info(line)
                # 预测结果
                logging.info(self.classifier.predict(line, k=2))
