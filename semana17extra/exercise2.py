#pasos



from semana16extras.Exercise2 import LinkedList


def bubble_sort_steps(ll):
    if ll.head is None:
        return ll, 0, 0

    iterations = 0
    swaps = 0
    swapped = True

    while swapped:
        swapped = False
        iterations += 1
        current = ll.head
        prev = None

        while current is not None and current.next is not None:
            nxt = current.next
            if current.value > nxt.value:
                swapped = True
                swaps += 1
                current.next = nxt.next
                nxt.next = current
                if prev is None:
                    ll.head = nxt
                else:
                    prev.next = nxt
                prev = nxt
            else:
                prev = current
                current = current.next

    return ll, iterations, swaps




