""" Sprite Sample Program """

import random
import arcade
import os
import arcade.gui
from arcade.gui import UIManager

# --- Constants ---
SPRITE_SCALING_PLAYER = 3
SPRITE_SCALING_VILAIN1 = 1.75

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "RPJam"


class MenuView(arcade.View):
    def on_show(self):
        self.background = arcade.load_texture("assets/bg2.jpg")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        arcade.draw_text("RPJam", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Cliquez pour commencer !", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-75, arcade.color.ORANGE, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = MyGame()
        self.window.show_view(game_view) 

class MyFlatButton(arcade.gui.UIFlatButton):
    def on_click(self):
        """ Called when user lets off button """
        print("Click flat button. ")


class MyGame(arcade.View):
    """ Our custom Window Class"""

    file_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(file_path)

    def __init__(self):
        super().__init__()
        self.ui_manager = UIManager()
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
        arcade.draw_rectangle_outline(center_x=282, center_y=57, width=550, height=100, color=arcade.color.WHITE, border_width=3)
        self.player_list.draw()
        self.vilain_list.draw()
    
    def on_show_view(self):
        self.setup()

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def setup(self):
        self.ui_manager.purge_ui_elements()
        y_slot = self.window.height // 9
        right_column_x = self.window.width // 8.5
        button = MyFlatButton(
            'Attaque 1',
            center_x=right_column_x,
            center_y=y_slot * 1,
            width=250,
            # height=20
        )
        button.set_style_attrs(
            bg_color = (255, 0, 0, 0),
            border_color = arcade.color.WHITE
        )
        self.ui_manager.add_ui_element(button)

        y_slot_2 = self.window.height // 9
        right_column_x_2 = self.window.width // 3.1
        button2 = MyFlatButton(
            'Attaque 2',
            center_x=right_column_x_2,
            center_y=y_slot_2 * 1,
            width=250,
            # height=20
        )
        button2.set_style_attrs(
            bg_color = (255, 0, 0, 0),
            border_color = arcade.color.WHITE
        )
        self.ui_manager.add_ui_element(button2)

        y_slot_3 = self.window.height // 20
        right_column_x_3 = self.window.width // 8.5
        button3 = MyFlatButton(
            'Attaque 3',
            center_x=right_column_x_3,
            center_y=y_slot_3 * 1,
            width=250,
            # height=20
        )
        button3.set_style_attrs(
            bg_color = (255, 0, 0, 0),
            border_color = arcade.color.WHITE
        )
        self.ui_manager.add_ui_element(button3)

        y_slot_4 = self.window.height // 20
        right_column_x_4 = self.window.width // 3.1
        button4 = MyFlatButton(
            'Attaque 4',
            center_x=right_column_x_4,
            center_y=y_slot_4 * 1,
            width=250,
            # height=20
        )
        button4.set_style_attrs(
            bg_color = (255, 0, 0, 0),
            border_color = arcade.color.WHITE
        )
        self.ui_manager.add_ui_element(button4)





def main():
    """ Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()