import time
from pynput.keyboard import Controller as Keyboard
from pynput.keyboard import GlobalHotKeys, Key


class KeyboardFun:
	def __init__(self):
		self.running = False            # running key combos or not
		self.program_running = True     # should program quit or not
		self.Keyboard = Keyboard()      # keyboard controller

		# listens for these key combos and runs these functions if key combos are pressed
		self.listener = GlobalHotKeys({
			'<ctrl>+<alt>+p': self.toggle_running,
			'<ctrl>+<alt>+O': self.toggle_running,
			'<ctrl>+<alt>+q': self.exit_out,
		})
		self.listener.start()           # starts listening for key combos

	def toggle_running(self):
		"""This just toggles the running state"""
		if self.running:
			self.running = False
		else:
			self.running = True

	def exit_out(self):
		"""This will clear key holds and exit"""
		self.Keyboard.release(Key.shift)
		self.program_running = False

	def toggle_shift(self, stop=False):
		"""This should press shift unless it's time to stop holding shift"""
		if stop:
			print('toggle shift release')
			self.Keyboard.release(Key.shift)
		else:
			print('toggle shift press')
			self.Keyboard.press(Key.shift)

	def keys_loop(self):
		time.sleep(0.1)
		if self.running:
			self.Keyboard.press(Key.shift)
			self.Keyboard.press('w')
		now = time.time()
		while self.running:
			if time.time() - now > 20:
				self.Keyboard.release('w')
				time.sleep(2)
				self.Keyboard.press('w')
				now = time.time()
			time.sleep(0.3)
			self.Keyboard.tap('c')
		self.Keyboard.release(Key.shift)
		self.Keyboard.release('w')


if __name__ == '__main__':
	kb = KeyboardFun()
	while kb.program_running:
		time.sleep(0.1)
		kb.keys_loop()
