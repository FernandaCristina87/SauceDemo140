# 1 - Bibliotecas
import selenium 
from selenium import webdriver 
from selenium.webdriver.common.by import By



# 2 - Classe(opcioanl)
class Teste_produtos():

# 2.1 - Atributos
    url = "https://www.saucedemo.com"


# 2.2 - Funções e Metodos
    def setup_method(self, method):                              # método de inicialização dos testes
        self.driver = webdriver.Chrome()                         # instancia o objeto do selenium WebDriver como Chrome
        self.driver.implicitly_wait(10)                          # define o tempo de espera padrao por elementos em 10 segundos

    def teardown_method(self, method):                            # método de finalização
        self.driver.quit()                                  # encerra / destroi o objeto do selenium WebDriver da memória


    def test_selecionar_produto(self):              # método de teste
        self.driver.get(self.url)                           # abre navegador
        self.driver.find_element(By.ID,"user-name").send_keys("standard_user")                     # escreve no campo do usuario
        self.driver.find_element(By.NAME,"password").send_keys("secret_sauce")                     # escreve a senha
