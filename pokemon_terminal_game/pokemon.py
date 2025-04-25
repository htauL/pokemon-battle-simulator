class Pokemon:
    def __init__(self, name, type1, type2, hp, atk, defense, sp_atk, sp_def, speed, moves):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.max_hp = hp
        self.current_hp = hp
        self.atk = atk
        self.defense = defense
        self.sp_atk = sp_atk
        self.sp_def = sp_def
        self.speed = speed
        self.moves = moves
        self.fainted = False

    def take_damage(self, damage):
        self.current_hp -= damage
        if self.current_hp <= 0:
            self.current_hp = 0
            self.fainted = True