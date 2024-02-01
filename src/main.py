#!/usr/bin/env python3

from src.Console import Console
from src.NBPApiAdapter import NBPApiAdapter
from src.Calculator import Calculator


def main():
    nbp_adapter = NBPApiAdapter()
    calculator = Calculator(nbp_adapter)
    console = Console(calculator)
    console.run()


if __name__ == '__main__':
    main()
