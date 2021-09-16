#!/usr/bin/env python3
import sys

from pyglet import window, clock, app, graphics, image, gl as openGL
from pyglet.window import mouse

from game import GameMain, LevelEditor, GameStart
import settings

class Game(window.Window):
    def __init__(self, width: int, height: int, caption: str):
        super().__init__(width=width, height=height, caption=caption)
        self.game_manager = {
            'main': GameMain,
            'Development': LevelEditor,
            # 'Game Start': GameStart
        }
        self.set_graphics()
        self.game_model = self.game_manager[settings.game_model]()
        self.mouse = mouse

    def set_graphics(self) -> None:
        image.Texture.default_mag_filter = openGL.GL_NEAREST
        graphics.glScalef(settings.GLOBAL_SCALE, settings.GLOBAL_SCALE, settings.GLOBAL_SCALE)


    def on_mouse_motion(self, x: int, y: int, *_) -> None:
        x = int(x/settings.GLOBAL_SCALE)
        y = int(y/settings.GLOBAL_SCALE)
        self.game_model.on_mouse_motion(x, y)

    def on_mouse_press(self, x: int, y: int, button: int, _) -> None:
        x = int(x/settings.GLOBAL_SCALE)
        y = int(y/settings.GLOBAL_SCALE)
        self.game_model.on_mouse_press(x, y, button)

    def on_key_press(self, key: int, _) -> None:
        self.game_model.on_key_press(key)

    def on_key_release(self, key: int, _) -> None:
        self.game_model.on_key_release(key)

    def on_draw(self) -> None:
        self.clear()
        self.game_model.draw()

    def update(self, dt: float) -> None:
        if settings.game_model == 'Exit':
            sys.exit(1)
        if self.game_manager.get(settings.game_model) != None and not isinstance(self.game_model, self.game_manager[settings.game_model]):
            self.game_model.dispose()
            self.game_model = self.game_manager[settings.game_model]()
        self.game_model.update(dt)

if __name__ == '__main__':
    game = Game(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT, settings.GAME_NAME)
    clock.schedule_interval(game.update, settings.FPS_LIMIT)
    app.run()
