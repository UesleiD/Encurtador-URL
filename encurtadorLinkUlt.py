from io import TextIOBase
import pickle
import os,time
from math import floor
from tkinter import N


class Encurtador:
    def __init__(self):
        self.dic = {}
        self.nome_arq = "urls.dat"
        self.__load_dic()
        self.indice = 1000 + len(self.dic)

    def __load_dic(self):
        # testar se arquivo existe
        if os.path.isfile(self.nome_arq):
            print("Arquivo existe")
            # carregar dicionario do arquivo .. variavel self.nome_arq
            with open(self.nome_arq, "rb") as f:
                self.dic = pickle.load(f)
        else:
            return

    def __save_dic(self):
        # salvar dicionario no arquivo .. variavel self.nome_arq
        with open(self.nome_arq, "wb") as f:
            pickle.dump(self.dic, f)

    def toBase(self, num, b = 62):
        if b <= 0 or b > 62:
            return 0
        base = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
        r = num % b
        res = base[r];
        q = floor(num / b)
        while q:
            r = q % b
            q = floor(q / b)
            res = base[int(r)] + res
        return res

    def to10(self, num, b = 62):
        base = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
        limit = len(num)
        res = 0;
        for i in range(limit):
            res = b * res + base.find(num[i])
        return res

    def encurtar(self, url):
        # salvar no dicionario usando como chave o valor da variavel self.indice
        # o valor a ser salvo é uma tupla onde a posicao 0 eh o indice convertido
        # para string usando base62 e a posicao 1 eh a url original
        # nao esqueca de incrementar a variavel self.indice   
        # e por fim, chamar o metodo __save_dic para salvar o dicionario no arquivo em disco.  
        self.dic[self.indice] = (self.toBase(self.indice), url)
        self.__save_dic()
        return self.dic[self.indice]

    def buscar(self, url_curta):
        indice = self.to10(url_curta)
        return self.dic[indice][1] # retorna a 2a posicao da tupla

    def listar_urls(self):
        print(self.dic)

def menu():
    while True:
        escolha = int(input("Escolha uma opção:\n(1) - Converter a URL\n(2) - Converter um inteiro para String\n(3) - Converter uma string para um inteiro\n(4) - Mostrar a tabela hash\n(5) - Sair\n---"))
        if escolha == 1:
            #Conversão de URL
            url = str(input("Digite a url: "))
            urlNew = e.encurtar(url)
            print("A url convertida é: " , urlNew)      
        elif escolha == 2:
            inteiro = int(input("Digite o inteiro: "))
            #conversão do inteiro para string
            inteiroConvert = e.toBase(inteiro)
            print("O inteiro convertido para string é: " , inteiroConvert)       
        elif escolha == 3:
            string = str(input("Digite uma string: "))
            #Conversão da string para inteiro
            stringConvert = e.to10(string)
            print("A string convertida para inteiro é: " , stringConvert)       
        elif escolha == 4:
            print("A tabela hash é:\n" , e.__dict__)   
        elif escolha == 5:
            quit()
        else:
            print("Opção Inválida!") 
        verNovamente = str(input('Quer escolher outra opção? (s/n)? '))
        if verNovamente == 's':
            print('Aguarde...logo o programa irá reiniciar.')
            time.sleep(2)
            os.system('cls')
        else:
            quit()

e = Encurtador()
menu()