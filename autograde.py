import argparse


def get_data_from_file(file_name):
    try:
        with open(file_name, encoding='utf-8') as f:
            lines = f.readlines()
            while lines[-1] == '\n':
                lines = lines[:-1]
            if lines[-1][-1] != '\n':
                lines[-1][-1] += '\n'
            return lines[0], [line[:-1] for line in lines[1:]]
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
    res, f = list(), list()
    for sentence in inputs:
        curr = start_set[0]
        for word in sentence:
            if curr == 'N':
                res.append('不接收，自动机卡住，当前状态为' + curr + '输入字符' + word + '\n所在句子为：' + sentence)
                f.append(False)
                break
            if word == '0':
                curr = transfers[curr][0]
            elif word == '1':
                curr = transfers[curr][1]
            else:
                res.append('不接收，读入的字符串中包含非0非1的字符：' + word)
                f.append(False)
                break

        if curr not in final_set:
            res.append('不接收，字符串读完，未停止在终止状态，当前状态为:' + curr + ' 所在句子为：' + sentence)
            f.append(False)
        else:
            res.append('句子{}成功接收！'.format(sentence))
            f.append(True)
    return res, f


def mini(num, states_len):
    return num == states_len


def add_parameters():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--ans_file', type=str, default='ans.txt')
    parser.add_argument('-s', '--sentences_file', type=str, default='sentences.txt')
    parser.add_argument('-d', '--debug', type=bool, default=False)
    parser.add_argument('-e', '--eval', type=bool, default=True)
    return parser.parse_args()


def print_results(res):
    for item in res:
        print(item)


def grade_scores(f):
    standard = [True] * 10 + [False] * 10
    score = 0
    fail_info = list()
    for i in range(20):
        if f[i] == standard[i]:
            score += 1
        else:
            fail_info.append(i)
    return score, fail_info


if __name__ == '__main__':
    args = add_parameters()
    ans_file = args.ans_file
    sentences_file = args.sentences_file
    _, contents = get_data_from_file(ans_file)
    states_num, sentences = get_data_from_file(sentences_file)
    states_num = int(states_num[:-1])

    S, F, table = get_state_set(contents)
    ans, f_ans = grade(S, F, table, sentences)
    if args.debug:
        print_results(ans)

    # 评分系统
    if args.eval:
        print(f_ans)
        # scores, error_info = grade_scores(f_ans)
    # print('End!')
    # if mini(states_num, len(contents)):
    #     print('√该自动机是极小的')
    # else:
    #     print('×自动机的状态不是极小的')
