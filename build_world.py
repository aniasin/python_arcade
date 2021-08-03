import random

import game
import items


def start_level(gi):
    # Keep track of scrolling
    gi.view_bottom = 0
    gi.view_left = 0
    # Keep track of the score
    gi.score = 0

    # Create the Sprite lists
    gi.player_list = game.arcade.SpriteList()
    gi.wall_list = game.arcade.SpriteList(use_spatial_hash=True)
    gi.coin_list = game.arcade.SpriteList(use_spatial_hash=True)

    create_player(gi)

    create_ground(gi)

    # Create the 'physics engine'
    gi.physics_engine = game.arcade.PhysicsEnginePlatformer(gi.player_sprite, gi.wall_list, game.GRAVITY)


def create_player(gi):
    # Set up the player, specifically placing it at these coordinates.
    gi.player_sprite = game.arcade.Sprite(
        ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png",
        game.CHARACTER_SCALING)
    gi.player_sprite.center_x = 64
    gi.player_sprite.center_y = 128
    gi.player_list.append(gi.player_sprite)


def create_ground(gi):
    # Create the ground
    # This shows using a loop to place multiple sprites horizontally
    for x in range(0, 1250, 64):
        wall = game.arcade.Sprite(":resources:images/tiles/grassMid.png", game.TILE_SCALING)
        wall.center_x = x
        wall.center_y = 32
        gi.wall_list.append(wall)

    if game.FROM_TILED:
        # Load from tiled editor
        map_name = ':resources:tmx_maps/map.tmx'
        platform_layer_name = 'Platforms'
        coin_layer_name = 'Coins'

        # Read the tiled map
        my_map = game.arcade.tilemap.read_tmx(map_name)
        gi.wall_list = game.arcade.tilemap.process_layer(my_map,
                                                         platform_layer_name,
                                                         game.TILE_SCALING,
                                                         use_spatial_hash=True)
        coin_list = game.arcade.tilemap.process_layer(my_map, coin_layer_name, game.TILE_SCALING)
        for coin in coin_list:
            my_coin = items.Coin()
            my_coin.position = coin.position
            my_coin.value = random.randint(1, 5)
            gi.coin_list.append(my_coin)
    else:
        # Put some crates on the ground
        # This shows using a coordinate list to place sprites
        coordinate_list = [[256, 96],
                           [512, 96],
                           [768, 96],
                           ]

        for coordinate in coordinate_list:
            # Add a crate on the ground
            wall = game.arcade.Sprite(":resources:images/tiles/boxCrate_double.png", game.TILE_SCALING)
            wall.position = coordinate
            gi.wall_list.append(wall)

            # Loop to place some coins
        for x in range(128, 1250, 256):
            coin = items.Coin()
            coin.center_x = x
            coin.center_y = 96
            coin.value = random.randint(1, 5)
            gi.coin_list.append(coin)
            print(coin)
