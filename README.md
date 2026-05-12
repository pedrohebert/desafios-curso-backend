
## descrição do problema   

Desafio 1 - Desafio Técnico Prático: "Otimizador de Rota de Entrega"  
Empresa: Inovatech Junior  


1. Objetivo  
O objetivo deste desafio é desenvolver um algoritmo que otimize a rota de entrega de um caminhão, visitando diversos pontos na ordem mais eficiente possível para minimizar a distância total percorrida. O foco está na lógica de programação e no uso de boas práticas. 


2. Regras de Desenvolvimento  
- Linguagem: Deve-se utilizar Python.
- Sem Frameworks: Não é permitida a utilização de frameworks ou bibliotecas externas para a lógica central.
- Versionamento: O código deve ser postado em um repositório privado no GitHub com commits regulares seguindo o padrão Conventional Commits.  


3. Representação e Entrada de Dados Cada ponto de entrega é representado por um dicionário com um identificador e coordenadas cartesianas.  

Exemplo de Entrada (Python):  

```python
ponto_de_entrega = [
    {"id": 1, "x":0 ,"y":0},
    {"id": 2, "x":10 ,"y":53},
    {"id": 3, "x":5 ,"y":12},
    {"id": 4, "x":8 ,"y":33},
    {"id": 5, "x":2 ,"y":83},
]
```

4. Processamento e Lógica O algoritmo deve implementar uma estratégia válida (como o Vizinho Mais Próximo) para encontrar uma rota eficiente.  

A Fórmula da Distância Para calcular o deslocamento entre dois pontos, deve-se obrigatoriamente usar a fórmula da distância euclidiana:
```
d = raiz( (x1 - x2)² + (y1 - y2)² )
```
