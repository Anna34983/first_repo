from typing import Dict
from enum import Enum
from datetime import datetime
import asyncio

# Definicja statusów zadań
class TaskStatus(Enum):
    PENDING = "pending"         # Zadanie oczekujące na przetworzenie
    PROCESSING = "processing"   # Zadanie w trakcie przetwarzania
    COMPLETING = "completing"   # Zadanie przetworzone poprawnie
    FAILED = "failed"           # Zadanie zakończone błędem

# Definicja priorytetów zadań - wyższy numer = wyższy priorytet
class TaskPriority(Enum):
    LOW = 1         # Niski
    MEDIUM = 2      # Średni
    HIGH = 3        # Wysoki

class Task:
    def __init__(self, task_id: str, data: Dict, priority: TaskPriority = TaskPriority.MEDIUM):
        self.task_id = task_id              # Unikalny identyfikator zadania
        self.data = data                    # Dane wejściowe
        self.status = TaskStatus.PENDING    # Początkowy status
        self.priority = priority            # Priorytet zadania
        self.created_at = datetime.now()    # Odcisk czasu utworzenia zadania
        self.error = None                   # Miejsce na przechowywanie ewentualnych błędów


class SimlpeOrchestrator:
    def __init__(self):
        # Słownik przechowujący wszystkie zadania
        self.tasks: Dict[str, Task] = {}
        # Zbiór zadań aktualnie przetwarzanych
        self.processing_tasks: set = set()

    async def add_task(self, task_id: str, data: Dict, priority: TaskPriority = TaskPriority.MEDIUM):
        """
        Dodaje nowe zadanie do orkiestratora.
        Zadania są dodawane do słownika i czekają na przetworzenie.
        """
        task = Task(task_id, data, priority)        # Tworzymu instancję klasy Task z zadaniem
        self.tasks[task_id] = task                  # Dodajemy zadanie do słownika
        print(f"Dodano zadanie: {task_id} z priorytetem {priority.name}")
        return task_id                              # Zwracamy task_id


# Metoda asynchroniczna main
async def main():
    orchestrator = SimlpeOrchestrator()         # Tworzymy orkiestrator

    task_id = await orchestrator.add_task(      # Dodajemy statyczne dane do zadania
        "task1",
        {
            "station_id": "STATION001",
            "temperature": 32.5,
            "humanity": 80
         },
        TaskPriority.HIGH
    )



if __name__ == "__main__":
    asyncio.run(main())