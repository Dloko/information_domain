# information_domain
Esse código é usado para encontrar informações de um certo site e domínios relacionados.
# como usar
Ao executar o código, ele vai aparecer um "@" na frente você vai escrever o domínio(Aviso: sem www, gov e etc), precisa ter um arquivo para armazenar as informações (por exemplo: teste.txt) e uma wordlist com possiveis subdomínios(por exemplo como a que esta na junto do arquivo do codigo).
# como funciona 
O código primeiramente deleta tudo dentro do "teste.txt", por mais que o código seja em python, ele usa alguns comandos do sistema como "whois", "sort -u", também usa algumas bibliotecas do python como "os".
