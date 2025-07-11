import json
from datetime import datetime
import os

def load_tasks(filename="tasks.json"):
    try:
        if not os.path.exists(filename):
            initial_data = []
            with open(filename, 'w') as file:
                json.dump(initial_data, file, indent=4)
            print(f"File {filename} sakhte shod.")
            return initial_data
        
        with open(filename, 'r') as file:
            return json.load(file)
            
    except Exception as e:
        print(f"Error dar load file: {e}")
        return []

def save_tasks(tasks, filename="tasks.json"):
    try:
        with open(filename, 'w') as file:
            json.dump(tasks, file, indent=4)
        print("Liste karha ba movafaghiat zakhire shod.")
    except Exception as e:
        print(f"Error dar zakhire file: {e}")

def add_task(tasks):
    print("\n--- Ezafe kardan kar jadid ---")
    task_name = input("Name kar jadid ra vared konid: ")
    while True:
        priority = input("Olaviat (bala/motevaset/payin): ").lower()
        if priority in ['bala', 'motevaset', 'payin']:
            break
        print("Lotfan yeki az gozinehaye 'bala', 'motevaset' ya 'payin' ra vared konid.")
    
    due_date = input("Tarikh anjam (YYYY-MM-DD) (ekhtiari - Enter baraye rad kardan): ")
    
    new_task = {
        'name': task_name,
        'priority': priority,
        'added': datetime.now().strftime("%Y-%m-%d"),
        'due_date': due_date if due_date else None,
        'completed': False
    }
    
    tasks.append(new_task)
    print(f"\nKar '{task_name}' ba movafaghiat ezafe shod!")
    save_tasks(tasks)

def show_tasks(tasks, sort_by='priority'):
    if not tasks:
        print("\nListe karha khali ast!")
        return
    
    if sort_by == 'priority':
        priority_order = {'bala': 1, 'motevaset': 2, 'payin': 3}
        tasks.sort(key=lambda x: priority_order.get(x['priority'], 4))
    elif sort_by == 'name':
        tasks.sort(key=lambda x: x['name'])
    elif sort_by == 'due_date':
        tasks.sort(key=lambda x: x['due_date'] or '9999-12-31')
    
    print("\nListe karha:")
    print("=" * 50)
    for i, task in enumerate(tasks, 1):
        status = "✓" if task['completed'] else " "
        priority_text = ""
        if task['priority'] == 'bala':
            priority_text = "BALA"
        elif task['priority'] == 'motevaset':
            priority_text = "MOTEVASET"
        else:
            priority_text = "PAYIN"
        
        print(f"{i}. [{status}] {priority_text} {task['name']}")
        print(f"   Ezafe shode dar: {task['added']}")
        if task['due_date']:
            print(f"   Moead anjam: {task['due_date']}")
    print("=" * 50)

def complete_task(tasks):
    if not tasks:
        print("\nListe karha khali ast!")
        return
    
    show_tasks(tasks)
    try:
        task_num = int(input("\nShomare kare anjam shode ra vared konid: ")) - 1
        if 0 <= task_num < len(tasks):
            if tasks[task_num]['completed']:
                print(f"Kar '{tasks[task_num]['name']}' ghablan anjam shode bud!")
            else:
                tasks[task_num]['completed'] = True
                print(f"\nKar '{tasks[task_num]['name']}' be onvan anjam shode alamat zade shod!")
                save_tasks(tasks)
        else:
            print("Shomare kar namotabar ast!")
    except ValueError:
        print("Lotfan yek adad vared konid!")

def delete_task(tasks):
    if not tasks:
        print("\nListe karha khali ast!")
        return
    
    show_tasks(tasks)
    try:
        task_num = int(input("\nShomare kari ke mikhahid hazf konid ra vared konid: ")) - 1
        if 0 <= task_num < len(tasks):
            deleted_task = tasks.pop(task_num)
            print(f"\nKar '{deleted_task['name']}' ba movafaghiat hazf shod!")
            save_tasks(tasks)
        else:
            print("Shomare kar namotabar ast!")
    except ValueError:
        print("Lotfan yek adad vared konid!")

def main():
    print("\n" + "=" * 50)
    print("Sistem modiriyat liste karha".center(50))
    print("=" * 50)
    
    tasks = load_tasks()
    
    while True:
        print("\nMenu asli:")
        print("1. Namayeshe karha")
        print("2. Ezafe kardan kar jadid")
        print("3. Alamat zadan kare anjam shode")
        print("4. Hazfe kar")
        print("5. Khoruj")
        
        choice = input("\nGozine mored nazar ra entekhab konid (1-5): ")
        
        if choice == '1':
            print("\nRavesh moratab sazi:")
            print("1. Bar asase olaviat")
            print("2. Bar asase name")
            print("3. Bar asase tarikh anjam")
            sort_choice = input("Gozine moratab sazi ra entekhab konid (1-3): ")
            
            if sort_choice == '1':
                show_tasks(tasks, 'priority')
            elif sort_choice == '2':
                show_tasks(tasks, 'name')
            elif sort_choice == '3':
                show_tasks(tasks, 'due_date')
            else:
                print("Gozine namotabar! Namayesh be soorate pishfarz (olaviat)")
                show_tasks(tasks)
                
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("\n" + "=" * 50)
            print("Taghirat zakhire shod. Khodahafez!".center(50))
            print("=" * 50)
            break
        else:
            print("Gozine namotabar! Lotfan adad beyne 1 ta 5 vared konid.")

if __name__ == "__main__":
    main()