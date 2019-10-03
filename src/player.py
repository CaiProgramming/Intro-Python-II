# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self,name,sex,age,room):
        self.name = name;
        self.sex = sex;
        self.age = str(age);
        self.room = room;
        self.items = [];
    def currentRoom(self):
        return self.room
    def changeRoom(self,room):
        self.room = room
    def addItems(self,item):
        self.items.append(item)
    def playerItems(self):
        return self.items
    def dropItem(self,x):
        self.items.remove(x)
    def __str__(self):
        return 'Name: ' + self.name + ' Age: ' + self.age + ' Sex: ' + self.sex
