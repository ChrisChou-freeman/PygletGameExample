from pyglet.image import AbstractImage
from pyglet.sprite import Sprite
from pyglet.graphics import Batch, OrderedGroup

from .common_type import Rectangle, Point

class Button(Sprite):
    def __init__(self,
                 img: AbstractImage,
                 x:int,
                 y:int,
                 batch: Batch,
                 group: OrderedGroup):
        super().__init__(img, x, y, batch=batch, group=group)
        self.in_select = False

    def get_rec(self) -> Rectangle:
        return Rectangle(self.x, self.y, self.width, self.height)

    def on_hover(self, point: Point) -> bool:
        rec = self.get_rec()
        return point.x >= rec.x and point.x <= (rec.x + rec.width) and point.y >= rec.y and point.y <= (rec.y + rec.width)

    def on_click(self) -> None:
        self.in_select = True
