def area(sideA, sideB, sideC):
    p = (sideA + sideB + sideC) / 2
    return (p * (p - sideA) * (p - sideB) * (p - sideC)) ** 0.5


def side_2d(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5


def is_triangle_exists(sideA, sideB, sideC):
    return sideA < sideB + sideC and sideB < sideA + sideC and sideC < sideB + sideA


def collinear_2d(point1, point2, point3):
    x1, y1 = point2[0] - point1[0], point2[1] - point1[1]
    x2, y2 = point3[0] - point1[0], point3[1] - point1[1]
    return abs(x1 * y2 - x2 * y1) < 1e-12


def find_triangle_with_max_area(points):
    max_area = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            for k in range(j + 1, len(points)):
                point1 = points[i]
                point2 = points[j]
                point3 = points[k]
                if collinear_2d(point1, point2, point3):
                    print(f"Vertices {point1, point2, point3} are collinear")
                    continue
                sideA = side_2d(point1, point2)
                sideB = side_2d(point2, point3)
                sideC = side_2d(point1, point3)
                if not is_triangle_exists(sideA, sideB, sideC):
                    continue
                current_area = area(sideA, sideB, sideC)
                if current_area > max_area:
                    max_area = current_area
    return max_area


if __name__ == '__main__':
    print(find_triangle_with_max_area([[1, 2], [1, 3], [2, 4]]))
