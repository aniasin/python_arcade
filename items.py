from arcade import Sprite, load_sound, play_sound
import game


class Coin(Sprite):
    def __init__(self):
        super().__init__(':resources:images/items/coinGold.png', game.COIN_SCALING)
        self.collect_coin_sound = load_sound(':resources:sounds/coin1.wav')
        self.value = 1

    def collided(self, player):
        self.remove_from_sprite_lists()
        play_sound(self.collect_coin_sound)
