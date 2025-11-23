import multiprocessing
import time
import random

order_max = 20
oven_number = 3

class Oven:
    def __init__(self, oven_id, lock):
        self.oven_id = oven_id
        self.lock = lock

    def run(self, queue):
        with self.lock:
            if queue:
                order_id = queue.pop(0)
                print(f"Pec {self.oven_id} pece pizzu cislo {order_id}")
            else:
                print(f"Pec {self.oven_id} nepece, chladne")
                order_id = None

        time.sleep(random.randint(1, 2))

        if order_id is not None:
            with self.lock:
                print(f"Pec {self.oven_id} dopekla pizzu cislo {order_id}")

def customer_simulation(queue, lock):
    order_counter = 0

    while True:
        time.sleep(random.randint(3, 10)/10)
        with lock:
            if len(queue) >= order_max:
                print("Restaurace ma moc objednavek, neprijima nove")
                continue

            order_counter += 1
            queue.append(order_counter)
            print(f"Zakaznik si objednal pizzu cislo {order_counter}, v pizza fronte je {len(queue)} pizz")

def oven_start_sim(oven: Oven, queue):
    while True:
        oven.run(queue)

if __name__ == "__main__":
    manager = multiprocessing.Manager()
    queue = manager.list()
    lock = manager.Lock()
    ovens = []

    for i in range(1, oven_number + 1):
        oven = Oven(i, lock)
        p = multiprocessing.Process(target=oven_start_sim, args=(oven, queue))
        ovens.append(p)

    customersim = multiprocessing.Process(target=customer_simulation, args=(queue, lock))

    for oven in ovens:
        oven.start()
    customersim.start()

    for oven in ovens:
        oven.join()
    customersim.join()
