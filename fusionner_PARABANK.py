"""
fusionner.py - Fusionne tous les rapports JSON en un seul

Usage:
    python fusionner.py

Fusion de:
    - rapport_login.json
    - rapport_open_account.json
    - rapport_bill_pay.json
    - rapport_cas_avances.json

Génère:
    - rapport.json (fusion complète avec statistiques)
"""

import json
import os
import sys
from datetime import datetime


def fusionner_rapports():
    """Fusionne tous les fichiers rapport_*.json en un seul rapport.json"""
    
    # Fichiers à fusionner pour VOTRE projet Parabank
    fichiers_rapports = [
        'rapport_login.json',
        'rapport_open_account.json',
        'rapport_bill_pay.json',
        'rapport_cas_avances.json',
    ]
    
    print("\n" + "=" * 70)
    print("🔄 FUSION DES RAPPORTS DE TEST")
    print("=" * 70)
    
    # Initialiser les listes et statistiques
    toutes_les_features = []
    stats_globales = {
        'total_features': 0,
        'total_scenarios': 0,
        'total_steps': 0,
        'scenarios_passed': 0,
        'scenarios_failed': 0,
        'steps_passed': 0,
        'steps_failed': 0,
        'steps_skipped': 0,
        'duration_total': 0.0,
    }
    
    fichiers_traites = 0
    
    # Parcourir chaque fichier rapport
    print("\n📂 Traitement des fichiers:")
    for fichier in fichiers_rapports:
        if os.path.exists(fichier):
            print(f"   ✅ {fichier:<40} [TROUVÉ]")
            
            try:
                with open(fichier, 'r', encoding='utf-8') as f:
                    donnees = json.load(f)
                    
                    # S'assurer que c'est une liste
                    if not isinstance(donnees, list):
                        donnees = [donnees]
                    
                    # Ajouter les features
                    toutes_les_features.extend(donnees)
                    fichiers_traites += 1
                    
                    # Calculer les statistiques pour ce fichier
                    for feature in donnees:
                        stats_globales['total_features'] += 1
                        
                        for scenario in feature.get('elements', []):
                            stats_globales['total_scenarios'] += 1
                            
                            # Status du scénario
                            scenario_status = 'passed'
                            
                            # Compter les steps
                            for step in scenario.get('steps', []):
                                stats_globales['total_steps'] += 1
                                
                                # Status du step
                                if 'result' in step:
                                    result = step['result']
                                    status = result.get('status', '')
                                    duration = result.get('duration', 0)
                                    
                                    if duration:
                                        stats_globales['duration_total'] += duration / 1000000000  # Nano en secondes
                                    
                                    if status == 'passed':
                                        stats_globales['steps_passed'] += 1
                                    elif status == 'failed':
                                        stats_globales['steps_failed'] += 1
                                        scenario_status = 'failed'
                                    elif status == 'skipped':
                                        stats_globales['steps_skipped'] += 1
                            
                            # Compter le scénario
                            if scenario_status == 'passed':
                                stats_globales['scenarios_passed'] += 1
                            else:
                                stats_globales['scenarios_failed'] += 1
                
            except json.JSONDecodeError:
                print(f"   ❌ {fichier:<40} [ERREUR JSON]")
            except Exception as e:
                print(f"   ❌ {fichier:<40} [ERREUR: {str(e)}]")
        else:
            print(f"   ⚠️  {fichier:<40} [NON TROUVÉ]")
    
    print(f"\n📋 Fichiers traités: {fichiers_traites}/{len(fichiers_rapports)}")
    
    # Créer le rapport fusionné
    rapport_fusionne = {
        'features': toutes_les_features,
        'statistics': stats_globales,
        'generated_at': datetime.now().isoformat(),
    }
    
    # Sauvegarder
    try:
        with open('rapport.json', 'w', encoding='utf-8') as f:
            json.dump(rapport_fusionne, f, indent=2, ensure_ascii=False)
        
        print(f"\n✅ Rapport fusionné créé: rapport.json")
        
        # Afficher les statistiques
        total_scen = stats_globales['total_scenarios'] or 1
        total_steps = stats_globales['total_steps'] or 1
        pct_scenarios = (stats_globales['scenarios_passed'] / total_scen * 100)
        pct_steps = (stats_globales['steps_passed'] / total_steps * 100)
        
        print("\n" + "=" * 70)
        print("📊 STATISTIQUES GLOBALES")
        print("=" * 70)
        print(f"\n📌 Features:")
        print(f"   Total: {stats_globales['total_features']}")
        
        print(f"\n🎬 Scénarios:")
        print(f"   Total:    {stats_globales['total_scenarios']}")
        print(f"   ✅ PASS:  {stats_globales['scenarios_passed']} ({pct_scenarios:.1f}%)")
        print(f"   ❌ FAIL:  {stats_globales['scenarios_failed']}")
        
        print(f"\n📝 Steps:")
        print(f"   Total:    {stats_globales['total_steps']}")
        print(f"   ✅ PASS:  {stats_globales['steps_passed']} ({pct_steps:.1f}%)")
        print(f"   ❌ FAIL:  {stats_globales['steps_failed']}")
        print(f"   ⊘  SKIP:  {stats_globales['steps_skipped']}")
        
        print(f"\n⏱️  Durée totale: {stats_globales['duration_total']:.2f}s")
        
        # Déterminer le statut global
        if stats_globales['scenarios_failed'] == 0:
            statut = "✅ TOUS LES TESTS PASSENT"
            couleur = "VERT"
        else:
            statut = f"❌ {stats_globales['scenarios_failed']} TEST(S) ÉCHOUÉ(S)"
            couleur = "ROUGE"
        
        print(f"\n🎯 Statut global: {statut} ({couleur})")
        print("\n" + "=" * 70)
        
        print("\n💡 Prochaines étapes:")
        print("   1. Générer le rapport HTML: python generer_rapport.py")
        print("   2. Ouvrir le rapport: start rapport.html")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Erreur lors de la sauvegarde: {str(e)}")
        return False


if __name__ == '__main__':
    success = fusionner_rapports()
    sys.exit(0 if success else 1)