import asyncio

async def cozinhar():
    print("Cozinhando... " )
    await asyncio.sleep(8)
    print("Prato pronto! ")
    
async def limpar():
    print("Limpando... " )
    await asyncio.sleep(6)
    print("Limpeza concluída! ")

async def main():
    # Executa as duas tarefas ao mesmo tempo
    await asyncio.gather(cozinhar(), limpar())
    
# Inicia o loop de eventos
asyncio.run(main())