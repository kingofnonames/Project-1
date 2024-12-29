import json
from beam_search import beam_search
from collections import defaultdict
import dill
# Đọc dữ liệu từ tệp JSON

if __name__ == "__main__":
    # path = r'D:\Tài liệu học đại học\Project1\Project-1\probabilities.json' 
    path = r'D:\Tài liệu học đại học\Project1\Project-1\probabilities.dill' 
    # with open(path, 'r', encoding='utf-8') as file:
    #     probabilities = json.load(file)

    # Lấy các dictionary từ dữ liệu đã đọc
    # start_prob = probabilities['start_prob']
    # trans_prob = probabilities['trans_prob']
    # emit_prob = probabilities['emit_prob']
    with open(path, 'rb') as f:
        start_prob, trans_prob, emit_prob = dill.load(f)
    states = defaultdict(list)
    print(start_prob)
    obs = input()
    print(obs)
    result = beam_search(obs.split(" "), states, start_prob, trans_prob, emit_prob)
    print("Chuỗi có dấu:", " ".join(result))

#"la mot to chuc hoat dong phi loi nhuan,"