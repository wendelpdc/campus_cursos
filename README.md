No código acima, terá a classe Campus, contendo os seguintes atributos da classe: código, nome e endereço. 
Esses atributos são para definir o campus. 
Ex: 2, Jardins de Anita, Itapajé. 

Dentro da classe Campus, será criado os métodos "add_curso" e "listar_curso" (fora o método especial "__init__", que é 
adicionado primeiramente para garantir a inicialização dos objetos).

Para ter uma melhor experiência, criei um menu interativo.
Nesse menu interativo tem presente 4 opções: 
1 - Criar campus 
2 - adicionar curso 
3 - listar cursos
4 - sair
Com isso, o programa ficou melhor e mais fácil de ser manipulado pelo usuário.

Estrutura do código (mais detalhada):
- A classe Campus contém métodos para adicionar cursos (add_curso) e listar cursos (listar_cursos).
- A função menu_interativo apresenta um menu no terminal com opções para criar campus, adicionar cursos, listar cursos ou sair do programa.
- O menu só permite operar nos cursos após um campus ser criado, garantindo a consistência dos dados.
- Ao executar o código, o menu é iniciado automaticamente possibilitando interação com o usuário.

Como usar
1. Execute o script Python em um terminal que suporte entrada interativa.
2. Use a opção "Criar campus" para definir os dados iniciais.
3. Utilize as opções para adicionar novos cursos e listar os existentes.
4. Encerre o programa pela opção "Sair".
