students = ["Germione", "Harry", "Ron"]

for i in range(len(students)):
    print(i+1, students[i])

# gryffindors = {student: "Gryffindor" for student in students}

# gryffindors = [{"name": student, "house":"Gryffindor"} for student in students] 

# for student in students:
#     gryffindors.append({"name":  student, "house":"Gryffindor"})

# print(gryffindors)


# Students = [
#     {"name":"Hermione", "house":"Gryffindor"},
#     {"name":"Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house":"Gryffindor"},
#     {"name":"Draco","house":"Slytherin" },
# ]

# def is_gryffindor(s):
#     return s["house"] == "Gryffindor"


# gryffindors =  filter(is_gryffindor, Students)

# for gryffindor in sorted(gryffindors,key=lambda s : s["name"]):
#     print(gryffindor["name"])


# gryffindors = [
#     student["name"] for student in students if student["house"]=="Gryffindor"
# ]


# for gryffindor in sorted(gryffindors):
#     print(gryffindor)

