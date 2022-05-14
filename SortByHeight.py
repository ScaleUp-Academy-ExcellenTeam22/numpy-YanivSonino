import numpy as np

if __name__ == '__main__':

    stud_id = np.array([111, 777, 555, 1234, 123, 4531, 55])
    stud_height = np.array([175, 174, 172, 176, 171, 170, 176])
    stud_sort_by_height = np.lexsort((stud_id, stud_height))

    print(stud_sort_by_height)
    for student in stud_sort_by_height:
        print("id: {}, height: {} cm".format(stud_id[student], stud_height[student]))
