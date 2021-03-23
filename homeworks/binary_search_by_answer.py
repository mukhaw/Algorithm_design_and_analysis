from typing import List
def get_length_of_section(file_name:str)->int:
    with open(file_name) as f:
        file = f.readlines()
    points =[int(i.rstrip('\n')) for i in file[2::]]
    number_of_section = int(file[1].rstrip('\n'))
    if number_of_section>=len(points):
        return 0
    min = 0
    max = points[-1]-points[0]
    while min!=max:
        mid = min+(max-min)//2
        if (mid == max or mid == min):
            return max
        if(check_is_length_right(points,number_of_section,mid)):

            max = mid
        else: min = mid
    return max
def check_is_length_right(points:List[int],number_of_section:int,length:int)->bool:
    end = points[0]+length
    number_of_section-= 1
    for i in points:
        if end < i:
            number_of_section -= 1
            end = i+length
            if number_of_section<0:
                return False
    return True
