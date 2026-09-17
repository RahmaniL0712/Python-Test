task_priorities = {
    1: 'E larte',
    2: 'E mesme',
    3: 'E ulet'
}
class User:
    def __init__(self, name, level, experience, tasks):
        self.name = name
        self.level = level
        self.experience = experience
        self.tasks = tasks

    def level_up(self, exp):
        self.experience = self.experience + exp
        if self.experience >= 100:
            self.level = self.level + 1
            print(f'U ngritet ne nivel! Ju arritet nivelin {self.level}!')
            self.experience = self.experience - 100
    
    def add_task(self, task):
        self.tasks.append(task)
        print('Detyra u regjistrua me sukses. Ju fituat 25 pike!')
        self.level_up(25)
    
    def list_tasks(self, menu_popup=True):
        if not self.tasks:
            add_task_input = input('Nuk keni detyra te regjistruara per momentin. Deshironi te shtoni nje detyre te re? (y/n) ').lower()
            if add_task_input == 'y':
                add_task(self)
        else:
            print('-'*80)
            print('Detyrat aktuale:')
            for number, task in enumerate(self.tasks, start=1):
                print(f'\n{number}. {task["Name"]}')
                print(f'   Kategoria: {task["Category"]}')
                print(f'   Prioriteti: {task_priorities[task["Priority"]]}')
                print(f'   Statusi: {task["Status"]}')
        if menu_popup:
                print('-'*80)
                input('Shtypni Enter per tu kthyer ne menune kryesore. ')
                

    def complete_task(self):
        incomplete_tasks = []
        for task in self.tasks:
            if task['Status'] is not 'Perfunduar':
                incomplete_tasks.append(task)
        if not incomplete_tasks:
            input('Nuk keni detyra te pa perfunduara. Shtypni Enter per tu kthyer ne menune kryesore. ')
        else:
            print('-'*80)
            print('Detyrat e pa perfunduara:')
            for number, task in enumerate(incomplete_tasks, start=1):
                print(f'\n{number}. {task["Name"]}')
                print(f'   Kategoria: {task["Category"]}')
                print(f'   Prioriteti: {task_priorities[task["Priority"]]}')
                print(f'   Statusi: {task["Status"]}')
            while True:
                try:
                    task_number = int(input('Cilen detyre do te perfundosh? '))
                    if task_number not in range(1, len(incomplete_tasks)+1):
                        print(f'Shkruani nje numer midis 1 dhe {len(incomplete_tasks)}')
                        continue
                    break
                except ValueError:
                    print('Shkruani nje numer per te perzgjedhur detyren e caktuar.')
            
            task = incomplete_tasks[task_number-1]
            task['Status'] = 'Perfunduar'
            print('Detyra perfundoi. Ju fituat 100 pike!')
            self.level_up(100)
            complete_another_task = input('Deshironi te perfundoni nje detyre tjeter? (y/n) ').lower()
            if complete_another_task == 'y':
                self.complete_task()
        
    def show_statistics(self):
        print('-'*80)
        print('Statistikat tuaja:')
        print("Emri:", self.name)
        print("Niveli:", self.level)
        print("Pikat e nevojshme per nivelin e ardhshem:", 100-self.experience)
        print(f'Detyrat totale: {len(self.tasks)}')
        counter_comp = 0
        for task in self.tasks:
            if task['Status'] == 'Perfunduar':
                counter_comp = counter_comp + 1
        print(f'    Te perfunduara: {counter_comp}')
        print(f'    Te pa perfunduara: {len(self.tasks)-counter_comp}')
        print('-'*80)
        input('Shtypni Enter per tu kthyer ne menune kryesore. ')
    
def registration_menu():
    print('Mire se vini. Ju lutem regjistroni te dhenat tuaja per te filluar.')
    name = input('Emri: ')
    user = User(name, 0, 0, [])
    main_menu(user)

def add_task(user):
    task_name = input('Titulli: ')
    task_category = input('Kategoria: ')
    while True:
        try:
            task_priority = int(input('''Prioriteti:
    1. E larte
    2. E mesme
    3. E ulet
    '''))
            if task_priority not in range(1, 4):
                print("Zgjidhni nje numer nga 1 deri ne 3.")
                continue
            break
        except ValueError:
            print('Shkruani nje numer.')

    task = {
        'Name': task_name,
        'Category': task_category,
        'Priority': task_priority,
        'Status': 'Hapur'
    }
    user.add_task(task)
    add_again = input('Deshironi te shtoni nje detyre tjeter? (y/n) ').lower()
    if add_again == 'y':
        add_task(user)


def main_menu(user):
    running = True
    while running:
        print('-'*80)
        print('''Mire se vini ne menune kryesore. Zgjidhni nje nga opsionet:
    1. Shiko detyrat
    2. Shto nje detyre
    3. Perfundo nje detyre
    4. Shiko statistikat
    5. Dil''')
        while True:
            try:
                user_input = int(input())

                if user_input not in range(1, 6):
                    print("Zgjidhni nje numer nga 1 deri ne 5.")
                    continue
                break
            except ValueError:
                print("Shkruani nje numer.")

        if user_input == 1:
            user.list_tasks()
        elif user_input == 2:
            add_task(user)
        elif user_input == 3:
            user.complete_task()
        elif user_input == 4:
            user.show_statistics()
        elif user_input == 5:
            running = False

registration_menu()

