# features/steps/common_steps.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def wait_click(context, locator, timeout=10):
    """Attendre que l'élément soit cliquable puis cliquer"""
    try:
        element = WebDriverWait(context.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
        print(f"   ✅ Cliqué sur: {locator}")
    except Exception as e:
        print(f"   ❌ Erreur au clic: {e}")
        raise

def wait_type(context, locator, text, timeout=10):
    """Attendre que l'élément soit visible puis saisir du texte"""
    try:
        element = WebDriverWait(context.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)
        print(f"   ✅ Saisi '{text}' dans: {locator}")
    except Exception as e:
        print(f"   ❌ Erreur à la saisie: {e}")
        raise

def wait_visible(context, locator, timeout=15):
    """Attendre que l'élément soit visible"""
    try:
        element = WebDriverWait(context.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        print(f"   ✅ Élément visible: {locator}")
        return element
    except Exception as e:
        print(f"   ❌ Erreur de visibilité: {e}")
        raise

def wait_present(context, locator, timeout=15):
    """Attendre que l'élément soit présent dans le DOM"""
    try:
        element = WebDriverWait(context.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        print(f"   ✅ Élément présent: {locator}")
        return element
    except Exception as e:
        print(f"   ❌ Erreur de présence: {e}")
        raise

def wait_for_url(context, url_part, timeout=15):
    """Attendre que l'URL contienne une certaine partie"""
    try:
        WebDriverWait(context.driver, timeout).until(
            EC.url_contains(url_part)
        )
        print(f"   ✅ URL contient: {url_part}")
    except Exception as e:
        print(f"   ❌ Erreur URL: {e}")
        raise
