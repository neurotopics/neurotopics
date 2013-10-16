# DocsToVocab.py

import sys
from collections import Counter

class DocsToVocab:

    def __init__(self, full_text_file_name, document_output_file_obj, vocabulary_output_file_obj):

        self.full_text_file_name = full_text_file_name
        self.document_output_file_obj = document_output_file_obj
        self.vocabulary_output_file_obj = vocabulary_output_file_obj

        self.token_list = []
        self.token_dict = {}

    def docs_to_vocab(self):

        full_text_file_obj = open(self.full_text_file_name, 'r')
        for line in full_text_file_obj:
            tokens = line.split()
            for token in tokens:
                lowered_token = token.lower()
                if not self.token_dict.has_key(lowered_token):
                    self.token_list.append(lowered_token)
                    self.token_dict[lowered_token] = len(self.token_list) - 1
                
                
        full_text_file_obj.close()
        full_text_file_obj = open(self.full_text_file_name, 'r')

        for line in full_text_file_obj:
            doc_dict = Counter()
            tokens = line.split()
            for token in tokens:
                lowered_token = token.lower()
                token_id = self.token_dict[lowered_token]
                doc_dict[token_id] += 1
            for k,v in doc_dict.iteritems():
                self.document_output_file_obj.write(str(k) + ':' + str(v) + ' ')
            self.document_output_file_obj.write('\n')

        for i in range(len(self.token_list)):
            self.vocabulary_output_file_obj.write(str(i) + ' ' + str(self.token_list[i]) + '\n')
    


if __name__ == '__main__':
    document_output_file_obj = open(sys.argv[2], 'wb')
    vocabulary_output_file_obj = open(sys.argv[3], 'wb')

    dtv = DocsToVocab(sys.argv[1], document_output_file_obj, vocabulary_output_file_obj)
    dtv.docs_to_vocab()
