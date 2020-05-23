import pygame

class Target:
	"""managing the target"""
	def __init__(self, target_game):
		self.screen = target_game.screen
		self.settings = target_game.settings
		self.screen_rect = target_game.screen.get_rect()
		self.color = target_game.settings.target_color

		self.rect = pygame.Rect(0,0,self.settings.target_width,self.settings.target_height)
		self.rect.midright = self.screen_rect.midright

		self.y = float(self.rect.y)

	def draw_target(self):
		pygame.draw.rect(self.screen, self.color, self.rect)

	def update_target(self):
		self.y += (self.settings.target_speed * self.settings.target_direction)
		self.rect.y = self.y

	def target_check_edges(self):
		screen_rect = self.screen.get_rect()
		if self.rect.top <= 0 or self.rect.bottom >= screen_rect.bottom: #if the aliens have gone beyond the bounds
			return True
