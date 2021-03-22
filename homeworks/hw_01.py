from typing import List,Tuple
import string
def get_data(file_name: str)-> Tuple[List[int], List[int]]:
      with open(file_name) as f:
        file = f.readlines()
      data = [int(i) for i in file[1].rstrip('\n').split()]
      number_for_search =[int(i.rstrip('\n')) for i in file[3::]]
      return data,number_for_search



def binary_search(a:List[int],value: int)-> int:
  left = 0
  right = len(a)
  found = False
  while left<=right and not found:
    middle = (left+right)//2
    if (a[left]<value and a[right-1]<value) or (a[left]>value and a[right-1]>value):
      return -1
      break
    if a[middle] == value:
      found = True
      return middle
      break
    elif value<a[middle]:
      right = middle
    else:
      left = middle
def load_binary_search_with_data(file_name:str)->List[int]:
  data = get_data(file_name)
  result = []
  for i in data[1]:
    result.append(binary_search(data[0],i))
  return result