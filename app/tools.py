
from math import sqrt
from app.PontoEntrega import PontoEntrega


def distancia(p1: PontoEntrega, p2: PontoEntrega) -> float:
    return sqrt((p1["x"] - p2["x"]) ** 2 + (p1["y"] - p2["y"]) ** 2)


def create_ponto_entrega(id: int, x: float, y: float, /) -> PontoEntrega:
    return PontoEntrega(id=id, x=x, y=y, visited=[])

def mais_proximo(p: PontoEntrega, ori_pontos: dict[int,PontoEntrega]) -> int:

    proximo = 0
    menor_dis = 99999999999999999

    pontos = [
        ponto
        for id,ponto in ori_pontos.items()
        if id != p["id"] and id not in p["visited"]
    ]

    # print(pontos)

    for ponto in pontos:
        dis = distancia(p, ponto)
        ponto["visited"].append(p["id"])
        if dis < menor_dis:
            proximo = ponto["id"]
            menor_dis = dis

    return proximo
