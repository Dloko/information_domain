# information_domain
Esse código é usado para encontrar informações de um certo site e domínios relacionados.
# como usar
Ao executar o código você precisa escrever um domínio(Aviso: sem www, gov e etc), precisa ter um arquivo para armazenar as informações (no meu caso teste.txt) e uma wordlist (lista_teste.txt).
# como funciona 
O código primeiramente deleta tudo dentro do "teste.txt", por mais que o código seja em python, ele usa alguns comandos do sistema como "whois", "sort -u", também usa algumas bibliotecas do python como "os".
