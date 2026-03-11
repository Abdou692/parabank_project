# features/steps/login_steps.py

from behave import given, when, then
from features.steps.selectors import *
from features.steps.common_steps import *
import time

@given("l'utilisateur est sur la page de connexion Parabank")
def step_open_login(context):
    """Ouvrir la page de connexion ParaBank"""
    context.driver.get(context.base_url)
    time.sleep(1)
    print(f"   ✅ Page de connexion ouverte: {context.base_url}")

@given("que l'utilisateur est sur la page de connexion Parabank")
def step_open_login_alt(context):
    """Alternative avec 'que' au début"""
    step_open_login(context)

@when("il saisit ses identifiants")
def step_login(context):
    """Saisir et soumettre les identifiants"""
    wait_type(context, USERNAME_INPUT, context.username)
    wait_type(context, PASSWORD_INPUT, context.password)
    wait_click(context, LOGIN_BUTTON)
    time.sleep(2)
    print(f"   ✅ Identifiants saisis et formulaire soumis")

@then("il doit être connecté avec succès")
def step_success(context):
    """Vérifier que la connexion est réussie"""
    wait_visible(context, ACCOUNTS_OVERVIEW_LINK, timeout=15)
    print(f"   ✅ Connexion réussie - Page d'accueil affichée")
