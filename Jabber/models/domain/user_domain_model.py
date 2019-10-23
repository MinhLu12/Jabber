import uuid

class UserDomainModel():
    def __init__(self, request):
        self.id = uuid.uuid4()
        self.name = request.name
        self.age = request.age
