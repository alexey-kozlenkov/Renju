__author__ = 'Alexey'


def get_square_center(x, y):
    left_up_corner = (x - x % 40, y - y % 40)
    result = (left_up_corner[0] + 20, left_up_corner[1] + 20)
    return result
