file_name = 'students.txt'


def add(first_name, last_name, age, city, student_id):
	with open(file_name, 'a') as file:
		file.write(f'{first_name},{last_name},{age},{city},{student_id}\n')


def lists():
	with open(file_name, 'r') as file:
		students = []
		lines = [line.strip().split(',') for line in file.readlines()]
		for line in lines:
			students.append({
				'first_name': line[0],
				'last_name': line[1],
				'age': line[2],
				'city': line[3],
				'student_id': line[4]
			})
	return students


def save_student(students):
	with open(file_name, 'w') as file:
		for student in students:
			file.write(f"{student['first_name']},{student['last_name']},{student['age']},{student['city']},{student['student_id']}")


def delete(student_id):
	students = lists()
	new_students = []
	for student in students:
		if student['student_id']!=student_id:
			new_students.append(student)
		save_student(students)


def update(student_id, key, new_data):
	students = lists()
	for student in students:
		if student['student_id']==student_id:
			student[key]=new_data
	save_student(students)

def detail(student_id):
	students = lists()
	for student in students:
		if student['student_id']==student_id:
			return student



user_choice = """
Enter:
- 'a' to add student 
- 'l' to list of student
- 'r' to delete a student
- 'd' to update a student
- 'i' to get detail of one student
- 'q' to quit

Your choice:"""

def add_student():
	first_name = input('enter your first name\n')
	last_name = input('enter your last name\n')
	age = int(input('enter your age\n'))
	city = input('enter your city\n')
	student_id = input('enter student id\n')
	add(first_name, last_name,age, city, student_id)

def lists_student():
	students = lists()
	for student in students:
		print(f"first_name: {student['first_name']}")
		print(f"last_name: {student['last_name']}")
		print(f"age: {student['age']}")
		print(f"city: {student['city']}")
		print(f"student_id: {student['student_id']}")

def delete_student():
	student_id = input('enter student id\n')
	delete(student_id)

def update_student():
	student_id = input('enter student id\n')
	key = input('enter key\n')
	new_data = input('enter new data\n')
	update(student_id, key, new_data)

def detail_student():
	student_id = input('enter student id\n')
	student = detail(student_id)
	print(f"first_name: {student['first_name']}")
	print(f"last_name: {student['last_name']}")
	print(f"age: {student['age']}")
	print(f"city: {student['city']}")
	print(f"student_id: {student['student_id']}")


def menu():
	choice = input(user_choice)
	while choice!='q':
		if choice=='a':
			add_student()
		elif choice=='l':
			lists_student()
		elif choice=='r':
			delete_student()
		elif choice=='d':
			update_student()
		elif choice == 'i':
			detail_student()
		else:
			print('Unknown command try again\n')
		choice = input(user_choice)
menu()