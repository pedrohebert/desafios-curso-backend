from app.PontoEntrega import PontoEntrega
from app.tools import distancia, create_ponto_entrega, mais_proximo


ponto_de_entrega: dict[int, PontoEntrega] = {}


def main():
    ponto_de_entrega[1] = (create_ponto_entrega(1, 0, 0))
    ponto_de_entrega[2]=(create_ponto_entrega(2, 1, 5))
    ponto_de_entrega[3]=(create_ponto_entrega(3, 5, 6))
    ponto_de_entrega[4]=(create_ponto_entrega(4, 10, 10))
    ponto_de_entrega[5] = (create_ponto_entrega(5, 2, 3))

    ponto_nulo = create_ponto_entrega(0, 0, 0)
    ordem = []
    distancia_total = 0
    proximo = mais_proximo(ponto_nulo, ponto_de_entrega)

    while proximo:
        ordem.append(proximo)
        distancia_total += distancia(ponto_de_entrega[proximo], ponto_de_entrega[ordem[-1]] or ponto_nulo)
        proximo = mais_proximo(
            ponto_de_entrega[ordem[-1]],
            ponto_de_entrega,
        )

    print(dict(ordem = ordem, distancia_total = distancia_total))


if __name__ == "__main__":
    main()
