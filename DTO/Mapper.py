from DTO import  BookDTO
from Model.Model import ModelEntity


class UserMapper:

    @staticmethod
    def getDTO(entity: ModelEntity):
        return BookDTO(
            entity.id, entity.title, entity.author
        )
    @staticmethod
    def getEnity(entity: ModelEntity):
        return ModelEntity(
            entity.id, entity.title, entity.author, entity.price, entity.internal_code
        )