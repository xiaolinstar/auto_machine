import argparse


def get_data_from_file(file_name):
    try:
        with open(file_name, encoding='utf-8') as f:
            lines = f.readlines()
            return [line[:-1] for line in lines[1:]]
    except IOError as e:
        print('读取文件异常', e)


def is_final(state):
    return '*' in state


def is_start(state):
    return '#' in state


def get_state_set(lines):
    start_set, final_set = list(), list()
    transfers = dict()
    for line in lines:
        states = line.split()
        start = states[0]
        if is_start(start):
            start_set.append(start.replace('#', '').replace('*', ''))
        if is_final(start):
            final_set.append(start.replace('#', '').replace('*', ''))
        start = start.replace('#', '').replace('*', '')
        zero = states[1]
        one = states[2]
        transfers[start] = (zero, one)
    return start_set, final_set, transfers


def grade(start_set, final_set, transfers, inputs):
    if len(start_set) != 1:
        return '开始状态不唯一'
    curr = start_set[0]
    for sentence in inputs:
        for word in sentence:
            if curr == 'N':
                return '错误，自动机卡住，当前状态为'+curr+'输入字符'+word+'\n所在句子为：'+sentence
            if word == '0':
                curr = transfers[curr][0]
            elif word == '1':
                curr = transfers[curr][1]
            else:
                return '错误，读入的字符串中包含非0非1的字符：'+word
        # print(curr)
        if curr not in final_set:
            return '错误，字符串读完，未停止在终止状态，当前状态为:'+curr+'\n所在句子为：'+sentence
    return '成功'


def add_parameters():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ans_file', type=str, default='ans.txt')
    parser.add_argument('--sentences_file', type=str, default='sentences.txt')
    return parser.parse_args()


if __name__ == '__main__':
    args = add_parameters()
    ans_file = args.ans_file
    sentences_file = args.sentences_file
    contents = get_data_from_file(ans_file)
    sentences = get_data_from_file(sentences_file)
    S, F, table = get_state_set(contents)
    ans = grade(S, F, table, sentences)
    print(ans)