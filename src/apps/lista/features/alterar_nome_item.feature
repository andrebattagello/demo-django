# language: pt-br


Funcionalidade: Alterar o nome do item
    Como um usuário
    Para que eu possa corrigir o que tenho pra fazer
    Eu gostaria de mudar o nome de um item

    Cenário: Novo nome é válido
        Dado que exista uma lista com os seguintes itens:
            | nome  | completo |
            | Item1 |   0      |
            | Item2 |   0      |
        Quando eu mudar o nome do "Item2" para "Item2-modificado"
        Então eu devo ser apresentado com "Item2-modificado"

    Cenário: Novo nome é inválido
        Dado que exista uma lista com os seguintes itens:
            | nome  | completo |
            | Item1 |   0      |
            | Item2 |   0      |
        Quando eu mudar o nome do "Item2" para ""
        Então eu devo ser apresentado com "Este campo é obrigatório"
