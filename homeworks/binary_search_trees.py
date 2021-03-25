from heapq import heappush, heappop, heapreplace
from typing import List

from bintrees import BinaryTree
from binary_heap import BinaryHeap, MinHeap


def read_data_from_file(file_name:str)->List:
    with open(file_name) as f:
        file = [i.rstrip('\n') for i in f.readlines()]
    return file[1::]
def write_data_to_file(data:List[int],file_name:str):
    with open(file_name, "w+") as f:
        for i in data:
           f.write(str(i)+'\n')


def find_number_in_binary_tree(file_name:str)->str:
    tree = BinaryTree()
    file = read_data_from_file(file_name)
    result =''
    for i in file:
        if i.rstrip('\n') not in tree:
            tree.insert(i.rstrip('\n'),0)
            result+='-'
        else:
            result+='+'
    with open("bintrees.out", "w+") as f:
        for i in result:
           f.write(i+'\n')
    return result
def binary_heap_finding(file_name:str)->List:
    data = read_data_from_file(file_name)
    heap = []
    res = []
    for i in range(len(data)):
        if data[i] == 'GET':
          res.append(max(heap))
          heap.remove(max(heap))
        elif data[i].isdigit():
            heappush(heap,int(data[i]))
    write_data_to_file(res,'2b_h.out')
    return heap

print(binary_heap_finding('/home/mukha/PycharmProjects/Algorithm_design_and_analysis/test/2.in'))


