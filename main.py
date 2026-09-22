import sys
from typing import Tuple, Dict, Any

from procedure import solver as procedural_solver
from oop import Solver as OOPSolver
from functional import solve_biquadratic, format_result


def parse_arguments() -> Tuple[str, list]:
    args = sys.argv[1:]
    mode = "proc"
    clean_args = []

    iterator = iter(args)
    for arg in iterator:
        if arg in ("--mode", "-m"):
            try:
                mode = next(iterator).lower()
            except StopIteration:
                print("Ошибка: После флага --mode не указан режим. Используется 'proc'.")
        else:
            clean_args.append(arg)
            
    return mode, clean_args

def get_coefficients(cli_args: list) -> Tuple[float, float, float]:
    coeffs: Dict[str, float] = {}
    names = ['A', 'B', 'C']
    cli_index = 0

    for name in names:
        while True:
            if cli_index < len(cli_args):
                val_str = cli_args[cli_index]
                cli_index += 1
                try:
                    val = float(val_str)
                    if name == 'A' and val == 0:
                        print("Ошибка в CLI: Коэффициент 'A' не может быть равен 0.")
                        continue
                    coeffs[name] = val
                    break
                except ValueError:
                    print(f"Аргумент командной строки для {name} ('{val_str}') некорректен. Переход к ручному вводу.")

            try:
                val = float(input(f"Введите коэффициент {name}: "))
                if name == 'A' and val == 0:
                    print("Коэффициент 'A' не может быть равен 0 для биквадратного уравнения. Попробуйте снова.")
                    continue
                coeffs[name] = val
                break
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите действительное число (float).")

    return coeffs['A'], coeffs['B'], coeffs['C']

def execute_solution(mode: str, **kwargs: float) -> None:
    a = kwargs.get('a', 1.0)
    b = kwargs.get('b', 0.0)
    c = kwargs.get('c', 0.0)

    print(f"\nРешаем уравнение: {a}x^4 + {b}x^2 + {c} = 0")

    match mode:
        case "proc" | "procedure" | "procedural":
            print("[Запуск: Процедурная парадигма]")
            roots = procedural_solver(int(a), int(b), int(c))
            print(f"Результат (список корней): {roots}")

        case "oop":
            print("[Запуск: Объектно-ориентированная парадигма]")
            solver_obj = OOPSolver(int(a), int(b), int(c))
            solver_obj.solve()
            print(solver_obj)

        case "func" | "functional":
            print("[Запуск: Функциональная парадигма (Pattern Matching)]")
            d, roots = solve_biquadratic(a, b, c)
            print(format_result(d, roots))

        case _:
            print(f"Неизвестный режим '{mode}'. Доступны: proc, oop, func. Запуск в режиме 'proc' по умолчанию.")
            execute_solution("proc", a=a, b=b, c=c)

def main():
    print("введите коэф.")
    mode, cli_coefficients = parse_arguments()
    a, b, c = get_coefficients(cli_coefficients)
    execute_solution(mode, a=a, b=b, c=c)

if __name__ == '__main__':
    main()
