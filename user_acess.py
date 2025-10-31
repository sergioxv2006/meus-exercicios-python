import functools

context_user = {"usuario_logado": None}

def login_requerido(func_original):
    @functools.wraps(func_original)
    def wrapper(*args, **kwargs):
        # Verificação de autenticação
        if context_user["usuario_logado"] is None:
            print("ACESSO NEGADO - Usuário não autenticado.")
            # Redirecionar para login ou outra ação apropriada
            return
        else:
            print(f"Acesso permitido para {func_original.__name__}")
            return func_original(*args, **kwargs)
    return wrapper

@login_requerido
def painel_usuario(nome_usuario):
    print(f"Bem-vindo ao seu painel, {nome_usuario}")
    return "Página do Painel do Usuário"

def pagina_inicial():
    print("Bem-vindo à página inicial!")

pagina_inicial()
r_painel1 = painel_usuario("Falha")
print(r_painel1)

# Simulando Login de Usuário
context_user["usuario_logado"] = "usuario123"
r_painel2 = painel_usuario("usuario123")
print(r_painel2)