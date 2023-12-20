import datetime

class Project:
    def __init__(self, name, start_date, priority, estimate, completion):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, " \
               f"estimate: ${self.estimate:.2f}, completion: {self.completion}%"

    def update_completion(self, new_completion):
        self.completion = new_completion

    def update_priority(self, new_priority):
        self.priority = new_priority


def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        header = lines[0].strip().split('\t')
        for line in lines[1:]:
            data = line.strip().split('\t')
            name = data[0]
            start_date = datetime.datetime.strptime(data[1], "%d/%m/%Y").date()
            priority = int(data[2])
            estimate = float(data[3])
            completion = int(data[4])
            project = Project(name, start_date, priority, estimate, completion)
            projects.append(project)
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("name\tstart_date\tpriority\testimate\tcompletion\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                       f"{project.estimate:.2f}\t{project.completion}\n")


def display_projects(projects):
    incomplete_projects = []
    completed_projects = []
    for project in projects:
        if project.completion < 100:
            incomplete_projects.append(project)
        else:
            completed_projects.append(project)

    print("Incomplete projects:")
    for project in sorted(incomplete_projects, key=lambda x: x.priority):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted(completed_projects, key=lambda x: x.priority):
        print(f"  {project}")


def filter_projects_by_date(projects, date):
    filtered_projects = []
    for project in projects:
        if project.start_date > date:
            filtered_projects.append(project)

    for project in sorted(filtered_projects, key=lambda x: x.start_date):
        print(f"{project}")


def add_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date_str = input("Start date (dd/mm/yyyy): ")
    start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))

    project = Project(name, start_date, priority, estimate, completion)
    projects.append(project)


def update_project(projects):
    print("Select a project to update:")
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]

    new_completion = int(input("New Percentage: "))
    project.update_completion(new_completion)

    new_priority = input("New Priority: ")
    if new_priority:
        project.update_priority(int(new_priority))


def main():
    projects = []
    filename = input("Enter the filename to load projects from: ")
    projects = load_projects(filename)

    while True:
        print("\n- (L)oad projects")
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
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
            filter_projects_by_date(projects, date)
        elif choice == 'a':
            add_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please try again.")

    print("Thank you for using custom-built project management software.")


if __name__ == "__main__":
    main()
