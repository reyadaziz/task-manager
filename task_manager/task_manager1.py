from storage import save_tasks, load_tasks
def add_task(title, description, due_date):
    tasks = load_tasks()
    task = {
        'title': title,
        'description': description,
        'due_date': due_date,
        'status': 'pending'
    }
    tasks.append(task)
    save_tasks(tasks)
def view_tasks():
    tasks = load_tasks()
    print("\nTasks list: \n")
    for i, task in enumerate(tasks, start = 1) :
        print( f"{i}. Title: {task['title']},Description:{task['description']}, Due Date: {task['due_date']}, Status: {task['status']}")
def remove_task(index):
    
    tasks = load_tasks()
    if 0<index<=len(tasks):
        del tasks [index-1]
        save_tasks(tasks)
    else:
        print("Invalid index")

def search_task(query):
    tasks = load_tasks()
    results = []
    for task in tasks:
        if query.lower() in task['title'].lower() or query.lower() in task ['description']:
            results.append(task)
    print("\nSearch Results: \n")
    for i, task in enumerate(results, start = 1) :  \
        print( f"{i}. Title: {task['title']},Description:{task['description']}, Due Date: {task['due_date']}, Status: {task['status']}")      
def update_task( index):

    tasks = load_tasks()
    if 0<index<=len(tasks):
        tasks[index-1]['status'] = "Completed"
        save_tasks(tasks)
    else:
        print("Invalid index")                   