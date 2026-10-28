#validacion


from semana17extra.exercise1 import LinkedList, bubble_sort_linked_list


def validated_bubble_sort(values):
    if len(values) == 0:
        return "Error: The list is empty"

    for v in values:
        if not isinstance(v, (int, float)):
            return "Error: The list contains non-numeric elements"

    ll = LinkedList()
    for v in values:
        ll.append(v)

    bubble_sort_linked_list(ll)
    return ll.to_list()

