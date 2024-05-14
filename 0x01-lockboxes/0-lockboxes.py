#!/usr/bin/python3
""" Module Doc """


def next_opened_box(opened_box):
    """ Looks for the next opened box
    Args:
        opened_box (dict): Dictionary which contains already opened boxes
    Returns:
        list: List with keys contained in opened box
    """
    for index, box in opened_box.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None


def canUnlockAll(boxes):
    """Check if all boxes can be opened
    Args:
        boxes (list): List which contains all boxes with keys
    Returns:
        bool: True if all boxes can be opened. otherwise, False
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    dict_tmp = {}
    while True:
        if len(dict_tmp) == 0:
            dict_tmp[0] = {
                    'status': 'opened',
                    'keys': boxes[0]
                    }
        keys = next_opened_box(dict_tmp)
        if keys:
            for key in keys:
                try:
                    if dict_tmp.get(key) and dict_tmp.get(key).get('status') \
                            == 'opened/checked':
                        continue
                    dict_tmp[key] = {
                            'status': 'opened',
                            'keys': boxes[key]
                            }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in dict_tmp.values()]:
            continue
        elif len(dict_tmp) == len(boxes):
            break
        else:
            return False

    return len(dict_tmp) == len(boxes)


def main():
    """ Entry Point """
    canUnlockAll([[]])


if __name__ == "__main__":
    main()
