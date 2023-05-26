import asyncio

async def my_process():
    print('process start')
    await asyncio.sleep(2)  # 等待同時將控制權拿回來，先執行後面步驟
    print('process end')

async def main():
    print('main start')
    await asyncio.gather(my_process(), my_process())  # 這裡常會忘記加await
    print('main end')

asyncio.run(main())  # 執行整個異步程式