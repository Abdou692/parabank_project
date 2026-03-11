# features/steps/open_account_steps.py

from behave import given, when, then
from selenium.webdriver.support.ui import Select
from features.steps.selectors import *
from features.steps.common_steps import *
import time

@given("l'utilisateur est connecté à ParaBank")
def step_login_first(context):
    """Se connecter d'abord à ParaBank"""
    context.driver.get(context.base_url)
    time.sleep(1)
    wait_type(context, USERNAME_INPUT, context.username)
    wait_type(context, PASSWORD_INPUT, context.password)
    wait_click(context, LOGIN_BUTTON)
    time.sleep(2)
    wait_visible(context, ACCOUNTS_OVERVIEW_LINK)
    print(f"   ✅ Utilisateur connecté à ParaBank")

@when("il accède à Open New Account")
def step_open_account(context):
    """Accéder à la page de création de compte"""
    wait_click(context, OPEN_NEW_ACCOUNT_LINK)
    time.sleep(1)
    wait_visible(context, ACCOUNT_TYPE_SELECT)
    print(f"   ✅ Page 'Open New Account' ouverte")

@when('il choisit le type de compte "{type_compte}"')
def step_choose_account_type(context, type_compte):
    """Choisir le type de compte"""
    try:
        select_element = Select(context.driver.find_element(*ACCOUNT_TYPE_SELECT))
        select_element.select_by_visible_text(type_compte)
        time.sleep(0.5)
        print(f"   ✅ Type de compte '{type_compte}' sélectionné")
    except Exception as e:
        print(f"   ❌ Erreur lors de la sélection du type: {e}")
        raise

@when("il sélectionne un compte source")
def step_select_source_account(context):
    """Sélectionner un compte source"""
    try:
        select_element = Select(context.driver.find_element(*FROM_ACCOUNT_SELECT))
        select_element.select_by_index(0)
        time.sleep(0.5)
        selected_account = select_element.first_selected_option.text
        context.source_account = selected_account
        print(f"   ✅ Compte source sélectionné: {selected_account}")
    except Exception as e:
        print(f"   ❌ Erreur lors de la sélection du compte: {e}")
        raise

@when("il clique sur Open New Account")
def step_submit_account_creation(context):
    """Soumettre la création de compte"""
    wait_click(context, OPEN_ACCOUNT_BUTTON)
    time.sleep(2)
    print(f"   ✅ Formulaire de création de compte soumis")

@then("le nouveau compte est créé avec succès")
def step_verify_account_created(context):
    """Vérifier que le compte a été créé"""
    wait_visible(context, ACCOUNT_CREATED_MSG, timeout=10)
    print(f"   ✅ Nouveau compte créé avec succès")

@then("le nouveau compte est créé avec successivement")
def step_verify_account_created_alt(context):
    """Alternative avec typo"""
    step_verify_account_created(context)
