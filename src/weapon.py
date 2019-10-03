from item import Item
class Weapon(Item):
    def __init__(self,name,weight,desc,damage,type):
        super().__init__(name, weight,desc,type)
        self.damage = damage
    def itemDamage(self):
        return self.damage
