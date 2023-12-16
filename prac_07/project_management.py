import datetime

from project import Project


def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        header = file.readline().strip().split('\t')
        for line in file:
            data = line.strip().split('\t')
            project = Project(*data)
            projects.append(project)
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        header = ['Name', 'Start Date', 'Priority', 'Estimate', 'Completion']
        file.write('\t'.join(header) + '\n')
        for project in projects:
            data = [project.name, project.start_date, project.priority, project.estimate, project.completion]
            file.write('\t'.join(data) + '\n')


def display_projects(projects):
    incomplete = [project for project in projects if project.completion < 100]
    completed = [project for project in projects if project.completion == 100]

    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")

    print("Completed projects:")
    for project in completed:
        print(f"  {project}")


def filter_projects_by_date(projects):
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        filtered_projects = [project for project in projects if project.start_date > date]
        for project in filtered_projects:
            print(f"  {project}")
    except ValueError:
        print("Invalid date format.")


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date_string = input("Start date (dd/mm/yyyy): ")
    try:
        start_date = datetime.datetime.strptime(start_date_string, "%d/%m/%Y").date()
        priority = int(input("Priority: "))
        estimate = input("Cost estimate: ")
        completion = int(input("Percent complete: "))

        project = Project(name, start_date, priority, estimate, completion)
        projects.append(project)
        print("New project added successfully.")
    except ValueError:
        print("Invalid date or priority value.")


def update_project(projects):
    print_projects(projects)
    try:
        choice = int(input("Project choice: "))
        if 0 <= choice < len(projects):
            project = projects[choice]
            new_completion = int(input("New Percentage: "))
            new_priority = input("New Priority: ")

            if new_completion != '':
                project.completion = new_completion
            if new_priority != '':
                project.priority = new_priority

            print("Project updated successfully.")
        else:
            print("Invalid project choice.")
    except ValueError:
        print("Invalid project choice.")


def print_menu():
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")


def main():
    projects = []
    filename = input("Enter the filename for projects data: ")

    while True:
        print_menu()
        choice = input(">>> ").lower()

        if choice == 'l':
            projects = load_projects(filename)
        elif choice == 's':
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
