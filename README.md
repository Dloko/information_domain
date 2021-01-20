# information_domain
Esse código é usado para encontrar informações de um certo site e domínios relacionados.
# como usar
Ao executar o código, ele vai aparecer um "@" na frente você vai escrever o domínio(Aviso: sem www, gov e etc), precisa ter um arquivo para armazenar as informações (por exemplo: teste.txt ou você pode criar seu proprio arquivo), você também precisa de uma wordlist com possiveis subdomínios(por exemplo o "lista_teste.txt" que esta junto ao arquivo do codigo) o "teste.txt" e o "lista_teste.txt" ja são pre-definido como padrão para mudar teria que entra no codigo
e mudar(não recomendo).
# como funciona(basico)
O código primeiramente deleta tudo dentro do "teste.txt", por mais que o código seja em python, ele usa alguns comandos do sistema como "whois", "sort -u", também usa algumas bibliotecas do python como "os".
