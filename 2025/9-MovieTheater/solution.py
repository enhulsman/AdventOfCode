from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

def solution():
    file = open("input.txt", "r")
    line = file.readline().strip()

    points: list[Point] = []

    while line:
        split = line.split(',')
        points.append(Point(int(split[0]), int(split[1])))
        line = file.readline().strip()

    def area(p1: Point, p2: Point):
        return (abs(p2.x - p1.x)+1) * (abs(p2.y - p1.y)+1)

    def part1():
        largest_area = 0
        for i, p1 in enumerate(points):
            for p2 in points[i+1:]:
                if area(p1, p2) > largest_area:
                    largest_area = area(p1, p2)
        print(largest_area)
        # Answ1: 4761598821 -- too low
        # Answ2: 4761736832 -- correct!

    def check_inside_tiles(polygon: Polygon, p1: Point, p2: Point):
        rectangle_coords = [
            (min(p1.x, p2.x), min(p1.y, p2.y)), 
            (max(p1.x, p2.x), min(p1.y, p2.y)), 
            (max(p1.x, p2.x), max(p1.y, p2.y)),
            (min(p1.x, p2.x), max(p1.y, p2.y)),
        ]

        rectangle = Polygon(rectangle_coords)
        return polygon.covers(rectangle)

    def part2():
        polygon = Polygon([(p.x, p.y) for p in points])
        largest_area = 0
        for i, p1 in enumerate(points):
            for p2 in points[i+1:]:
                if area(p1, p2) > largest_area and check_inside_tiles(polygon, p1, p2):
                    largest_area = area(p1, p2)
        print(largest_area)

    part1()
    part2()

if __name__ == '__main__':
    solution()
