def groups_of_3(lst):
    group = list()
    for idx in range(0,len(lst),3):
        group.append(lst[idx:idx+3])
    return group


    """start_idx = (group_num + 1)*3
    return group[start_idx:start_idx + 3]"""
