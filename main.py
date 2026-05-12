from typing import TypedDict
from math import sqrt

class PontoEntrega(TypedDict):
    id:int
    x:float
    y:float

ponto_de_entrega:list[PontoEntrega] = []

def distancia(p1:PontoEntrega, p2:PontoEntrega) -> float:
    return sqrt((p1["x"] - p2["x"])**2 + (p1["y"] - p2["y"])**2 )

def main():
    pass

if __name__ == "__main__":
    main()
