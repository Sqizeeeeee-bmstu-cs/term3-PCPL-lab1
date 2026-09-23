
def extract_roots_from_t(t: float) -> tuple[float, ...]:
    match t:
        case _ if t < 0:
            return ()
        case 0.0:
            return (0.0,)
        case _:
            return (t ** 0.5, -(t ** 0.5))

def solve_biquadratic(a: float, b: float, c: float) -> tuple[float, tuple[float, ...]]:

    d = b ** 2 - 4 * a * c
    
    match d:
        case _ if d < 0:
            return d, ()
            
        case 0.0:
            t = -b / (2 * a)
            return d, extract_roots_from_t(t)
            
        case _:
            sqrt_d = d ** 0.5
            t1 = (-b + sqrt_d) / (2 * a)
            t2 = (-b - sqrt_d) / (2 * a)

            all_roots = tuple(sorted(set(extract_roots_from_t(t1) + extract_roots_from_t(t2))))
            return d, all_roots

def format_result(d: float, roots: tuple[float, ...]) -> str:
    match roots:
        case ():
            return f"D = {d}. Действительных корней нет."
        case (root,):
            return f"D = {d}. Один корень: {root}"
        case _:
            return f"D = {d}. Действительные корни: {list(roots)}"

