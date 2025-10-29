# --- Classe Auxiliar ---
# O exercício menciona que a Playlist armazena "objetos Musica".
# Vamos criar uma classe simples para representar uma música.
class Musica:
    def __init__(self, nome, artista):
        self.nome = nome
        self.artista = artista

    # Usamos o __repr__ para que, ao imprimir uma música, 
    # vejamos uma representação clara dela.
    def __repr__(self):
        return f"Musica(nome='{self.nome}', artista='{self.artista}')"
    
# --- Classe Principal ---
class Playlist:
    """
    Implementa uma classe Playlist usando métodos mágicos
    conforme o exercício.
    """

    # Requisito Base: nome e lista interna
    def __init__(self, nome):
        self.nome = nome
        self.musicas = [] # Lista interna para guardar as Músicas
    
    # Método auxiliar para adicionar músicas (necessário para os testes)
    def add_musica(self, musica):
        if isinstance(musica, Musica):
            self.musicas.append(musica)
        else:
            print("Erro: Apenas objetos da classe Musica podem ser adicionados.")
    
    # Requisito 1: __str__
    # Define o que acontece ao usar print(playlist)
    def __str__(self):
        num_musicas = len(self.musicas)
        # Lógica simples para "música" vs "músicas"
        texto_musicas = "música" if num_musicas == 1 else "músicas"
        return f"Playlist '{self.nome}' ({num_musicas} {texto_musicas})"
    
    # Requisito 2: __repr__
    # Define a representação "oficial" do objeto
    def __repr__(self):
        return f"Playlist(nome='{self.nome}')"
    
    # Requisito 3: __len__
    # Define o que acontece ao usar len(playlist)
    def __len__(self):
        return f"Playlist(nome='{self.nome}')"
    
    # Requisito 3: __len__
    # Define o que acontece ao usar len(playlist)
    def __len__(self):
        return len(self.musicas)
    
    # Requisito 4: __getitem__
    # Define o que acontece ao usar playlist[indice] 
    def __getitem__(self, index):
        return self.musicas[index]
    
    # Requisito 5: __add__
    # Define o que acontece ao usar playlist1 + playlist2
    def __add__(self, outra_playlist):
        # Verificamos se o outro item é uma Playlist
        if not isinstance(outra_playlist, Playlist):
            return NotImplemented
        
        # 1. Criar um novo nome (conforme o exemplo "Mix: Rock + Pop")
        novo_nome = f"Mix: {self.nome} + {outra_playlist.nome}"

        # 2. Criar a nova playlist
        nova_playlist = Playlist(novo_nome)

        # 3. Combinar as listas de músicas
        # Não usamos add_musica aqui para ser mais direto
        nova_playlist.musicas = self.musicas + outra_playlist.musicas

        # 4. Retornar a nova playlist
        return nova_playlist
    
# --- Código de Teste ---

# 1. Criar algumas músicas
m1 = Musica("Bohemian Rhapsody", "Queen")
m2 = Musica("Stairway to Heaven", "Led Zeppelin")
m3 = Musica("Come As You Are", "Nirvana")
m4 = Musica("Back in Black", "AC/DC")

# 2. Criar duas playlists
playlist_rock = Playlist("Rock Clássico")
playlist_rock.add_musica(m1)
playlist_rock.add_musica(m2)

playlist_hard_rock = Playlist("Hard Rock")
playlist_hard_rock.add_musica(m3)
playlist_hard_rock.add_musica(m4)

print("--- Testando Playlist ---")

# Teste Requisito 1: __str__
print(f"\n[Teste __str__]:\n {playlist_rock}")

# Teste Requisito 2: __repr__
print(f"\n[Teste __repr__]:\n {repr(playlist_rock)}")

# Teste Requisito 3: __len__
print(f"\n[Teste __len__]:\n Comprimento: {len(playlist_rock)} músicas")

# Teste Requisito 4: __getitem__
print(f"\n[Teste __getitem__]:\n Primeira música: {playlist_rock[0]}")

# Teste Requisito 5: __add__
print("\n[Teste __add__]:")
playlist_mix = playlist_rock + playlist_hard_rock

# Testando a nova playlist (nome, tamanho e conteúdo)
print(f" Nova Playlist (str): {playlist_mix}")
print(f" Nova Playlist (len): {len(playlist_mix)} músicas")
print(f" Terceira música do mix: {playlist_mix[2]}")