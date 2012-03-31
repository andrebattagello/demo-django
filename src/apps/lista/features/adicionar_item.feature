# language: pt-br

Funcionalidade: Adicionar itens a lista
    Como um usuário
    Para que eu possa aumentar o que devo lembrar de fazer
    Eu gostaria de acrescentar um item a minha lista

    Cenário: Adicionar item válido a lista
        Dado que exista uma lista vazia
        Quando eu adicionar o item "Item1" a lista
        Então eu devo ser apresentado com os seguintes itens:
            | nome  | completo |
            | Item1 |   0      |
