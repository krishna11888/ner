import os

class SentenceReader(object):

    def __init__(self, path):
        self._path = path
        self.words = set()
        self.tags =  set()
        self.sentences = []

    def  __iter__(self):
        fd = open(self._path, 'r')
        try:
            for line in fd.readlines():
                line = line.rstrip()
                if '-DOCSTART-' in line:
                    yield None
                elif line == "":
                    # new sentence - emit sentence end and begin
                    yield "</s>"
                    yield "<s>"
                else:
                    fields = line.split()
                    tag = fields[-1]
                    token = fields[:-1]
                    self.words.add(token[0])
                    self.tags.add(tag)
                    token = [token[i] for i in range(0,2)]
                    yield (token, tag)
        finally:
            fd.close()

    def sents(self):
        buf = []
        for token in self:
            if token == "</s>":
                if len(buf) > 0:
                    yield buf
            elif token == "<s>":
                buf = []
            else:
                if token != None:
                    buf.append(token)



sentence_reader = SentenceReader(path="//Users/tejaswi/test/ner/conll2003/train.txt")

for sent in sentence_reader.sents():
    print(sent)