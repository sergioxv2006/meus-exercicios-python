class CDs:
    def __init__(self, titulo: str, ano: int, ehDuplo: bool = False, ehColetania: bool = False):
        self.titulo = titulo
        self.ano = ano
        self.ehDuplo = ehDuplo
        self.ehColetania = ehColetania
        self.musicas = []
        self.musicos = []

    def __str__(self):
        return f"CD: {self.titulo} ({self.ano}) - {'Duplo' if self.ehDuplo else 'Simples'} - {'Coletânea' if self.ehColetania else 'Original'}"

    def cadastrar(self):
        print(f"CD '{self.titulo}' cadastrado com sucesso!")

    def adicionar_musica(self, musica):
        self.musicas.append(musica)
        musica.cds.append(self)

    def adicionar_musico(self, musico):
        self.musicos.append(musico)
        musico.cds.append(self)

    @staticmethod
    def listarCDS_Musica(musica, lista_cds):
        cds_da_musica = []
        for cd in lista_cds:
            if musica in cd.musicas:
                cds_da_musica.append(cd)
        return cds_da_musica

    @staticmethod
    def listarCDS_Musico(musico, lista_cds):
        cds_da_musico = []
        for cd in lista_cds:
            if musico in cd.musicos:
                cds_da_musico.append(cd)
        return cds_da_musico
    
    def listar_musicas(self):
        print(f"\nMúsicas do CD '{self.titulo}':")
        if self.musicas:
            for musica in self.musicas:
                print(f"  - {musica.nome} ({musica.tempoFaixa} min)")
        else:
            print("  Nenhuma música cadastrada.")

    def listar_musicos(self):
        print(f"\nMúsicos do CD '{self.titulo}':")
        if self.musicos:
            for musico in self.musicos:
                print(f"  - {musico.nome} ({'Solo' if musico.ehSolo else 'Banda'})")
        else:
            print("  Nenhum músico cadastrado.")

class Musico:
    def __init__(self, nome: str, ehSolo: bool = True):
        self.nome = nome
        self.ehSolo = ehSolo
        self.cds = []

    def __str__(self):
        return f"Músico: {self.nome} ({'Solo' if self.ehSolo else 'Banda'})"

    def cadastrar(self):
        print(f"Músico '{self.nome}' cadastrado com sucesso!")

class Musica:
    def __init__(self, nome: str, tempoFaixa: float):
        self.nome = nome
        self.tempoFaixa = tempoFaixa
        self.cds = []

    def __str__(self):
        return f"Música: {self.nome} - Duração: {self.tempoFaixa} min"

    def cadastrar(self):
        print(f"Música '{self.nome}' cadastrada com sucesso!")

# Criando Músicos
print("=== CADASTRANDO MÚSICOS ===")
roberto_carlos = Musico("Roberto Carlos", True)
roberto_carlos.cadastrar()

elis_regina = Musico("Elis Regina", True)
elis_regina.cadastrar()

tim_maia = Musico("Tim Maia", True)
tim_maia.cadastrar()

# Criando Músicas
print("\n=== CADASTRANDO MÚSICAS ===")
musica1 = Musica("Como É Grande o Meu Amor Por Você", 3.40)
musica1.cadastrar()

musica2 = Musica("Águas de Março", 4.20)
musica2.cadastrar()

musica3 = Musica("Não Quero Dinheiro", 2.50)
musica3.cadastrar()

# Criando CDS
print("\n=== CADASTRANDO CDS ===")
cd1 = CDs("As melhores do Roberto Carlos", 1995, True)
cd1.cadastrar()

cd2 = CDs("Elis Regina - Ao Vivo", 1980, False)
cd2.cadastrar()

cd3 = CDs("Tim Maia - Grandes Sucessos", 2000, True)
cd3.cadastrar()

# Configurando Relações (Músicas -> CDS)
print("\n=== ADICIONANDO MÚSICAS E MÚSICOS AOS CDS ===")
cd1.adicionar_musica(musica1)
cd1.adicionar_musico(roberto_carlos)

cd2.adicionar_musica(musica2)
cd2.adicionar_musico(elis_regina)

cd3.adicionar_musica(musica3)
cd3.adicionar_musico(tim_maia)

print("Relações configuradas com sucesso!")

# Lista de todos os CDs
todos_cds = [cd1, cd2, cd3]
# Exibindo informações detalhadas dos objetos
print("\n=== INFORMAÇÕES DETALHADAS DOS OBJETOS ===")
print(f"\n{roberto_carlos}")
print(f"{musica1}")
print(f"{cd1}")

# Listando músicas e músicos de cada CD
print("\n=== LISTAGEM DE MÚSICAS E MÚSICOS POR CD ===")
cd1.listar_musicas()
cd1.listar_musicos()

cd2.listar_musicas()
cd2.listar_musicos()

cd3.listar_musicas()
cd3.listar_musicos()

# Buscando CDs por músico
print("\n=== BUSCAS ESPECÍFICAS ===")
print("\nCDs do Roberto Carlos:")
cds_roberto = CDs.listarCDS_Musico(roberto_carlos, todos_cds)
for cd in cds_roberto:
    print(f"  - {cd.titulo}")

print("\nCDs que contêm a música 'Como É Grande o Meu Amor Por Você':")
cds_musica1 = CDs.listarCDS_Musica(musica1, todos_cds)
for cd in cds_musica1:
    print(f"  - {cd.titulo}")

# Resumo final
print("\n=== RESUMO FINAL ===")
print(f"Total de CDs cadastrados: {len(todos_cds)}")
print(f"Total de músicos cadastrados: 3")
print(f"Total de músicas cadastradas: 3")

print("\nInformações resumidas:")
for cd in todos_cds:
    print(f"  {cd.titulo}: {len(cd.musicas)} música(s) e {len(cd.musicos)} músico(s)")