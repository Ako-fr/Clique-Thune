from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from time import sleep

print("""
 ██████╗██╗     ██╗ ██████╗██╗  ██╗    ████████╗██╗  ██╗██╗   ██╗███╗   ██╗███████╗
██╔════╝██║     ██║██╔════╝██║ ██╔╝    ╚══██╔══╝██║  ██║██║   ██║████╗  ██║██╔════╝
██║     ██║     ██║██║     █████╔╝        ██║   ███████║██║   ██║██╔██╗ ██║█████╗  
██║     ██║     ██║██║     ██╔═██╗        ██║   ██╔══██║██║   ██║██║╚██╗██║██╔══╝  
╚██████╗███████╗██║╚██████╗██║  ██╗       ██║   ██║  ██║╚██████╔╝██║ ╚████║███████╗
 ╚═════╝╚══════╝╚═╝ ╚═════╝╚═╝  ╚═╝       ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝

                            [!] Devlopped by Ako

""")

proxy_ip = open('proxy.txt', 'r')

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = proxy_ip
proxy.ssl_proxy = proxy_ip

capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)

link = input("Indique le lien : ")
click = 1000
count = 0
while count < click:
    driver = webdriver.Chrome(executable_path="chromedriver.exe", desired_capabilities=capabilities)
    driver.get(link)
    sleep(11)
    element = driver.find_element_by_id("compteur").click()
    sleep(2)
    print("[+] Action Reussi")
    count += 1
