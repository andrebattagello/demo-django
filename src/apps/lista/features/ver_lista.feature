# language: pt-br

Funcionalidade: Ver lista completa de items
    Como um usuário
    Para que eu possa saber todos os items
    Eu gostaria de visualizar a lista completa de items

    Cenário: Lista vazia
        Dado que exista uma lista vazia
        Quando eu ver a lista
        Então eu devo ser apresentado com "Lista Vazia"


    Cenário: Lista não é vazia
        Dado que exista uma lista com os seguintes itens:
            | nome  | completo |
            | Item1 |   0      |
            | Item2 |   0      |
        Quando eu ver a lista
        Então eu devo ser apresentado com "Lista contém 2 itens"
            E eu devo ser apresentado com os seguintes itens:
                | nome  | completo |
                | Item1 |   0      |
                | Item2 |   0      |
