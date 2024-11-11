import asyncio

async def main():
    print('hello')
    task = asyncio.create_task(foo(3,"1"))
    task2 = asyncio.create_task(foo(1,"2"))
    print('world')
    # await(task)
    # await(task2)
    task

   
    

async def foo(sekunder,str):
    
    await asyncio.sleep(sekunder)
    print("heyheyhey"+str)
    




asyncio.run(main())
