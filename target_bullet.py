import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""a class to manage bullets"""
	def __init__(self, target_game):
		"""create bullet object at ship's current position"""
		super().__init__()
		self.screen = target_game.screen
		self.settings = target_game.settings
		self.color = self.settings.bullet_color

		#create bullet rect at 0,0 and then set the correct position
		self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
		self.rect.midright = target_game.ship.ship_rect.midright

		#store the bullet's position as a decimal
		self.x = float(self.rect.x)

	def update(self):
		"""move the bullet up the screen"""
		#update the decimal position of the bullet
		self.x += self.settings.bullet_speed #subtracting the bullet speed because that's how fast the 
		#bullet is moving up the screen
		#update the rect position
		self.rect.x = self.x 

	def draw_bullet(self):
		"""draw the bullet to the screen"""
		pygame.draw.rect(self.screen, self.color, self.rect) #fills the part of the screen defined by the 
		#bullet's rect with the color stored in self.color 