class Tower:

    def __init__(self, name, damage, aspd, attack_range):
        self.tower_name = name
        self.tower_damage = damage
        self.tower_aspd = aspd
        self.tower_attack_range = attack_range
    


    # Getters & Setters
    def get_tower_name(self):
        return self.tower_name
    
    def get_tower_damage(self):
        return self.tower_damage
    
    def get_tower_aspd(self):
        return self.tower_aspd
    
    def get_tower_attack_range(self):
        return self.tower_attack_range
    

    def set_tower_name(self, name):
        self.tower_name = name

    def set_tower_damage(self, damage):
        self.tower_damage = damage
    
    def set_tower_aspd(self, aspd):
        self.tower_apsd = aspd
    
    def set_tower_attack_range(self, attack_range):
        self.tower_attack_range = attack_range

