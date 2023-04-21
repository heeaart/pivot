def quicksort(tab: list, lvl: int = 0) -> list:
    if len(tab) in [0,1]:
        return tab

    pivot = tab[0]

    left_part = [x for x in tab[1:] if x <= pivot]
    right_part = [x for x in tab[1:] if x > pivot]

    return quicksort(left_part, lvl + 1) + [pivot] + quicksort(right_part, lvl + 1)


if __name__ == '__main__':
    tab = ["ala","benek","azymut"]
    tab1= ["ala","azymut","benek"]
    assert quicksort(tab) == tab1
    print(f"sortowanie {quicksort(tab)}")
