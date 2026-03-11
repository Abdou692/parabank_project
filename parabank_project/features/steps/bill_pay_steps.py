# features/steps/bill_pay_steps.py

from behave import given, when, then
from selenium.webdriver.support.ui import Select
from features.steps.selectors import *
from features.steps.common_steps import *
import time

@given("l'utilisateur est connecté à ParaBank pour le paiement de factures")
def step_login_bill_pay(context):
    """Se connecter à ParaBank pour le paiement"""
    context.driver.get(context.base_url)
    time.sleep(1)
    wait_type(context, USERNAME_INPUT, context.username)
    wait_type(context, PASSWORD_INPUT, context.password)
    wait_click(context, LOGIN_BUTTON)
    time.sleep(2)
    wait_visible(context, BILL_PAY_LINK)
    print(f"   ✅ Utilisateur connecté pour Bill Pay")

@when("il accède à Bill Pay")
def step_access_bill_pay(context):
    """Accéder à la page Bill Pay"""
    wait_click(context, BILL_PAY_LINK)
    time.sleep(1)
    wait_visible(context, PAYEE_NAME)
    print(f"   ✅ Page 'Bill Pay' ouverte")

@when("il remplit un paiement valide")
def step_fill_payment_form(context):
    """Remplir le formulaire de paiement avec des données valides"""
    try:
        wait_type(context, PAYEE_NAME, "Abdou")
        wait_type(context, ADDRESS, "123 rue test")
        wait_type(context, CITY, "Paris")
        wait_type(context, STATE, "NA")
        wait_type(context, ZIP, "75001")
        wait_type(context, PHONE, "0102030405")
        wait_type(context, ACCOUNT_NUMBER, "12345")
        wait_type(context, VERIFY_ACCOUNT, "12345")
        wait_type(context, AMOUNT, "100")
        
        # Sélectionner le compte source
        try:
            # Chercher le SELECT element
            select_element = Select(context.driver.find_element(*FROM_ACCOUNT_ID))
            select_element.select_by_index(0)
            time.sleep(0.5)
            print(f"   ✅ Compte source sélectionné via Select")
        except Exception as select_error:
            # Si ce n'est pas un select, essayer de cliquer directement
            print(f"   ⚠️  Select échoué, essai alternatif: {select_error}")
            try:
                element = context.driver.find_element(*FROM_ACCOUNT_ID)
                context.driver.execute_script("arguments[0].click();", element)
                time.sleep(0.5)
                print(f"   ✅ Compte source cliqué directement")
            except:
                print(f"   ⚠️  Compte source optionnel, continuant...")
        
        print(f"   ✅ Formulaire de paiement rempli")
    except Exception as e:
        print(f"   ❌ Erreur lors du remplissage: {e}")
        raise

@when("il soumet le paiement")
def step_submit_payment(context):
    """Soumettre le paiement"""
    wait_click(context, SEND_PAYMENT_BUTTON)
    time.sleep(2)
    print(f"   ✅ Paiement soumis")

@then("le paiement est confirmé")
def step_verify_payment_success(context):
    """Vérifier que le paiement est confirmé"""
    wait_visible(context, PAYMENT_COMPLETE_MSG, timeout=10)
    print(f"   ✅ Paiement confirmé avec succès")