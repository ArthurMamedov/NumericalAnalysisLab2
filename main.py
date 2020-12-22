#!/bin/python3
from numerical import ReductionMethod
from analytical import LeastSquare
from graphics import Graphics
from table_print import TablePrinter
from config import Config
from math import sin, cos, log, e


MANUAL = False


def main():

    print("y\"+2*x*y'-y=2*cos(x)*(x^2+1)")
    print("y'(0)=0, y(0.5)=0.5*sin(0.5)")
    print("y*=x*sin(x)")

    print('Программа высчитывает численное и аналитическое решение.')
    config = Config()
    if MANUAL: print("\nПромежуток [a,b]:")
    config['a']    = float(input('Введите a: ')) if MANUAL else 0.0
    config['b']    = float(input('Введите b: ')) if  MANUAL else 0.5

    if MANUAL: print("\nУравнение g(x)y\"(x) + p(x)y'(x) + q(x)y(x) = f(x):")
    config['g(x)'] =       input('Введите g(x): ') if MANUAL else '1'
    config['p(x)'] =       input('Введите p(x): ') if MANUAL else '2*x'
    config['q(x)'] =       input('Введите q(x): ') if MANUAL else '-1'
    config['f(x)'] =       input('Введите f(x): ') if MANUAL else '2*cos(x)*(x**2+1)'
    
    if MANUAL: print("\nГраничное условие a0*y(a)+a1*y'(a)=A:")
    config['a0']   = float(input('Введите a0: ')) if MANUAL else 0
    config['a1']   = float(input('Введите a1: ')) if MANUAL else 1
    config['A']    = float(input('Введите A: ')) if MANUAL else 0
    
    if MANUAL: print("\nГраничное условие b0*y(b)+b1*y'(b)=B:")
    config['b0']   = float(input('Enter b0: ')) if MANUAL else 1
    config['b1']   = float(input('Enter b1: ')) if MANUAL else 0
    config['B']    = float(input('Enter B: ')) if MANUAL else 0.5*sin(0.5)

    if MANUAL: print()
    step           = float(input('Введите шаг: ')) if MANUAL else 0.01
    check          =       input('Введите точное решение: ') if MANUAL else 'x*sin(x)'

    if not check == '' or config.is_valid(check):
        rm = ReductionMethod(config)
        ls = LeastSquare(config)
        grp = Graphics()
        xpoints : List[Tuple[float, float]] = []
        rmpoints : List[Tuple[float, float]] = []
        lspoints : List[Tuple[float, float]] = []
        rpoints : Optional[List[Tuple[float, float]]] = [] if check != '' else None
        for set_rm, set_ls in zip(rm.get_values(step), ls.get_values(step)):
            xpoints.append(round(set_rm[0], 4))
            rmpoints.append(round(set_rm[1], 4))
            lspoints.append(round(set_ls[1], 4))
            if rpoints is not None:
                rpoints.append(eval(check.replace('x', f'({set_rm[0]})')))
        print(ls.get_analytical_solution())
        if rpoints is not None:
            tb = TablePrinter(['Значения Х', *xpoints], ['Метод редукции', *rmpoints], ['Метод наим.квадратов', *lspoints], ['Точные значения', *rpoints])
            tb.print_table()
            grp.draw([xpoints, xpoints, xpoints], [rmpoints, lspoints, rpoints], ['Метод редукции','Метод наим.квадратов','Точное значение'], 'Задача Коши')
    else:
        print('Sorry, the conditions are not valid.')
        exit()


if __name__ == '__main__':
    main()
