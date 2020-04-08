package tokenizer

import (
	"io"
	"io/ioutil"

	"github.com/go-ego/gse"
)

// Tokenizer ..
type Tokenizer struct {
	gse.Segmenter
}

// New ..
func New() *Tokenizer {
	return &Tokenizer{gse.New()}
}

// Tokenize ..
func (t *Tokenizer) Tokenize(r io.Reader) chan string {
	b, _ := ioutil.ReadAll(r)
	segment := t.Segment(b)
	ch := make(chan string)
	defer func() {
		go func() {
			for _, sg := range segment {
				ch <- sg.Token().Text()
			}
			close(ch)
		}()
	}()
	return ch
}
