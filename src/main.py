#!/usr/bin/env python3

from Console.Console import Console
from Api.NBPApiAdapter import NBPApiAdapter
from Calculator.Calculator import Calculator


def main():
    nbp_adapter = NBPApiAdapter()
    calculator = Calculator(nbp_adapter)
    console = Console(calculator)
    console.run()


if __name__ == '__main__':
    main()
