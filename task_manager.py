import json
import os
from datetime import datetime

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.filename = "tasks.json"
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    self.tasks = json.load(file)
            except:
                self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, description):
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'completed': False,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print("Tarefa adicionada com sucesso!")

    def list_tasks(self):
        if not self.tasks:
            print("Nenhuma tarefa encontrada.")
            return

        print("\nLista de Tarefas:")
        for task in self.tasks:
            status = "✓" if task['completed'] else " "
            print(f"[{status}] {task['id']}. {task['description']}")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                print("Tarefa marcada como concluída!")
                return
        print("Tarefa não encontrada.")

    def remove_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print("Tarefa removida com sucesso!")
                return
        print("Tarefa não encontrada.")

def main():
    task_manager = TaskManager()
    
    while True:
        print("\n=== Gerenciador de Tarefas ===")
        print("1. Listar tarefas")
        print("2. Adicionar tarefa")
        print("3. Marcar tarefa como concluída")
        print("4. Remover tarefa")
        print("5. Sair")
        
        choice = input("\nEscolha uma opção: ")
        
        if choice == "1":
            task_manager.list_tasks()
        
        elif choice == "2":
            description = input("Digite a descrição da tarefa: ")
            task_manager.add_task(description)
        
        elif choice == "3":
            task_manager.list_tasks()
            task_id = int(input("Digite o ID da tarefa a ser concluída: "))
            task_manager.complete_task(task_id)
        
        elif choice == "4":
            task_manager.list_tasks()
            task_id = int(input("Digite o ID da tarefa a ser removida: "))
            task_manager.remove_task(task_id)
        
        elif choice == "5":
            print("Programa encerrado.")
            break
        
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main() 