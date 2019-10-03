# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self,name,desc,id,map,items):
        self.name = name
        self.desc = desc
        self.id = id
        self.map = map
        self.items = items
    def roomName(self):
        return self.name
    def roomDesc(self):
        return self.desc
    def roomId(self):
        return self.id
    def roomMap(self):
        return self.map
    def roomItems(self):
        return self.items
    def removeItem(self,x):
        self.items.remove(x)
        return self.items
