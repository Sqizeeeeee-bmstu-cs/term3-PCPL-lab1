from typing import List


class Solver:

    def __init__(self, A: int, B: int, C: int):

        if A == 0:
            raise ValueError('A != 0!')

        self.a = A
        self.b = B
        self.c = C

        self.d: float | None = None

        self.roots: List[float] = []

    def solve(self) -> None:

        self.d = self.b ** 2 - 4 * self.a * self.c

        if self.d < 0:
            self.roots = []
            return

        roots_set = set()
        sqrt_d = self.d ** 0.5

        t1 = (-self.b + sqrt_d) / (self.a * 2)
        t2 = (-self.b - sqrt_d) / (self.a * 2)

        cand = (t1,) if self.d == 0 else (t1, t2)

        for t in cand:

            if t > 0:

                roots_set.add(t ** 0.5)
                roots_set.add(-(t** 0.5))

            if t == 0:

                roots_set.add(0.0)

        self.roots = sorted(roots_set)

    def __str__(self) -> str:

        res = f"Roots: {self.roots}" if self.roots else "No roots"

        return res 
