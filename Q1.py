# function definition
def str_comp(str1, str2):
    # fetching lengths
    l1 = len(str1)
    l2 = len(str2)

    # comparing lengths
    if l1 == l2:
        return True
    else:
        return False


print(str_comp("projects", "computer"))
