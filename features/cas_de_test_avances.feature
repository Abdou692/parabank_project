# language: fr
Fonctionnalité: Tests avancés ParaBank - Cas limites et erreurs

  # ============================================================================
  # CAS DE TEST CRÉATION DE COMPTE
  # ============================================================================
  
  Scénario: TC-CPT-10 - Refus de création de compte si solde source < 100$
    Étant donné l'utilisateur est connecté à ParaBank
    Quand il accède à Open New Account
    Et il choisit le type de compte "CHECKING"
    Et il sélectionne un compte source avec solde insuffisant (< 100$)
    Et il clique sur Open New Account
    Alors un message d'erreur doit s'afficher indiquant "solde insuffisant"
    Et le nouveau compte ne doit pas être créé

  # ============================================================================
  # CAS DE TEST PAIEMENT DE FACTURES
  # ============================================================================

  Scénario: TC-BP-02 - Paiement refusé si solde insuffisant
    Étant donné l'utilisateur est connecté à ParaBank pour le paiement de factures
    Quand il accède à Bill Pay
    Et il remplissage un paiement avec montant supérieur au solde disponible
    Et il soumet le paiement
    Alors un message d'erreur doit s'afficher indiquant "solde insuffisant"
    Et le paiement ne doit pas être confirmé

  Scénario: TC-BP-04 - Paiement avec montant négatif
    Étant donné l'utilisateur est connecté à ParaBank pour le paiement de factures
    Quand il accède à Bill Pay
    Et il remplit le formulaire avec :
      | payee   | address     | city   | state | zipCode | phone        | account | verifyAccount | amount |
      | John    | 123 Main St | Boston | MA    | 02101   | 617-555-0100 | 12345   | 12345         | -50    |
    Et il soumet le paiement
    Alors un message d'erreur doit s'afficher indiquant "montant invalide"
    Et le paiement ne doit pas être confirmé

  Scénario: TC-BP-05 - Paiement avec montant vide
    Étant donné l'utilisateur est connecté à ParaBank pour le paiement de factures
    Quand il accède à Bill Pay
    Et il remplit le formulaire avec :
      | payee   | address     | city   | state | zipCode | phone        | account | verifyAccount | amount |
      | John    | 123 Main St | Boston | MA    | 02101   | 617-555-0100 | 12345   | 12345         |        |
    Et il soumet le paiement
    Alors un message d'erreur doit s'afficher indiquant "montant obligatoire"
    Et le paiement ne doit pas être confirmé

  Scénario: TC-BP-09 - Nom bénéficiaire avec caractères spéciaux
    Étant donné l'utilisateur est connecté à ParaBank pour le paiement de factures
    Quand il accède à Bill Pay
    Et il remplit le formulaire avec :
      | payee   | address     | city   | state | zipCode | phone        | account | verifyAccount | amount |
      | John@#$ | 123 Main St | Boston | MA    | 02101   | 617-555-0100 | 12345   | 12345         | 100    |
    Et il soumet le paiement
    Alors soit le paiement doit être confirmé soit un message d'erreur s'affiche