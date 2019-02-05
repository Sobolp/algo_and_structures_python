"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""
import queue


class HuffmanNode(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def __eq__(self, other):
        if isinstance(other, HuffmanNode):
            return 0
        else:
            return 1

    def __lt__(self, other):
        if isinstance(other, HuffmanNode):
            return 0
        else:
            return 1


def getTree(frequencies):
    p = queue.PriorityQueue()
    for item in frequencies:
        p.put(item)

    while p.qsize() > 1:
        left, right = p.get(), p.get()
        node = HuffmanNode(left, right)
        p.put((left[0] + right[0], node))
    return p.get()


def walk_tree(tree, path="", tbl={}):
    if isinstance(tree[1].left[1], HuffmanNode):
        walk_tree(tree[1].left, path + "0", tbl)
    else:
        tbl[tree[1].left[1]] = path + "0"
    if isinstance(tree[1].right[1], HuffmanNode):
        walk_tree(tree[1].right, path + "1", tbl)
    else:
        tbl[tree[1].right[1]] = path + "1"
    return tbl


def getFreq(in_str):
    all_freq = {}
    result = []
    for i in in_str:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    for key, value in all_freq.items():
        temp = (value, key)
        result.append(temp)
    return result

def getEncoded(tbl,in_str):
    result = ""
    for ch in in_str:
        result += tbl[ch]
    return result

in_str = "beep boop beer!"
freq = getFreq(in_str)

print(freq)
tree = getTree(freq)
tbl = {}
walk_tree(tree, "", tbl)
print(tbl)
print(getEncoded(tbl,in_str))
