from Model.Model import ModelEntity
from Mapper import UserMapper

class Controller:
    def __init__(self):
        self.books = [
            ModelEntity(57832346, "ic-01", "George Orwell", 200, "cob-c2"),
            ModelEntity(545825849,"Brave New World","Aldous Huxley", 100, "c-o1b" ),
          ]

    def getAllBooksDTO(self):
        return [UserMapper.getDTO(book) for book in self.books]
    def getAllBooksEntity(self):
        return [UserMapper.getEnity(book) for book in self.books]
