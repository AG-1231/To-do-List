import json
import os
 

SAVE_FILE = "my_todos.json"
 
 
def load_todos()
    if not os.path.exists(SAVE_FILE):
        return []
    with open(SAVE_FILE, "r") as f:
        return json.load(f)
 
 
def save_todos(todos):
    with open(SAVE_FILE, "w") as f:
        json.dump(todos, f, indent=2)
 
 
def show_todos(todos):
    if not todos:
        print("\n  nothing here yet! add something.\n")
        return
 
    print("\n  your todos:")
    print("  " + "-" * 30)
    for i, item in enumerate(todos, start=1):
        status = "x" if item["done"] else " "
        print(f"  [{status}] {i}. {item['task']}")
    print("  " + "-" * 30 + "\n")
 
 
def add_todo(todos):
    task = input("  what do you need to do? ").strip()
    if not task:
        print("  you didn't type anything, try again.")
        return
    todos.append({"task": task, "done": False})
    save_todos(todos)
    print(f"  added: '{task}'")
 
 
def mark_done(todos):
    if not todos:
        print("  no todos to mark!")
        return
 
    show_todos(todos)
    try:
        num = int(input("  which number did you finish? ")) - 1
        if num < 0 or num >= len(todos):
            print("  that number doesn't exist")
            return
        todos[num]["done"] = True
        save_todos(todos)
        print(f"  nice, marked '{todos[num]['task']}' as done!")
    except ValueError:
        print("  that's not a number...")
 
 
def delete_todo(todos):
    if not todos:
        print("  nothing to delete!")
        return
 
    show_todos(todos)
    try:
        num = int(input("  which number do you want to delete? ")) - 1
        if num < 0 or num >= len(todos):
            print("  that number doesn't exist")
            return
        removed = todos.pop(num)
        save_todos(todos)
        print(f"  deleted '{removed['task']}'")
    except ValueError:
        print("  type a number please")
 
 
def clear_done(todos):
    before = len(todos)
    todos[:] = [t for t in todos if not t["done"]]
    after = len(todos)
    save_todos(todos)
    removed = before - after
    if removed == 0:
        print("  no completed todos to clear")
    else:
        print(f"  cleared {removed} completed todo(s)")
 
 
def main():
    todos = load_todos()
 
    print("\n  === my todo list ===")
 
    while True:
        print("  what do you want to do?")
        print("  1. show todos")
        print("  2. add a todo")
        print("  3. mark one as done")
        print("  4. delete a todo")
        print("  5. clear all completed")
        print("  6. quit")
 
        choice = input("\n  pick a number: ").strip()
 
        if choice == "1":
            show_todos(todos)
        elif choice == "2":
            add_todo(todos)
        elif choice == "3":
            mark_done(todos)
        elif choice == "4":
            delete_todo(todos)
        elif choice == "5":
            clear_done(todos)
        elif choice == "6":
            print("\n  bye! don't forget your todos :)\n")
            break
        else:
            print("  hmm, pick a number between 1 and 6")
 
 
if __name__ == "__main__":
    main()
