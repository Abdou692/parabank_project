from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def before_all(context):
    context.base_url = context.config.userdata.get("base_url", "http://localhost:8080/parabank/index.htm")
    context.username = context.config.userdata.get("username", "john")
    context.password = context.config.userdata.get("password", "demo")
    print("🚀 Tests avec Firefox")
    print(f"   URL: {context.base_url}")

def before_scenario(context, scenario):
    print(f"\n📋 Scénario: {scenario.name}")
    options = Options()
    service = Service(GeckoDriverManager().install())
    context.driver = webdriver.Firefox(service=service, options=options)
    context.driver.implicitly_wait(5)
    print(f"   ✅ Driver prêt")

def after_scenario(context, scenario):
    if hasattr(context, 'driver') and context.driver:
        context.driver.quit()

def after_all(context):
    print("\n✨ Tests terminés")