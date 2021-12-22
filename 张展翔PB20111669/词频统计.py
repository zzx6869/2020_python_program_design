import string
from matplotlib import pyplot as plt


def process_line(line, hist):
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        # 统一大小写
        word = word.lower()

        hist[word] = hist.get(word, 0) + 1


def process_file(filename):
    hist = {}
    with open(filename, 'r') as f:
        for line in f:
            process_line(line, hist)
    return hist


def most_comon(hist, num):
    """获取前 num 个单词"""
    t = []
    for key, value in hist.items():
        t.append((value, key))
    # 反向排序
    t.sort(reverse=True)
    return t[:num]


def run():
    """主函数"""
    hist = process_file('I have a dream.txt')  # 文件位置
    data = most_comon(hist, 20)
    # 画图
    for word in data:
        plt.bar(word[-1:], word[:1])
    plt.legend()
    plt.xlabel('words')
    plt.ylabel('rate')
    plt.title('I have a dream')
    plt.show()


if __name__ == '__main__':
    run()
