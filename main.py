import asyncio
import random
import time

max_sleep_time = 10
start_time = time.time()

def get_time():
    return round(time.time() - start_time, 2)

def log(message):
    current_time = get_time()
    print(f"{current_time}s: {message}")


async def task_A():
    time_to_sleep = random.randint(1, max_sleep_time)
    log(f"task A sleeping for {time_to_sleep} s") 
    await asyncio.sleep(time_to_sleep)
    log(f"task A finished in {time_to_sleep} s")

async def task_B():
    time_to_sleep = random.randint(1, max_sleep_time)
    log(f"task B sleeping for {time_to_sleep} s")
    await asyncio.sleep(time_to_sleep)
    log(f"task B finished in {time_to_sleep} s")

async def task_C():
    time_to_sleep = random.randint(1, max_sleep_time)
    log(f"task C sleeping for {time_to_sleep} s")
    await asyncio.sleep(time_to_sleep)
    log(f"task C finished in {time_to_sleep} s")

async def loop_ABC():
    while True:
        log("#################################################")
        taskA = asyncio.create_task(task_A())
        taskB = asyncio.create_task(task_B())
        taskC = asyncio.create_task(task_C())
        # await taskA
        # await taskB
        # await taskC
        task_list = [taskA, taskB, taskC]
        # results = await asyncio.gather(taskA, taskB, taskC)
        done, pending = await asyncio.wait(task_list, return_when = asyncio.FIRST_COMPLETED)
        for pending_task in pending:
            pending_task.cancel()

        log("\n\n\n")
        await asyncio.sleep(0.100)


async def continuous_task():
    while True:
        await asyncio.sleep(5)
        log("Im saying hi every 5 seconds")

async def main_loop():
    loop_ABC_task = asyncio.create_task(loop_ABC())
    loop_ABC_task = asyncio.create_task(continuous_task())
    await asyncio.gather(loop_ABC_task, loop_ABC_task, return_exceptions=False)

    


asyncio.run(main_loop())