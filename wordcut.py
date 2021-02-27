import jieba
import json

def write_to_file(words_dict):
    json_dict = dict()
    data = list()
    for item in words_dict:
        # print(item)
        if item[1] < 30:
            break
        data.append({"name": item[0], "value": item[1]})
    json_dict["data"] = data
    with open('comments.json', 'a', encoding='utf-8') as file:
        json.dump(json_dict, file, ensure_ascii=False)
        print("DONE PROCESS SUCCESSFULLY!")
def word_counter(read_buff):
    words_dict = dict()
    for word in read_buff:
        words_dict[word] = words_dict.get(word, 0) + 1
    return sorted(words_dict.items(), key=lambda item: item[1], reverse=True)

def breakup_sentence(sentence, read_buff):
    msg_list = jieba.cut(sentence)
    for msg in msg_list:
        if len(msg) > 1:
            read_buff.append(msg)

def load_data(read_buff):
    with open('comments.txt', 'r', encoding='utf-8') as file:
        items = file.readlines()
        for item in items:
            breakup_sentence(item, read_buff)

def main():
    read_buff = list()
    load_data(read_buff)
    words_dict = word_counter(read_buff)
    write_to_file(words_dict)

if __name__ == '__main__':
    main()
