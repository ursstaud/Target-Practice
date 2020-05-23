import sys
import pygame
from target_settings import Settings
from target_ship import Ship
from target_bullet import Bullet
from target_target import Target
from target_button import Button

class TargetPractice:
	"""overall class for game"""
	def __init__(self):
		"""initialize game"""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width 
		self.settings.screen_height = self.screen.get_rect().height
		self.settings.screen = self.screen.get_rect()
		pygame.display.set_caption("Target Practice")

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.target = Target(self)
		self.play_button = Button(self, "Play")
		self.number_misses = 0
		self.number_hits = 0
		

	def run_game(self):
		"""main loop for the game"""
		while True:
			self._check_events()

			if self.settings.game_active:
				self.ship.update_ship()
				self._update_bullets()
				self._update_target()

			#redraw screen and flip 
			self._update_screen()
			
			
	#updating 
	def _update_screen(self):
		"""update images on screen and flip"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.target.draw_target()

		if not self.settings.game_active:
			self.play_button.draw_button()
		
		pygame.display.flip()
	

	#bullets
	def _fire_bullet(self):
		"""create new bullet and add to group"""
		if len(self.bullets)< self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		"""updates actions of bullet"""
		self.bullets.update()
		self._check_misses()


	#target 
	def _update_target(self):
		"""update actions of the target"""
		self._check_target_edges()
		self.target.update_target()
		self._check_bullet_outcome()
		
	def _check_target_edges(self):
		"""switch directions when a target hits the edge"""
		if self.target.target_check_edges():
			self.settings.target_direction *= -1

	def _check_bullet_outcome(self):
		"""possible outcomes for a bullet"""
		if pygame.sprite.spritecollideany(self.target, self.bullets):
			self._check_hits()
		if not pygame.sprite.spritecollideany(self.target, self.bullets):
			self._check_misses()

	def _check_hits(self):
		"""checking to see if a bullet hit the target"""
		for bullet in self.bullets.copy():
			if bullet.rect.right >= self.target.rect.left:	
				self.bullets.remove(bullet)
				self.number_hits += 1
				print(f"Number of hits: {self.number_hits}")
		self.settings.increase_speed()

	def _check_misses(self):
		"""checking to see if a bullet missed the target"""
		for bullet in self.bullets.copy():
			if bullet.rect.left >= self.settings.screen.right:
				self.bullets.remove(bullet)
				self.number_misses += 1
				print(f"Number of misses: {self.number_misses}")

		self._check_bullet_counts()

	def _check_bullet_counts(self):
		if self.number_misses >= 3:
			self.settings.game_active = False
			 
	def _reset_statistics(self):
		"""reset statistics to original values"""
		self.number_misses = 0
		self.number_hits = 0


	#check events			
	def _check_events(self):
		"""respond to key presses"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)

	def _check_play_button(self, mouse_pos):
		"""start a new game when the player clicks play"""
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.settings.game_active:
			self.settings.initialize_dynamic_settings()
			self._reset_statistics()
			self.settings.game_active = True
			self.bullets.empty()

	def _check_keydown(self, event):
		"""respond to keydown"""
		if event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup(self, event):
		"""respond to keyup"""
		if event.key == pygame.K_UP:
			self.ship.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False


if __name__ == '__main__':
	tp = TargetPractice()
	tp.run_game()
