def is_list_mirror_inverse(list1, list2):
    if len(list1) != len(list2):
        return False
    length = len(list1)
    for index in range(length):
        if list1[index] != list2[length-(index+1)] :
            return False
        return True