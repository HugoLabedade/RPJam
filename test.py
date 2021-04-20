""" Sprite Sample Program """

import random
import arcade
import os

# --- Constants ---
SPRITE_SCALING_PLAYER = 3
SPRITE_SCALING_VILAIN1 = 1.75

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "RPJam"


class MenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("RPJam", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Cliquez pour commencer !", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-75, arcade.color.ORANGE, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = MyGame()
        self.window.show_view(game_view) 


class MyGame(arcade.View):
    """ Our custom Window Class"""

    file_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(file_path)

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        
        super().__init__()

        self.background = arcade.load_texture("assets/bg2.jpg")

        self.player_list = arcade.SpriteList()
        self.vilain_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite("assets/benjam.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 250
        self.player_sprite.center_y = 235

        self.vilain_sprite = arcade.Sprite("assets/mechant1.png", SPRITE_SCALING_VILAIN1)
        self.vilain_sprite.center_x = 1000
        self.vilain_sprite.center_y = 350

        self.vilain_list.append(self.vilain_sprite)
        self.player_list.append(self.player_sprite)


    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.player_list.draw()
        self.vilain_list.draw()





def main():
    """ Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()