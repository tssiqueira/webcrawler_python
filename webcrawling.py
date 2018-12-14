
from selenium import webdriver
import unicodedata
from time import sleep

class Investing_spider():
    #phantom_path = "C:/Users/lmenniti/Downloads/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe"
    #phantom_path = "//corp.bloomberg.com/ra-dfs/Sao Paulo/userFolders/My Documents/phantomjs-2.1.1-windows/bin/phantomjs.exe"
    # chrome_path = 'C:/Users/lmenniti/Downloads/chromedriver.exe'
    array_of_ativos = []

    def __init__(self):
        #self.driver = webdriver.PhantomJS(executable_path=r'{}'.format(self.phantom_path))
        # self.driver = webdriver.Chrome(executable_path=r'{}'.format(self.chrome_path))
        self.driver = webdriver.Chrome()
        #Powershell.__init__(self)

    def convert_unicode(self, text):
        word = str(unicodedata.normalize('NFKD', text).encode('ascii', 'ignore'))
        return word

    def get_main_link(self, url=None):
        if url == None:
            self.driver.get('http://www.debentures.com.br/exploreosnd/consultaadados/emissoesdedebentures/caracteristicas_r.asp?tip_deb=publicas&op_exc=')
        else:
            self.driver.get(url)

    def get_characteristic_link(self, ativo_code):
        self.driver.get('http://www.debentures.com.br/exploreosnd/consultaadados/emissoesdedebentures/caracteristicas_d.asp?tip_deb=publicas&selecao={}'.format(ativo_code))

    def get_main_page_data(self):

        for n_ativo in range(1, 10000):
            try:
                ativo_code = self.driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[2]/table[2]/tbody/tr[2]/td[3]/table[2]/tbody/tr[{}]/td[2]/a".format(n_ativo)).text
                #ativo_code = ativo_code.remove('=')
                ativo_name = self.driver.find_element_by_xpath(
                    "/html/body/table[2]/tbody/tr[1]/td[2]/table[2]/tbody/tr[2]/td[3]/table[2]/tbody/tr[{}]/td[3]".format(
                        n_ativo)).text
                # ativo_code = ativo_code.remove('=')
            except Exception as e:
                print(e)
                # break
            print(ativo_code, ativo_name)

            self.array_of_ativos.append(ativo_code)
        print(self.array_of_ativos)

debentures = Investing_spider()
debentures.get_main_link()
debentures.get_main_page_data()