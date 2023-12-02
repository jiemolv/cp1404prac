def get_data():
    input_file = open(FILENAME)
    data = []

    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        data.append(parts)

    input_file.close()
    return data
def display_subject_details(data):
    for subject in data:
        subject_code = subject[0]
        lecturer = subject[1]
        student_count = subject[2]
        print(f"{subject_code} is taught by {lecturer} and has {student_count} students")
