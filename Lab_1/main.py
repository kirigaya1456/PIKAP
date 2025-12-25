import sys
import math

def GetCoef(index, msg):
    try:
        coefStr = sys.argv[index]
    except:
        print(msg)
        coefStr = input()
    coef = float(coefStr)
    return coef

def GetRoots(a, b, c):
    result = []
    D = b * b - 4 * a * c

    if D < .0:
        return result
    elif D == 0:
        t = -b / (2.0 * a)

        if t >= 0:
            root = math.sqrt(t)
            result.append(root)
            result.append(-root)

    elif D > 0:
        sqD = math.sqrt(D)

        t1 = (-b + sqD) / (2.0 * a)
        t2 = (-b - sqD) / (2.0 * a)

        if t1 >= 0:
            root1 = math.sqrt(t1)
            result.append(root1)
            result.append(-root1)

        if t2 >= 0 and t2 != t1:
            root2 = math.sqrt(t2)
            result.append(root2)
            result.append(-root2)

    return result

def main():
    a = GetCoef(1, "Введите коэффициент А")
    b = GetCoef(2, "Введите коэффициент B")
    c = GetCoef(3, "Введите коэффициент C")

    if a == 0:
        print("Ошибка: коэффициент A не может быть равен 0 для биквадратного уравнения")
        return

    roots = GetRoots(a, b, c)
    lenRoots = len(roots)

    if lenRoots == 0:
        print("Нет действительных корней")
    elif lenRoots == 2:
        print("Два корня: {} и {}".format(roots[0], roots[1]))
    elif lenRoots == 4:
        print("Четыре корня: {}, {}, {} и {}".format(roots[0], roots[1], roots[2], roots[3]))
    else:
        print("Ошибка")

if __name__ == "__main__":
    main()
