def unique_to_both_lists(list1, list2):
    set1, set2 = set(list1), set(list2)
    # Найдем элементы, которые уникальны для обоих множеств
    unique_elements = (set1 - set2) | (set2 - set1)
    # Преобразуем результат обратно в список и возвращаем его
    return list(unique_elements)
