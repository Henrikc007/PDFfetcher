import asyncio

async def main():
    print('hello')
    task = asyncio.create_task(foo(1))
    await task
    print("heyheyhey")

async def foo(sekunder):
    await asyncio.sleep(sekunder)
asyncio.run(main())
print('world')