# project.py

import datetime

class Project:
    def __init__(self, name, start_date, priority, estimate, completion):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: {self.estimate:.2f}, completion: {self.completion}%"

    def update_completion(self, new_completion):
        self.completion = new_completion

    def update_priority(self, new_priority):
        self.priority = new_priority

def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        header = lines[0]
        for line in lines[1:]:
            fields = line.strip().split('\t')
            name = fields[0]
            start_date = datetime.datetime.strptime(fields[1], "%d/%m/%Y").date()
            priority = int(fields[2])
            estimate = float(fields[3])
            completion = int(fields[4])
            project = Project(name, start_date, priority, estimate, completion)
            projects.append(project)
    return projects

def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tEstimate\tCompletion\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.estimate:.2f}\t{project.completion}\n")


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion < 100]
    completed_projects = [project for project in projects if project.completion == 100]

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")
    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")

def filter_projects_by_date(projects):
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date > filter_date]
    filtered_projects.sort(key=lambda project: project.start_date)

    print("Filtered projects:")
    for project in filtered_projects:
        print(f"  {project}")

def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date_string = input("Start date (dd/mm/yyyy): ")
    start_date = datetime.datetime.strptime(start_date_string, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))

    project = Project(name, start_date, priority, estimate, completion)
    projects.append(project)
    print("New project added successfully!")

def update_project(projects):
    print("Current projects:")
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    choice = int(input("Project choice: "))
    project = projects[choice]

    new_completion = int(input("New percentage complete: "))
    project.update_completion(new_completion)

    new_priority = input("New priority (leave blank to retain existing value): ")
    if new_priority:
        project.update_priority(int(new_priority))

    print("Project updated successfully!")

def main():
    filename = input("Enter the filename to load projects from: ")
    projects = load_projects(filename)

    while True:
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")

        choice = input(">>> ").lower()

        if choice == 'l':
            filename = input("Enter the filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter the filename to save projects to: ")
            save_projects(filename, projects)
            print("Projects saved successfully!")
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
