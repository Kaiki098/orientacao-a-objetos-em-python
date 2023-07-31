class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
        
    def __eq__(self, programa):
        return self._nome == programa    
    
    @property
    def likes(self):
        return self._likes
    
    def dar_like(self):
        self._likes += 1
        
    @property    
    def nome(self):
        return self._nome
        
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
        
    def __str__(self) -> str:
        return f'{self._nome} - {self.ano} - {self._likes} Likes'

class Filme(Programa):
    
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    
    def __str__(self) -> str:
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'    
  
class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    def __str__(self) -> str:
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'  
    
class Playlist:  
    
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
        
    def __eq__(self, programa):
        return programa in self._programas
        
    def __getitem__(self, item):
        return self._programas[item]
    
    def __len__(self):
        return len(self._programas)
    
vingadores = Filme('vingadores - guerra infinita', 2018, 160)  
atlanta = Serie('Atlanta', 2018, 2)

programas = [vingadores, atlanta]

minha_playlist = Playlist("minha_playlist", programas)

incriveis = Filme('Os incríveis', 2005, 100)
xmen = Filme("X-men: o filme", 1999, 100)

outros_programas = [incriveis, xmen]
outra_playlist = Playlist("Fim de semana", outros_programas)

for programa in minha_playlist:
    print(programa)
    
for programa in outra_playlist:
    print(programa)

print(f'Tamanho da playlist: {len(minha_playlist)}')

if 'Atlanta' == outra_playlist:
    print('aaa') 
else:
    print('bbb')