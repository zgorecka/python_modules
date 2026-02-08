def helper(days):
    if days > 1:
        result = helper(days - 1)
        print(result)
    else:
        result = 1
    return(days)


def ft_count_harvest_recursive():
    print("Days until harvest: ", end='')
    days = int(input())
    print(helper(days))
