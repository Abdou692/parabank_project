# language: fr
Fonctionnalité: Création compte

Scénario: Création compte CHECKING
    Étant donné l'utilisateur est connecté à ParaBank
    Quand il accède à Open New Account
    Et il choisit le type de compte "CHECKING"
    Et il sélectionne un compte source
    Et il clique sur Open New Account
    Alors le nouveau compte est créé avec succès

Scénario: Création compte SAVINGS
    Étant donné l'utilisateur est connecté à ParaBank
    Quand il accède à Open New Account
    Et il choisit le type de compte "SAVINGS"
    Et il sélectionne un compte source
    Et il clique sur Open New Account
    Alors le nouveau compte est créé avec succès
