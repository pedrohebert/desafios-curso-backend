from typing import TypedDict


class PontoEntrega(TypedDict):
    id: int
    x: float
    y: float
    visited: list[int]
