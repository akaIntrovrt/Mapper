from Controller.Controller import Controller

controller = Controller()

dto = controller.getAllBooksDTO()
entity = controller.getAllBooksEntity()

for i in dto:
    print(i.__dict__)
print("\n")
for i in entity:
    print(i.__dict__)