package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"

	"github.com/n3integration/classifier/naive"
	"github.com/traininghq/n3integration-classifier-test/pkg/tokenizer"
)

func main() {
	cf := naive.New(naive.Tokenizer(tokenizer.New()))

	trainingTextFile(cf, "舔狗", "data/舔狗日记.txt")
	trainingTextFile(cf, "鸡汤", "data/心灵鸡汤.txt")

	if classification, err := cf.ClassifyString(os.Args[1]); err == nil {
		fmt.Println("分类 => ", classification) // ham
	} else {
		fmt.Println("error: ", err)
	}
}

func trainingTextFile(cf *naive.Classifier, cat, path string) error {
	body, err := ioutil.ReadFile(path)
	if err != nil {
		return err
	}
	lines := strings.Split(string(body), "\n")
	for _, line := range lines {
		if err = cf.TrainString(line, cat); err != nil {
			return err
		}
	}
	return nil
}
