class Task:
    def __init__(self, nome, descricao):
        if not nome or nome.strip() == "":
            raise ValueError("O nome da tarefa é obrigatório.")
        self.nome = nome
        self.descricao = descricao
        self.status = "em andamento"

    def mark_done(self):
        if self.status == "concluída":
            raise ValueError("A tarefa já está concluída.")
        self.status = "concluída"

    def mark_in_progress(self):
        if self.status == "concluída":
            raise ValueError("Não é possível marcar como 'em andamento' uma tarefa concluída.")
        self.status = "em andamento"

    def edit(self, novo_nome, nova_descricao):
        if not novo_nome or novo_nome.strip() == "":
            raise ValueError("O nome da tarefa é obrigatório.")
        self.nome = novo_nome
        self.descricao = nova_descricao


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, nome, descricao):
        task = Task(nome, descricao)
        self.tasks.append(task)

    def find_task(self, nome):
        for task in self.tasks:
            if task.nome == nome:
                return task
        return None

    def mark_done(self, nome):
        task = self.find_task(nome)
        if not task:
            raise ValueError("Tarefa não encontrada.")
        task.mark_done()

    def mark_in_progress(self, nome):
        task = self.find_task(nome)
        if not task:
            raise ValueError("Tarefa não encontrada.")
        task.mark_in_progress()

    def edit_task(self, nome, novo_nome, nova_descricao):
        task = self.find_task(nome)
        if not task:
            raise ValueError("Tarefa não encontrada.")
        task.edit(novo_nome, nova_descricao)

    def remove_task(self, nome):
        task = self.find_task(nome)
        if not task:
            raise ValueError("Tarefa não encontrada.")
        self.tasks.remove(task)
