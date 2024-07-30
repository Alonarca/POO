# IMPORTAR BIBLIOTECA
import random

# CLASSE JOGADOR
class Jogador:
    def __init__(self, nome, escolha=None):
        self.nome = nome
        self.escolha = None
       
    def EscolherJogada(self):
        pass


# CLASSE HUMANO
class Humano(Jogador):
    def __init__(self, nome, escolha=None):
        super().__init__(nome, escolha)
       
    def EscolherJogada(self):
        while True:
            escolha = input(
                """QUAL É SUA JOGADA?
                PEDRA
                PAPEL
                TESOURA
               
                Digite Aqui:
                """
            )
            if escolha.upper() in ["PEDRA", "PAPEL", "TESOURA"]:
                self.escolha = escolha.upper()
                break
            else:
                print("Por favor! Apenas as três opções destacadas!")


# CLASSE COMPUTADOR
class Computador(Jogador):
    def __init__(self, nome, escolha=None):
        super().__init__(nome, escolha)
       
    def EscolherJogada(self):
        self.escolha = random.choice(["PEDRA", "PAPEL", "TESOURA"])


# CLASSE JOGO
class Jogo:
    # inicializar
    def __init__(self):
        self.humano = Humano("Humano")
        self.computador = Computador("Computador")
        self.placar = {"Humano": 0, "Computador": 0}


    # definir vencedor
    def DefinirVencedor(self):
        humano = self.humano.escolha
        computador = self.computador.escolha
        if humano == computador:
            return None
        #condições de ganho do humano
        elif ((humano == "PEDRA" and computador == "TESOURA") or
              (humano == "PAPEL" and computador == "PEDRA") or
              (humano == "TESOURA" and computador == "PAPEL")):
            return "Humano"
        #condição de ganho do computador
        else:
            return "Computador"


    # jogar partida
    def JogarPartida(self):
        #loop infinito
        while True:
            self.humano.EscolherJogada()
            self.computador.EscolherJogada()
            print(f"A jogada do {self.humano.nome} foi {self.humano.escolha}")
            print(f"A jogada do {self.computador.nome} foi {self.computador.escolha}")
            vencedor = self.DefinirVencedor()
            if vencedor:
                print(f"O vencedor foi {vencedor}")
                self.placar[vencedor] += 1
            else:
                print("Houve um empate")
            resposta = input(
                """Deseja continuar jogando?
                SIM - S
                NÃO - N
                """
            )
            #interromper loop
            if resposta.upper() != "S":
                break
        print(
            f"""O PLACAR FINAL FOI:
            HUMANO: {self.placar["Humano"]}
            COMPUTADOR: {self.placar["Computador"]}
            """
        )


jogo = Jogo()
jogo.JogarPartida()
