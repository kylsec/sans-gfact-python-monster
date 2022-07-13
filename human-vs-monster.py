import random
import os


# Wipe terminal on both Windows and Linux
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Sets human attributes
class Human():
    def __init__(self, name, weapon, weapon_min_damage, weapon_max_damage, health_max, health_current, potions, potion_strength, alive):
        self.name = name
        self.weapon = weapon
        self.weapon_min_damage = weapon_min_damage
        self.weapon_max_damage = weapon_max_damage
        self.health_current = health_current
        self.health_max = health_max
        self.potions = potions
        self.potion_strength = potion_strength
        self.alive = alive

    def human_attack(self):
        damage_amount = random.randrange(
            self.weapon_min_damage, self.weapon_max_damage)
        if damage_amount < enemy.health_current:
            enemy.health_current -= damage_amount
            print(
                f'{self.name} attacks with {self.weapon} and causes {damage_amount} damage!\n')
            input('Press any key to continue...')
            clear()
        else:
            print(
                f'{self.name} attacks with {self.weapon} and causes {damage_amount} damage!\n')
            input(f'You defeated {enemy.name}!\n\nPress any key to exit...')
            enemy.alive = False

    def take_potion(self):
        if self.potions >= 1:
            self.potions -= 1
            self.health_current = self.health_current + self.potion_strength
            print(
                f'{self.name} took a potion and restored {self.potion_strength} health!\n')
        else:
            print(f'{self.name} has no potions left!\n')
        input('Press any key to continue...')
        clear()

    def check_stats(self):
        print(f'Name: {self.name}')
        print(f'Weapon: {self.weapon}')
        print(f'Health: {self.health_current}/{self.health_max}')
        print(
            f'Potions: {self.potions}\n')
        input('Press any key to continue...')
        clear()


# Sets enemy attributes
class Enemy():
    def __init__(self, name, weapon, weapon_min_damage, weapon_max_damage, health_max, health_current, alive):
        self.name = name
        self.weapon = weapon
        self.weapon_min_damage = weapon_min_damage
        self.weapon_max_damage = weapon_max_damage
        self.health_max = health_max
        self.health_current = health_current
        self.alive = alive

    def enemy_attack(self):
        if enemy.health_current == 1:
            input(f'{self.name} ran away!!\n\nPress any key to exit...')
            self.alive = False
        else:
            if (random.randrange(0, 10) > 1):
                damage_amount = random.randrange(
                    self.weapon_min_damage, self.weapon_max_damage)
                if damage_amount < player.health_current:
                    player.health_current -= damage_amount
                    print(
                        f'{self.name} attacks {player.name} with {self.weapon} and causes {damage_amount} damage!\n')
                    input('Press any key to continue...')
                    clear()
                else:
                    print(
                        f'{self.name} attacks {player.name} with {self.weapon} and causes {damage_amount} damage!\n')
                    input(f'You died!\n\nPress any key to exit...')
                    player.alive = False
            else:
                print(f'{self.name} roars at {player.name}!\n')
                input('Press any key to continue...')
                clear()


# Set player data
clear()
player_name = input('Please enter your name\n> ').strip().title()
player_weapon = input('\nChoose your weapon\n> ').strip().title()
player_weapon_min_damage = 5
player_weapon_max_damage = 30
player_health_max = 100
player_health_current = player_health_max
player_potions = 1
player_potion_strength = 20
player_alive = True
player = Human(player_name, player_weapon, player_weapon_min_damage,
               player_weapon_max_damage, player_health_max, player_health_current, player_potions, player_potion_strength, player_alive)


# Set enemy data
enemy_name = input('\nEnter enemy name\n> ').strip().title()
enemy_weapon = input('\nEnter enemy weapon\n> ').strip().title()
enemy_weapon_min_damage = 5
enemy_weapon_max_damage = 40
enemy_health_max = 100
enemy_health_current = enemy_health_max
enemy_alive = True
enemy = Enemy(enemy_name, enemy_weapon, enemy_weapon_min_damage,
              enemy_weapon_max_damage, enemy_health_max, enemy_health_current, enemy_alive)

# Welcome message
clear()
input(f'Hello {player.name}, good luck surviving with that {player.weapon}!\n\nPress any key to start...')
clear()

print(f'You encounter a wild {enemy.name}!\n')

# Enter main loop
while player.alive and enemy.alive:
    print(f'{player.name} (HP: {player.health_current}/{player.health_max})\n{enemy.name} (HP: {enemy.health_current}/{enemy.health_max})\n')
    print('1. Attack | 2. Use Potion | 3. Stats')
    choice = input('\n> ')
    if choice == '1':
        clear()
        player.human_attack()
        if enemy.alive:
            enemy.enemy_attack()
    if choice == '2':
        clear()
        player.take_potion()
    if choice == '3':
        clear()
        player.check_stats()
    else:
        clear()
