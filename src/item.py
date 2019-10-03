class Item:
    def __init__(self,name,weight,desc,type):
        self.name = name
        self.weight = weight
        self.desc = desc
        self.type = type
    def itemName(self):
        return self.name
    def itemWeight(self):
        return self.weight
    def itemDesc(self):
        return self.desc
    def itemType(self):
        return self.type
