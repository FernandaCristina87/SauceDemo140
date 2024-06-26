#Bibliotecas imports
import time
from behave import given, when, then
from selenium import webdriver  
from selenium.webdriver.common.by import By 
import time 

@given(u'que acesso o site Sauce Demo')
def step_impl(context):
    context.driver = webdriver.Chrome()                        # instanciar o objeto do selenium webdriver especializado para o chrome
    context.driver.maximize_window()                           # maximizar a janela do navegador
    context.driver.implicitly_wait(10)                         # esperar ate 10 segundos por qualquer elemento  
    context.driver.get("https://www.saucedemo.com")            # abrir navegador no site alvo

@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)
    context.driver.find_element(By.ID, "password").send_keys(senha)
    context.driver.find_element(By.ID, "login-button").click()

   
@then(u'sou direcionado para pagina Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"
    time.sleep(2)    # espera por 2 segundos  -  remover depois = alfinete


    # teardown / encerramento 
    context.driver.quit()

    