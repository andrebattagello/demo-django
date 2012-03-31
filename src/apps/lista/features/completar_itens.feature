# language: pt-br

Funcionalidade: Completar itens da lista
    Como um usuário
    Para que eu possa gravar o meu andamento nas minhas tarefas
    Eu gostaria de marcar alguns itens como Completos

    Cenário: Marcar item como completo
        Dado que exista uma lista com os seguintes itens:
            | nome  | completo |
            | Item1 |   0      |
            | Item2 |   0      |
        Quando eu marcar o "Item2" como completo
        Então eu devo verificar que o "Item2" realmente está completo

    Cenário: Marcar item como imcompleto
        Dado que exista uma lista com os seguintes itens:
            | nome  | completo |
            | Item1 |   1      |
            | Item2 |   0      |
        Quando eu marcar o "Item2" como incompleto
        Então eu devo verificar que o "Item2" realmente está incompleto

