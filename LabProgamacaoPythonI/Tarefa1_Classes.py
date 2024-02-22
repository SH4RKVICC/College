class Filme:
    def __init__(self, nome, diretor, genero, lancamento):
        self.nome = nome
        self.diretor = diretor
        self.genero = genero
        self.lancamento = lancamento

#criar instâncias das classes para cada filme
anyone_but_you = Filme("Anyone But You", "Will Gluck", "Romance", 2023)
la_la_land = Filme("La La Land", "Damian Chazelle", "Musical", 2017)
poor_things = Filme("Poor Things", "Yorgos Lanthimos", "Comédia, Ficção Científica", 2023)

#organizar os filmes em um dicionário
filmes = {
    "Romance": [anyone_but_you],
    "Musical": [la_la_land],
    "Comedia": [poor_things],
    "Ficcao_cient": [poor_things]
}

#solicitar ao usuário um gênero
genero_usuario = input("Digite o gênero desejado (Romance, Musical, Comedia, Ficcao cient): ")

#exibir informações sobre os filmes do gênero escolhido
if genero_usuario in filmes:
    filmes_genero = filmes[genero_usuario]

    for filme in filmes_genero:
        print("\nFilme:", filme.nome)
        print("Diretor:", filme.diretor)
        print("Gênero:", filme.genero)
        print("Lançamento:", filme.lancamento)
        print("----")
else:
    print("Por favor, escolha uma categoria válida.")
