class Teacher:
    def __init__(self, first_name="", last_name="", teacher_id=-1) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.teacher_id = teacher_id

    def from_dict(self, teacher_dict):
        self.first_name = teacher_dict["first_name"]
        self.last_name = teacher_dict["last_name"]
        self.teacher_id = teacher_dict["teacher_id"]

    def to_dict(self):
        teacher_dict = {"first_name": self.first_name,
                        "last_name": self.last_name,
                        "teacher_id": self.teacher_id}
        return teacher_dict

    def __str__(self) -> str:
        st = f"\nName       : {self.first_name}"
        st += f"\nLast Name  : {self.last_name}"
        st += f"\nTeacher ID : {self.teacher_id}"
        return st
