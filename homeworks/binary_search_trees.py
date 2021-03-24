from bintrees import BinaryTree
def find_number_in_tree(file_name:str)->str:
    tree = BinaryTree()
    with open(file_name) as f:
        file = f.readlines()
    result =[]
    for i in file[1::]:
        if i.rstrip('\n') not in tree:
            tree.insert(i.rstrip('\n'),0)
            result.append('-')
        else:
            result.append('+')
    with open("bintrees.out", "w+") as f:
        for i in result:
           f.write(i+'\n')




print(find_number_in_tree('/home/mukha/PycharmProjects/Algorithm_design_and_analysis/test/2.in'))