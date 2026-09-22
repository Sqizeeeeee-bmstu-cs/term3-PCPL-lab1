from typing import List

def solver(a: int, b: int, c: int) -> List[float]:

    d = b ** 2 - 4 * a * c

    if d < 0:
        return []

    res = []

    t1 = (-b + d ** 0.5) / (2 * a)
    
    t2 = (-b - d ** 0.5) / (2 * a)

    if t1 > 0:
        res.append(t1 ** 0.5)
        res.append(-(t1 ** 0.5))
    elif t1 == 0:
        res.append(0.0)


    if d > 0:
        if t2 > 0:
            res.append(t2 ** 0.5)
            res.append(-(t2 ** 0.5))
        elif t2 == 0:
            res.append(0.0)

    return sorted(res)
