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

    create_ground(gi)
    game.arcade.set_background_color(game.arcade.csscolor.CORNFLOWER_BLUE)

    # Create the 'physics engine'
    gi.physics_engine = game.arcade.PhysicsEnginePlatformer(gi.player, gi.wall_list, game.GRAVITY)


def create_player(gi):
    # Set up the player, specifically placing it at these coordinates.
    texture_path = 'assets/img/player/'
    walking_path = [
        texture_path + f'player_walk{x}.png' for x in (1, 2)
    ]
    climbing_path = [
        texture_path + f'player_climb{x}.png' for x in (1, 2)
    ]
    standing_path = [
        texture_path + f'player_stand.png'
    ]

    # Load the textures
    walking_right_textures = [
        game.arcade.load_texture(texture) for texture in walking_path
    ]
    walking_left_textures = [
        game.arcade.load_texture(texture, mirrored=True) for texture in walking_path
    ]
    walking_up_textures = [
        game.arcade.load_texture(texture) for texture in climbing_path
    ]
    walking_down_textures = [
        game.arcade.load_texture(texture) for texture in climbing_path
    ]
    standing_right_textures = [
        game.arcade.load_texture(texture) for texture in standing_path
    ]
    standing_left_textures = [
        game.arcade.load_texture(texture, mirrored=True) for texture in standing_path
    ]

    # Create the sprite
    player = game.arcade.AnimatedWalkingSprite()

    # Add the proper textures
    player.stand_left_textures = standing_left_textures
    player.stand_right_textures = standing_right_textures
    player.walk_right_textures = walking_right_textures
    player.walk_left_textures = walking_left_textures
    player.walk_up_textures = walking_up_textures
    player.walk_down_textures = walking_down_textures

    # Set the player defaults
    player.center_x = 64
    player.center_y = 128
    player_state = game.arcade.FACE_RIGHT
    # Set the initial texture
    player.texture = player.stand_right_textures[0]

    return player


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
