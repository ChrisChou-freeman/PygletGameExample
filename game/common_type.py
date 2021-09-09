from typing import NamedTuple

class Point(NamedTuple):
    x: int
    y: int

class RGBAColor(NamedTuple):
    r: int
    g: int
    b: int
    a: int

class Rectangle(NamedTuple):
    x: int
    y: int
    width: int
    height: int
