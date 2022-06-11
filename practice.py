class Character:
	def __init__(self, class_type, status):
		self.class_type = class_type
		self.status = status

	@property
	def afk(self):
		self.status = 'AFK'
		print('Playing set to FALSE')

	@property
	def playing(self):
		self.status = 'playing'
		print('Playing set to TRUE')



class Brawler(Character):
	def __init__(self, class_type, status, passive, crit, weapon):
		Character.__init__(self, class_type, status)

		self.passive = passive
		self.crit = crit
		self.weapon = weapon

	@property
	def character_weapon(self):
		return 'This brawler weilds a ' + self.weapon


class Spellcaster(Character):
	def __init__(self, class_type, status, passive, crit, weapon):
		Character.__init__(self, class_type, status)

		self.passive = passive
		self.crit = crit
		self.weapon = weapon

	@property
	def character_weapon(self):
		return 'This spellcaster weilds a ' + self.weapon

Warrior = Brawler('Melee','Playing','Absorption','Blade Maelstrom','sword')
Warrior.afk
print(Warrior.character_weapon)
print(Warrior.status)

Wizard = Spellcaster('Mid-range','AFK','Spellspinner', 'Conjure Constellation','wand')
Wizard.playing
print(Wizard.character_weapon)
print(Wizard.status)