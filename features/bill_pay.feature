# language: fr
Fonctionnalité: Paiement de factures

Scénario: Paiement valide
    Étant donné l'utilisateur est connecté à ParaBank pour le paiement de factures
    Quand il accède à Bill Pay
    Et il remplit un paiement valide
    Et il soumet le paiement
    Alors le paiement est confirmé
