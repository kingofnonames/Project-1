import json
from utils import beam_search, split_into_sentences, merge_sentences
from collections import defaultdict
import dill
if __name__ == "__main__":
    path = r'D:\Tài liệu học đại học\Project1\Project-1\probabilities1a.dill' 

    with open(path, 'rb') as f:
        states, start_prob, trans_prob, emit_prob = dill.load(f)
    obs = input()
    corpus = split_into_sentences(obs)
    output = []
    for sentence in corpus:
        result = beam_search(sentence.split(" "), states, start_prob, trans_prob, emit_prob)
        output.append(" ".join(result))
    print("Chuỗi có dấu:", merge_sentences(output))

#"la mot to chuc hoat dong phi loi nhuan,"
#Tram nam trong coi nguoi ta. Chu tai chu menh kheo la ghet nhau
#Chuc mung nam moi
#Nhung ngon ngu nay co chung mot so tu vung can ban. Thi du, tu "tay" trong tieng Viet tuong duong trong tieng Muong la "thay", trong tieng Khmer la "day" va trong tieng Mon la "tai".