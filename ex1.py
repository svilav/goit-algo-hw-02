import queue
import time
import threading
import random


def generate_request(q, request_id):
    """Функція для генерації нових заявок."""
    print(f"Генеруємо заявку з ID: {request_id}")
    q.put(request_id)


def process_request(q):
    """Функція для обробки заявок."""
    while True:
        try:
            request_id = q.get(timeout=3)
            print(f"Обробляємо заявку з ID: {request_id}")
            time.sleep(random.randint(1, 3))
            q.task_done()
        except queue.Empty:
            print("Черга пуста, чекаємо на нові заявки...")
            break


def main():
    q = queue.Queue()
    request_id = 0

    processing_thread = threading.Thread(target=process_request, args=(q,))
    processing_thread.start()

    try:
        while True:
            time.sleep(2)
            generate_request(q, request_id)
            request_id += 1
    except KeyboardInterrupt:
        print("Завершення програми...")

    q.join()
    processing_thread.join()


if __name__ == "__main__":
    main()
