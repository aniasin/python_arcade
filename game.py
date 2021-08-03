import arcade
import build_world
import player_controller
import view
import items

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"
FROM_TILED = True

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5

# Movement speed of player, in pixels per frame
GRAVITY = 1
PLAYER_JUMP_SPEED = 20
PLAYER_MOVEMENT_SPEED = 5

# How many pixels to keep as minimum margin between player and edge of screen
LEFT_VIEWPORT_MARGIN = 250
RIGHT_VIEWPORT_MARGIN = 250
BOTTOM_VIEWPORT_MARGIN = 50
TOP_VIEWPORT_MARGIN = 100


class MyGame(arcade.Window):
    """
    Main application class.
    """
    def __init__(self):
        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.coin_list = None
        self.wall_list = None
        self.player_list = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        # Our physics engine
        self.physics_engine = None

        # Keep track of scrolling
        self.view_bottom = 0
        self.view_left = 0

        # Keep track of the score
        self.score = 0

        # Load sounds
        self.jump_sound = arcade.load_sound(':resources:sounds/jump1.wav')
        self.collect_coin_sound = arcade.load_sound(':resources:sounds/coin1.wav')

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        build_world.start_level(self)

    def on_draw(self):
        """ Render the screen. """
        # Clear the screen to the background color
        arcade.start_render()
        # Draw our sprites
        self.wall_list.draw()
        self.coin_list.draw()
        self.player_list.draw()

        # Draw score on the screen, scrolling
        score_text = f'Score: {self.score}'
        arcade.draw_text(score_text, 10 + self.view_left, 10 + self.view_bottom,
                         arcade.csscolor.WHITE, 18
                         )

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        player_controller.input_press(self, key, self.player_sprite)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        player_controller.input_release(key, self.player_sprite)

    def on_update(self, delta_time):
        """ Movement and game logic """
        # Move the player with the physics engine
        self.physics_engine.update()

        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coin_hit_list:
            coin.collided(self.player_sprite)
            self.score += coin.value

        view.scroll(self)

