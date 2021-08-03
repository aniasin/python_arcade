import game


def scroll(gi):
    # ---- Manage scrolling ----
    # Track if we need to change the viewport
    changed = False

    # Scroll left
    left_boundary = gi.view_left + game.LEFT_VIEWPORT_MARGIN
    if gi.player.left < left_boundary:
        gi.view_left -= left_boundary - gi.player.left
        changed = True
    # Scroll right
    right_boundary = gi.view_left + game.SCREEN_WIDTH - game.RIGHT_VIEWPORT_MARGIN
    if gi.player.left > right_boundary:
        gi.view_left += gi.player.right - right_boundary
        changed = True
    # Scroll up
    top_boundary = gi.view_bottom + game.SCREEN_HEIGHT - game.TOP_VIEWPORT_MARGIN
    if gi.player.top > top_boundary:
        gi.view_bottom += gi.player.top - top_boundary
        changed = True
    # Scroll down
    bottom_boundary = gi.view_bottom + game.BOTTOM_VIEWPORT_MARGIN
    if gi.player.bottom < bottom_boundary:
        gi.view_bottom -= bottom_boundary - gi.player.bottom
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
