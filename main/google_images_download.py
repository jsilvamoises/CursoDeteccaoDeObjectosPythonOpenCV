from selenium import webdriver
import pyautogui
import time

driver = webdriver.Chrome()

driver.get("https://images.google.com/")

inputSearch = driver.find_element_by_name("q")
inputSearch.send_keys("caneca")
inputSearch.submit()

ferramentas = driver.find_element_by_partial_link_text("Ferramentas")
ferramentas.click()
time.sleep(1)


tamanho = pyautogui.locateOnScreen("../images/bt_tamanho.PNG")
center = pyautogui.center(tamanho)
pyautogui.click(center)

exatamente = pyautogui.locateOnScreen("../images/bt_exatamente.PNG")
center = pyautogui.center(exatamente)
pyautogui.click(center)


largura = driver.find_element_by_id("kbqVne")
largura.send_keys("400")

altura = driver.find_element_by_id("XOyNzd")
altura.send_keys("400")

ir = driver.find_element_by_xpath("//button[text()='Ir']")
ir.click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, 10000)")
#driver.execute_script("window.scrollTo(0, 0)")
images = driver.find_elements_by_tag_name("img")

for scroll in range(0,1000,1000):  
    driver.execute_script("window.scrollTo(0, {})".format(scroll))  
    for x in range(200):
        print(images[x].get_property("src"))
        print()



