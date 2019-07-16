class Player:

    def __init__(self, player_name, player_money, player_life):
        
        self.player_name  = player_name
        self.player_money = player_money
        self.player_life  = player_life
    


    # Getters & Setters
    def get_player_name(self):
        return self.player_name
    
    def get_player_money(self):
        return self.player_money

    def get_player_life(self):
        return self.player_life
    
    def set_player_name(self, player_name):
        self.player_name = player_name
    
    def set_player_money(self, player_money):
        self.player_money = player_money

    def set_player_life(self, player_life):
        self.player_life = player_life
    



    # Methods
    def add_player_money(self, money):
        self.set_player_money(self.get_player_money() + money)
    
    def deal_player_life_damage(self, damage):
        self.set_player_life(self.get_player_life - damage)


