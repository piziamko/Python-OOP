class Equipment:
    id_ = 0

    def __init__(self, name):
        self.name = name
        self.id = 1

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        Equipment.id_ += 1
        return Equipment.id_
