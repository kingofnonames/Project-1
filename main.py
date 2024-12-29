import json
from utils import beam_search
from collections import defaultdict
import dill

if __name__ == "__main__":
    path = r'D:\Tài liệu học đại học\Project1\Project-1\probabilities.dill' 

    with open(path, 'rb') as f:
        states, start_prob, trans_prob, emit_prob = dill.load(f)
    obs = input()
    result = beam_search(obs.split(" "), states, start_prob, trans_prob, emit_prob)
    print("Chuỗi có dấu:", " ".join(result))

#"la mot to chuc hoat dong phi loi nhuan,"