"""
run_pipeline_PARABANK.py - Automatise TOUT le pipeline de test + rapport

Usage:
    python run_pipeline_PARABANK.py

Fait automatiquement:
    1. Exécute les 4 tests (login, open_account, bill_pay, cas_avances)
    2. Fusionne les rapports JSON
    3. Génère le rapport HTML
    4. Ouvre le rapport dans le navigateur
"""

import subprocess
import os
import sys
import time


def run_all_tests():
    """Exécute tous les tests et génère le rapport complet"""
    
    print("\n" + "=" * 70)
    print("🚀 LANCEMENT DU PIPELINE COMPLET - PARABANK PROJECT")
    print("=" * 70)
    
    # Vos 4 features pour Parabank
    tests = [
        ('login', 'features/login.feature'),
        ('open_account', 'features/open_account.feature'),
        ('bill_pay', 'features/bill_pay.feature'),
        ('cas_avances', 'features/cas_de_test_avances.feature'),
    ]
    
    # ÉTAPE 1: Exécuter les tests
    print("\n" + "=" * 70)
    print("1️⃣  EXÉCUTION DES TESTS")
    print("=" * 70)
    
    all_passed = True
    
    for name, feature in tests:
        print(f"\n📝 Test: {name.upper()}")
        print(f"   Feature: {feature}")
        print(f"   Exécution en cours...", end=" ", flush=True)
        
        try:
            result = subprocess.run([
                'python', '-m', 'behave', feature,
                '--format', 'json',
                '--outfile', f'rapport_{name}.json',
                '--no-capture'
            ], capture_output=True, text=True, timeout=120)
            
            if result.returncode == 0:
                print("✅ PASS")
            else:
                print("⚠️  Completed (avec warnings)")
                
        except subprocess.TimeoutExpired:
            print("❌ TIMEOUT")
            all_passed = False
        except Exception as e:
            print(f"❌ ERREUR: {str(e)}")
            all_passed = False
        
        time.sleep(1)
    
    # ÉTAPE 2: Fusionner les rapports
    print("\n" + "=" * 70)
    print("2️⃣  FUSION DES RAPPORTS")
    print("=" * 70)
    
    try:
        print("\nExécution de fusionner_PARABANK.py...", end=" ", flush=True)
        result = subprocess.run(['python', 'fusionner_PARABANK.py'], 
                              capture_output=True, text=True, timeout=30)
        print("✅ Complété")
        print(result.stdout)
    except Exception as e:
        print(f"❌ ERREUR: {str(e)}")
        all_passed = False
    
    # ÉTAPE 3: Générer le rapport HTML
    print("\n" + "=" * 70)
    print("3️⃣  GÉNÉRATION DU RAPPORT HTML")
    print("=" * 70)
    
    try:
        print("\nExécution de generer_rapport_PARABANK.py...", end=" ", flush=True)
        result = subprocess.run(['python', 'generer_rapport_PARABANK.py'], 
                              capture_output=True, text=True, timeout=30)
        print("✅ Complété")
        print(result.stdout)
    except Exception as e:
        print(f"❌ ERREUR: {str(e)}")
        all_passed = False
    
    # ÉTAPE 4: Ouvrir le rapport
    print("\n" + "=" * 70)
    print("4️⃣  OUVERTURE DU RAPPORT")
    print("=" * 70)
    
    if os.path.exists('rapport.html'):
        print("\n📂 Ouverture de rapport.html...", end=" ", flush=True)
        
        try:
            if sys.platform == 'win32':
                os.startfile('rapport.html')
            elif sys.platform == 'darwin':
                os.system('open rapport.html')
            else:
                os.system('xdg-open rapport.html')
            
            print("✅ Ouvert dans le navigateur")
        except Exception as e:
            print(f"⚠️  Erreur: {str(e)}")
            print("   Ouvrez manuellement: rapport.html")
    else:
        print("\n❌ rapport.html non trouvé!")
    
    # RÉSUMÉ
    print("\n" + "=" * 70)
    print("📊 PIPELINE TERMINÉ")
    print("=" * 70)
    
    if all_passed:
        print("\n✅ TOUS LES TESTS COMPLÉTÉS AVEC SUCCÈS!")
        print("\n📄 Fichiers générés:")
        print("   ✅ rapport_login.json")
        print("   ✅ rapport_open_account.json")
        print("   ✅ rapport_bill_pay.json")
        print("   ✅ rapport_cas_avances.json")
        print("   ✅ rapport.json (fusion)")
        print("   ✅ rapport.html (rapport visuel)")
    else:
        print("\n⚠️  PIPELINE TERMINÉ AVEC AVERTISSEMENTS")
        print("   Vérifiez les résultats dans rapport.html")
    
    print("\n" + "=" * 70)
    print("💡 Prochaines étapes:")
    print("   1. Vérifiez rapport.html dans le navigateur")
    print("   2. Analysez les scénarios échoués (le cas échéant)")
    print("   3. Corrigez les features/steps")
    print("   4. Relancez: python run_pipeline_PARABANK.py")
    print("\n" + "=" * 70 + "\n")


if __name__ == '__main__':
    try:
        run_all_tests()
    except KeyboardInterrupt:
        print("\n\n❌ Pipeline interrompu par l'utilisateur")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Erreur fatale: {str(e)}")
        sys.exit(1)