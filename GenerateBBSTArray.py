def GenerateBBSTArray(a):
    a.sort()
    abst = [None] * len(a)
    start = 0

    def sort_for_bbst(a_bst, start_index, list_to_sort):
        middle = len(list_to_sort) // 2
        a_bst[start_index] = list_to_sort[middle]
        if len(list_to_sort) == 1:
            return
        start_left = start_index * 2 + 1
        start_right = start_index * 2 + 2
        sort_for_bbst(a_bst, start_left, list_to_sort[:middle])
        sort_for_bbst(a_bst, start_right, list_to_sort[(middle + 1):])
    sort_for_bbst(abst, start, a)
    return abst
