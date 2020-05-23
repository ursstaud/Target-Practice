class Settings:
	"""a class to store all the settings for the Alien Invasion game"""

	def __init__(self):
		"""initialize the game settings"""
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (124, 185, 232)
		self.game_active = False

		#bullet stuff
		self.bullet_width = 15
		self.bullet_height = 3
		self.bullet_color = (60,60,60)
		self.bullets_allowed = 3

		#target stuff
		self.target_width = 20
		self.target_height = 150
		self.target_color = (165, 42, 42)
		
		self.speedup_scale = 1.1

		self.ship_speed = 5
		self.bullet_speed = 15
		self.target_speed = 3
		self.target_direction = 1

	def initialize_dynamic_settings(self):
		"""settings that change throughout the game"""
		self.ship_speed = 5
		self.bullet_speed = 15
		self.target_speed = 3
		self.target_direction = 1

	def increase_speed(self):
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.target_speed *= self.speedup_scale