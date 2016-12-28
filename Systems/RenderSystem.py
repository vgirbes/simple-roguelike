import tcod as libtcod

class RenderSystem:
    def __init__(self, scrWidth = 80, scrHeight = 50):
        self.scrWidth = scrWidth
        self.scrHeight = scrHeight

        self.background = libtcod.BKGND_NONE

        self.windowName = 'rogue'

        self.render = libtcod

        self.render.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
        self.render.console_init_root(self.scrWidth, self.scrHeight, self.windowName, False)

    def pre_update(self):
        return None

    def update(self, entities):
        for entity in entities:
            self.render.console_put_char(0,
                entity.components['position'].x,
                entity.components['position'].y,
                entity.components['render'].char,
                self.background)

    def post_update(self):
        self.render.console_flush()
