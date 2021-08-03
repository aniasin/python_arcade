import game


def input_press(gi, key, player_sprite):
    if key == game.arcade.key.UP or key == game.arcade.key.W or key == game.arcade.key.SPACE:
        if gi.physics_engine.can_jump():
            player_sprite.change_y = game.PLAYER_JUMP_SPEED
            game.arcade.play_sound(gi.jump_sound)
    elif key == game.arcade.key.DOWN or key == game.arcade.key.S:
        player_sprite.change_y = -game.PLAYER_MOVEMENT_SPEED
    elif key == game.arcade.key.LEFT or key == game.arcade.key.A:
        player_sprite.change_x = -game.PLAYER_MOVEMENT_SPEED
    elif key == game.arcade.key.RIGHT or key == game.arcade.key.D:
        player_sprite.change_x = game.PLAYER_MOVEMENT_SPEED


def input_release(key, player_sprite):
    if key == game.arcade.key.UP or key == game.arcade.key.W:
        player_sprite.change_y = 0
    elif key == game.arcade.key.DOWN or key == game.arcade.key.S:
        player_sprite.change_y = 0
    elif key == game.arcade.key.LEFT or key == game.arcade.key.A:
        player_sprite.change_x = 0
    elif key == game.arcade.key.RIGHT or key == game.arcade.key.D:
        player_sprite.change_x = 0

