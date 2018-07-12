from student import Student
from teacher import Teacher

def main():
    t = Teacher("王飞", 30, "男", "象棋", 5)
    t.show()
    t.teach()
    t.play()
    s = Student("小明", 15, "男", "足球", "00023102")
    s.show()
    s.study()
    s.play()


if __name__ == "__main__":
    main()