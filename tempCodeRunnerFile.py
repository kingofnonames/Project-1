import json
from utils import beam_search, split_into_sentences, merge_sentences
from collections import defaultdict
import dill
if __name__ == "__main__":
    path = r'D:\Tài liệu học đại học\Project1\Project-1\probabilities.dill' 

    with open(path, 'rb') as f:
        states, start_prob, trans_prob, emit_prob = dill.load(f)
    obs = input()
    corpus = split_into_sentences(obs)
    output = []
    print(corpus)
    for sentence in corpus:
        result = beam_search(obs.split(" "), states, start_prob, trans_prob, emit_prob)
        output.append(" ".join(result))
    print(output)
    #print("Chuỗi có dấu:", merge_sentences(output))

#"la mot to chuc hoat dong phi loi nhuan,"

#Nhung ngon ngu nay co chung mot so tu vung can ban. Thi du, tu "tay" trong tieng Viet tuong duong trong tieng Muong la "thay", trong tieng Khmer la "day" va trong tieng Mon la "tai".