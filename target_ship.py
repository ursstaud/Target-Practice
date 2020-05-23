import pygame

class Ship:
	"""creating a class for the ship"""
	def __init__(self, target_game):
		self.screen = target_game.screen
		self.settings = target_game.settings
		self.screen_rect = target_game.screen.get_rect()
		self.ship_image = pygame.image.load('shipedit.bmp')
		self.ship_rect = self.ship_image.get_rect()

		self.ship_rect.midleft = self.screen_rect.midleft
		self.y = float(self.ship_rect.y)

		self.moving_up = False
		self.moving_down = False

	def blitme(self):
		self.screen.blit(self.ship_image, self.ship_rect)

	def update_ship(self):
		#if self.moving_up:
		#	self.y -= self.settings.ship_speed
		#if self.moving_down:
		#	self.y += self.settings.ship_speed
		#self.ship_rect.y = self.y
		"""update the ship's position"""
		if self.moving_up and self.ship_rect.top > 0:
			self.y -= self.settings.ship_speed
		if self.moving_down and self.ship_rect.bottom < self.screen_rect.bottom: #checks the position of the ship before changing the value of self.x
			self.y += self.settings.ship_speed
		

		#update rect object from self.x
		self.ship_rect.y = self.y

#class Target:
