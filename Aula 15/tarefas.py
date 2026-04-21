import asyncio

async def tarefa(nome, tempo):
	print(f"Iniciando {nome}")
	await asyncio.sleep(tempo)
	print(f"Finalizando {nome}")

async def main():
	await asyncio.gather(
		tarefa("Tarefa 1", 4),
		tarefa("Tarefa 2", 1),
		tarefa("Tarefa 3", 2)
	)

asyncio.run(main())