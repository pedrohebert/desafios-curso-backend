from typing import TypedDict
from math import sqrt

class PontoEntrega(TypedDict):
    id:int
    x:float
    y:float
    visited: list[int]

ponto_de_entrega:list[PontoEntrega] = []

def distancia(p1:PontoEntrega, p2:PontoEntrega) -> float:
    return sqrt((p1["x"] - p2["x"])**2 + (p1["y"] - p2["y"])**2 )

def create_ponto_entrega(id:int, x:float, y:float,/) -> PontoEntrega:
    return PontoEntrega(id=id, x=x,y=y, visited=[])

def mais_proximo(p:PontoEntrega, ori_pontos:list[PontoEntrega]) -> int:

    proximo = 0
    menor_dis = 99999999999999999

    pontos = [ponto for ponto in ori_pontos if ponto["id"] != p["id"]]
    pontos = [ponto for ponto in pontos if ponto["id"] not in p["visited"]]

    print(pontos)

    for ponto in pontos:
        dis = distancia(p,ponto)
        ponto["visited"].append(p["id"])
        if dis < menor_dis:
            proximo = ponto["id"]
            menor_dis = dis

    return proximo



def main():
    ponto_de_entrega.append(create_ponto_entrega(1,0,0))
    ponto_de_entrega.append(create_ponto_entrega(2,1,5))
    ponto_de_entrega.append(create_ponto_entrega(3,5,6))
    ponto_de_entrega.append(create_ponto_entrega(4,10,10))
    ponto_de_entrega.append(create_ponto_entrega(5,2,3))

    ordem = []
    proximo = mais_proximo(create_ponto_entrega(0,0,0), ponto_de_entrega)

    while proximo:

        ordem.append(proximo)
        proximo = mais_proximo(
            list([i for i in ponto_de_entrega if i["id"] == ordem[-1]])[-1],
            ponto_de_entrega
        )







    print(ordem)

if __name__ == "__main__":
    main()
