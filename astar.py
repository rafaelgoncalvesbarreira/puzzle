import heapq
from path_item import PathItem

def find_by_less_cost(list, target):
    best = 999999
    best_item = None
    for item in list:
        cost = item.calculate_cost(target)
        if cost < best:
            best = cost
            best_item = item

    return best_item

def find_in_list(search, list):
    for item in list:
        if item.board == search.board:
            return item
    return None

def resolve(start, target):
    """ doc """
    open_list = []
    close_list = []
    heapq.heappush(open_list, (0, start))

    #current = find_by_less_cost(open_list, target)
    while len(open_list) > 0:
        current = open_list[0][1]
        if current.board == target.board:
            break
        heapq.heappop(open_list)
        close_list.append(current)

        nodes = current.get_adjacent()
        for node in nodes:
            if node.board not in [x.board for x in close_list]:
                if node.board in [item[1].board for item in open_list]:
                    existent_tupla = [item for item in open_list if item[1].board == node.board][0]
                    existent = existent_tupla[1]
                    if existent.calc_G() < node.calc_G():
                        existent.parent = current
                        old_cost = existent.costF
                        existent.recalculate_cost(target)
                        #open_list[old_cost].remove(existent)
                        open_list.remove(existent_tupla)
                        heapq.heappush(open_list, (existent.costF, existent))
                else:
                    new_item = PathItem(node.board, current)
                    new_item.recalculate_cost(target)
                    heapq.heappush(open_list, (new_item.costF, new_item))
#end of while
    if current.board == target.board:
        return_list = []
        item = current
        while item is not None:
            return_list.insert(0, item)
            item = item.parent
        return return_list
    else:
        return []
