import time
import requests

def medir_tempo(func_original):
    def wrapper():
        inicio = time.time() # Pega a hora atual do sistema
        r = func_original() # Executa a função original
        fim = time.time() # Pega a hora atual do sistema após a execução
        duracao = fim - inicio
        print(f"Tempo de Duração: {duracao:.3f} segundos")
        return r
    return wrapper

@medir_tempo
def buscar_API():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    print("Realizando GET")
    try:
        response = requests.get(url,timeout=10)
        response.raise_for_status() # ERRO: 404
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao realizar a requisição: {e}")
        return None
    
requisicao1 = buscar_API()
print(requisicao1)
