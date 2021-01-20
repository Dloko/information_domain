#Importar bibliotecas.
import os
import requests
import subprocess

#Abre o arquivo em mode escrita(mais so escreve ao final do texto).
teste = open('teste.txt','a')
#Apaga tudo dentro do .txt e escreve dentro do .txt '=======informações======='.
delete = os.popen('echo =======informações======= > teste.txt').read()

#Printa um aviso.
print('AVISO: sem www')
#Entrada para saber qual dominio sera testado.
dominio = input('@ ')

#O codigo ira executar o whois no dominio dentro da variavel 'dominio', vai da um '| grep' para separa uma certa informação depois vai dar 'sort -u' para não repetir informações e joga tudo para o arquivo chamado "teste.txt"(tudo e executado dentro do shell).
whois1 = subprocess.run('whois ' + dominio + " |grep 'domain:' |sort -u  >> teste.txt ", shell=True)
whois2 = subprocess.run('whois ' + dominio + " |grep 'e-mail:' |sort -u  >> teste.txt ", shell=True)
whois3 = subprocess.run('whois ' + dominio + " |grep 'contact:'|sort -u  >> teste.txt ", shell=True)
whois4 = subprocess.run('whois ' + dominio + " |grep 'name:' |sort -u >> teste.txt ", shell=True)
whois5 = subprocess.run('whois ' + dominio + " |grep 'address:' |sort -u  >> teste.txt ", shell=True)
whois6 = subprocess.run('whois ' + dominio + " |grep 'organisation:' |sort -u >> teste.txt ", shell=True)
whois7 = subprocess.run('whois ' + dominio + " |grep 'phone:' |sort -u >> teste.txt ", shell=True)
whois8 = subprocess.run('whois ' + dominio + " |grep 'fax-no:' |sort -u  >> teste.txt ", shell=True)

#abre o arquivo teste.txt em modo leitura.
teste2 = open('teste.txt','r').read()
#printa oque contem no arquivo.
print(teste2)

#abre em modo leitura uma wordlist
lista = open('lista_teste.txt','r').readlines()#(e usado "readlines()" para que leia em forma de lista).

#vai escrever dentro do teste.txt "=======domínios=======".
teste.write('=======domínios=======')
#printa "=======domínios=======".
print('=======domínios=======')

for linha in lista:

    linha = linha.rstrip('\n')#ira usar r.strip na linha para remover o "\n"(espaço entre linhas).

    url = 'http://' + linha + '.' + dominio#vai juntar a string "http://", variavel 'linha', string '.' e a variavel 'dominio' tudo dentro da variavel url.
    #o try aqui vai servi para se der algum error ele direcionar para o except
    try:
        r = requests.get(url) 
        #o if e para se saber se o site esta online(codigo 200).
        if r.status_code == 200:
            #vai printa falando que a linha existe.
            print(linha, ' existe')
            #dentro do arquivo 'teste.txt' vai dar um '\n'(espaço).
            teste.write('\n')
            #ainda dentro do 'teste.txt' vai anotar a variavel 'url'.
            teste.write(url)
    #except aqui serve para quando ocorrer error e não encontrar o site.
    except:
        #printa a variavel 'linha' como a string ' não existe'.
        print(linha, ' nao existe')
    