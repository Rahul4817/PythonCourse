# class Student:
#     def __init__(self, name, dob, erp_no):
#         self.name = name
#         self._dob = dob  # protect data member
#         self.__erp_no = erp_no  # private data member
#
#     def show(self):
#         print(self.__erp_no)
#
#
# s = Student("ABC", "15 - 07 - 2004", "147230")
# print(s.name)
# print(s._dob)
# print(s._Student__erp_no)
# s.show()


import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="task",
            message="once upon time",
            timeout=10
        )
        time.sleep(3600)


