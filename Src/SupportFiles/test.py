from selenium.webdriver import Edge
from time import sleep
import subprocess
import os

web = Edge()

web.get('https://app.powerbi.com/groups/me/list?noSignUpCheck=1&cmpid=pbi-home-body-snn-signin')

email = 'felipe@opendt.onmicrosoft.com'
password = 'Xky@15935!'

web.find_element_by_xpath('//*[@id="i0116"]').send_keys(email)
web.find_element_by_xpath('//*[@id="idSIButton9"]').click()
sleep(2)

web.find_element_by_xpath('//*[@id="i0118"]').send_keys(password)
web.find_element_by_xpath('//*[@id="idSIButton9"]').click()
sleep(2)

web.find_element_by_xpath('//*[@id="idBtn_Back"]').click()

web.find_element_by_xpath('//*[@id="artifactContentList"]/div[1]/div[1]/div[2]/span/a').click()

while len(web.find_elements_by_id('exportMenuBtn')) < 1:
    sleep(1)

web.find_element_by_xpath('//*[@id="exportMenuBtn"]/span').click()
sleep(2)
web.find_element_by_xpath('//*[@id="mat-menu-panel-11"]/div/button[3]').click()
sleep(2)
web.find_element_by_xpath('//*[@id="okButton"]').click()

while True:
    print('Tentando abrir o arquivo')
    try:
        os.rename(r'C:\Users\USER\Downloads\AnaliseDados.pdf', r'C:\Users\USER\OneDrive\Documentos\Programação\Python\Projetos\Comandas-Açai\Dashboard\AnaliseDados.pdf')
        subprocess.Popen(r'explorer C:\Users\USER\OneDrive\Documentos\Programação\Python\Projetos\Comandas-Açai\Dashboard\AnaliseDados.pdf')
        break
    except:
        sleep(10)