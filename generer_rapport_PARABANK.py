"""
generer_rapport.py - Génère un rapport HTML élégant à partir du rapport.json

Usage:
    python generer_rapport.py

Entrée:
    - rapport.json (généré par fusionner.py)

Sortie:
    - rapport.html (rapport visuel)
"""

import json
import os
from datetime import datetime


def generer_rapport_html():
    """Génère un rapport HTML élégant à partir de rapport.json"""
    
    # Lire le rapport fusionné
    if not os.path.exists('rapport.json'):
        print("❌ Erreur: rapport.json n'existe pas")
        print("   Exécutez d'abord: python fusionner.py")
        return
    
    print("📄 Génération du rapport HTML...")
    
    with open('rapport.json', 'r', encoding='utf-8') as f:
        rapport = json.load(f)
    
    stats = rapport.get('statistics', {})
    features = rapport.get('features', [])
    
    # Calculer les pourcentages
    total_scenarios = stats.get('total_scenarios', 1)
    total_steps = stats.get('total_steps', 1)
    pct_scenarios = (stats.get('scenarios_passed', 0) / total_scenarios * 100) if total_scenarios > 0 else 0
    pct_steps = (stats.get('steps_passed', 0) / total_steps * 100) if total_steps > 0 else 0
    
    # Déterminer la couleur de statut global
    if stats.get('scenarios_failed', 0) == 0:
        statut_couleur = '#28a745'  # Vert
        statut_texte = '✅ TOUS LES TESTS PASSENT'
    else:
        statut_couleur = '#dc3545'  # Rouge
        statut_texte = '❌ CERTAINS TESTS ONT ÉCHOUÉ'
    
    # Construire le HTML
    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rapport de Tests Parabank</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
            padding: 20px;
            min-height: 100vh;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px 20px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        
        .header p {{
            font-size: 1.1em;
            opacity: 0.9;
        }}
        
        .status {{
            background-color: {statut_couleur};
            color: white;
            padding: 15px;
            text-align: center;
            font-size: 1.2em;
            font-weight: bold;
        }}
        
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 30px;
            background: #f8f9fa;
        }}
        
        .stat-card {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            text-align: center;
        }}
        
        .stat-card h3 {{
            color: #667eea;
            font-size: 0.9em;
            text-transform: uppercase;
            margin-bottom: 10px;
        }}
        
        .stat-card .number {{
            font-size: 2.5em;
            font-weight: bold;
            color: #333;
        }}
        
        .stat-card .detail {{
            font-size: 0.9em;
            color: #666;
            margin-top: 10px;
        }}
        
        .progress-bar {{
            background: #e9ecef;
            border-radius: 10px;
            height: 25px;
            overflow: hidden;
            margin-top: 10px;
        }}
        
        .progress-fill {{
            background: linear-gradient(90deg, #28a745, #20c997);
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: bold;
            font-size: 0.85em;
            transition: width 0.3s ease;
        }}
        
        .content {{
            padding: 30px;
        }}
        
        .section {{
            margin-bottom: 30px;
        }}
        
        .section h2 {{
            color: #667eea;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }}
        
        .feature {{
            background: #f8f9fa;
            border-left: 5px solid #667eea;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 4px;
        }}
        
        .feature-name {{
            font-weight: bold;
            color: #333;
            font-size: 1.1em;
            margin-bottom: 10px;
        }}
        
        .scenario {{
            background: white;
            padding: 10px;
            margin-top: 10px;
            border-radius: 4px;
            border-left: 3px solid #ddd;
        }}
        
        .scenario.passed {{
            border-left-color: #28a745;
        }}
        
        .scenario.failed {{
            border-left-color: #dc3545;
        }}
        
        .scenario-title {{
            font-weight: bold;
            margin-bottom: 5px;
        }}
        
        .scenario.passed .scenario-title::before {{
            content: "✅ ";
        }}
        
        .scenario.failed .scenario-title::before {{
            content: "❌ ";
        }}
        
        .step {{
            font-size: 0.9em;
            color: #666;
            padding: 5px;
            margin: 3px 0;
            padding-left: 20px;
        }}
        
        .step.passed {{
            color: #28a745;
        }}
        
        .step.failed {{
            color: #dc3545;
        }}
        
        .step.pending {{
            color: #ffc107;
        }}
        
        .footer {{
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            color: #666;
            font-size: 0.9em;
            border-top: 1px solid #ddd;
        }}
        
        .timestamp {{
            color: #999;
            font-size: 0.85em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 Rapport de Tests Parabank</h1>
            <p>Automation Tests - Selenium + Behave</p>
        </div>
        
        <div class="status">
            {statut_texte}
        </div>
        
        <div class="stats">
            <div class="stat-card">
                <h3>Scénarios</h3>
                <div class="number">{stats.get('scenarios_passed', 0)}/{total_scenarios}</div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {pct_scenarios:.1f}%">
                        {pct_scenarios:.0f}%
                    </div>
                </div>
            </div>
            
            <div class="stat-card">
                <h3>Steps</h3>
                <div class="number">{stats.get('steps_passed', 0)}/{total_steps}</div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {pct_steps:.1f}%">
                        {pct_steps:.0f}%
                    </div>
                </div>
            </div>
            
            <div class="stat-card">
                <h3>Scénarios Échoués</h3>
                <div class="number" style="color: #dc3545;">
                    {stats.get('scenarios_failed', 0)}
                </div>
                <div class="detail">
                    {stats.get('steps_failed', 0)} steps échoués
                </div>
            </div>
            
            <div class="stat-card">
                <h3>Durée Totale</h3>
                <div class="number">{stats.get('duration_total', 0):.1f}s</div>
                <div class="detail">
                    Exécution complète
                </div>
            </div>
        </div>
        
        <div class="content">
            <div class="section">
                <h2>📋 Détails des Tests</h2>
                
                {_generer_details_features(features)}
            </div>
        </div>
        
        <div class="footer">
            <p>
                Rapport généré le <strong>{datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}</strong>
            </p>
            <p class="timestamp">
                Total: {total_scenarios} scénarios | {total_steps} steps | Durée: {stats.get('duration_total', 0):.2f}s
            </p>
        </div>
    </div>
</body>
</html>
"""
    
    # Sauvegarder le HTML
    with open('rapport.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ Rapport HTML créé: rapport.html")
    print(f"\n📈 RÉSUMÉ:")
    print(f"   ✅ Scénarios réussis: {stats.get('scenarios_passed', 0)}/{total_scenarios} ({pct_scenarios:.1f}%)")
    print(f"   ❌ Scénarios échoués: {stats.get('scenarios_failed', 0)}/{total_scenarios}")
    print(f"   ✅ Steps réussis: {stats.get('steps_passed', 0)}/{total_steps} ({pct_steps:.1f}%)")
    print(f"\n🌐 Ouvrez rapport.html dans un navigateur pour voir le rapport détaillé")


def _generer_details_features(features):
    """Génère le HTML pour les détails des features"""
    
    html = ""
    
    for feature in features:
        feature_name = feature.get('name', 'Feature sans nom')
        description = feature.get('description', '')
        
        html += f'<div class="feature">\n'
        html += f'    <div class="feature-name">🎯 {feature_name}</div>\n'
        
        if description:
            html += f'    <div style="color: #666; font-size: 0.9em;">{description}</div>\n'
        
        for scenario in feature.get('elements', []):
            scenario_name = scenario.get('name', 'Scenario sans nom')
            
            # Déterminer le statut du scénario
            statut = 'passed'
            for step in scenario.get('steps', []):
                if step.get('result', {}).get('status') == 'failed':
                    statut = 'failed'
                    break
            
            html += f'    <div class="scenario {statut}">\n'
            html += f'        <div class="scenario-title">{scenario_name}</div>\n'
            
            # Ajouter les steps
            for step in scenario.get('steps', []):
                step_name = step.get('name', '')
                step_status = step.get('result', {}).get('status', 'unknown')
                
                html += f'        <div class="step {step_status}">'
                html += f'{step_name} <em>({step_status})</em>'
                html += f'</div>\n'
            
            html += f'    </div>\n'
        
        html += f'</div>\n'
    
    return html


if __name__ == '__main__':
    generer_rapport_html()