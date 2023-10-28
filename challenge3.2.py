class student:
    def__init__(self, name, roll_number, cgpa):
        self.name=name
        self.roll_number=roll_number
        self.cgpa=cgpa


def sort_student(student_list):
    #sort the list of student in descending order of cgpa
    sorted_student=sorted(student_list,
                          key=Lambda student:student.cgpa,
                          reverse=True)
    return sorted_student


# example usage:
student=[
    student("Hari","A123",7.8),
    student("srikath","A123",9.1),
    student("saumya","A125",9.1),
    student("Mahidhar","A126",9.9),
]

sorted_student=sort_student(student

#print the sorted list of student
for student in sorted_student:
    print("name:{},Roll number:{}".format(student.name,

student.roll_number,
                                           student.cgpa))
