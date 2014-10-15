from math import pow, sqrt
from traffic_heatmap.util import number


def generate_grid(center, density, radius):
    """
    Generate a list of x, y coordinates confined to the inside of a circle with
    specified center point and radius. The density is how many points per
    single coordinate unit
    :param center: The (x, y) center of the circle
    :param density: How many points per x/y unit
    :param radius: The radius of the circle
    :return: List of (x, y) point grid inside the circle
    """
    # Boundaries
    top = center[1] + radius
    bottom = center[1] - radius
    left = center[0] - radius
    right = center[0] + radius

    # Get Points
    for y in number.drange(bottom, top, 1/density):
        for x in number.drange(left, right, 1/density):
            if point_in_circle(center, radius, (x, y)):
                yield (x, y)


def point_in_circle(center, radius, point):
    """
    Determine if a specified point is inside of a circle with a specified
    center point and radius.
    :param center: The (x, y) center of the circle
    :param radius: The radius of the circle
    :param point: The (x, y) point in question
    :return: True or False
    """
    # Use pythagorean theorem to see if the hypotenuse is less than the radius
    a = abs(center[0] - point[0])
    b = abs(center[1] - point[1])
    return sqrt(pow(a, 2) + pow(b, 2)) <= radius
