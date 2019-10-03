from item import Item
class Potion(Item):
    def __init__(self,name,weight,desc,effect,type):
        super().__init__(name, weight,desc,type)
        self.effect = effect
    def itemEffect(self):
        return self.effect
