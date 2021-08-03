import game


def scroll(gi):
    # ---- Manage scrolling ----
    # Track if we need to change the viewport
    changed = False

    # Scroll left
    left_boundary = gi.view_left + game.LEFT_VIEWPORT_MARGIN
    if gi.player_sprite.left < left_boundary:
        gi.view_left -= left_boundary - gi.player_sprite.left
        changed = True
    # Scroll right
    right_boundary = gi.view_left + game.SCREEN_WIDTH - game.RIGHT_VIEWPORT_MARGIN
    if gi.player_sprite.left > right_boundary:
        gi.view_left += gi.player_sprite.right - right_boundary
        changed = True
    # Scroll up
    top_boundary = gi.view_bottom + game.SCREEN_HEIGHT - game.TOP_VIEWPORT_MARGIN
    if gi.player_sprite.top > top_boundary:
        gi.view_bottom += gi.player_sprite.top - top_boundary
        changed = True
    # Scroll down
    bottom_boundary = gi.view_bottom + game.BOTTOM_VIEWPORT_MARGIN
    if gi.player_sprite.bottom < bottom_boundary:
        gi.view_bottom -= bottom_boundary - gi.player_sprite.bottom
        changed = True

    if changed:
        gi.view_bottom = int(gi.view_bottom)
        gi.view_left = int(gi.view_left)

    # Do the scrolling
    game.arcade.set_viewport(gi.view_left,
                             game.SCREEN_WIDTH + gi.view_left,
                             gi.view_bottom,
                             game.SCREEN_HEIGHT + gi.view_bottom
                             )
