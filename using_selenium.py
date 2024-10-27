from selenium import webdriver
from selenium.webdriver.common.by import By


#Keep chrome browser open ofter program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.in/HP-Windows-Office21-Keyboard-fd1099TU/dp/B0D262YX9D/ref=pd_rhf_gw_s_pd_crcd_d_sccl_1_3/262-0218610-6246804?pd_rd_w=1NA5d&content-id=amzn1.sym.785b16db-ca40-46a3-ae75-2b38bb48d1aa&pf_rd_p=785b16db-ca40-46a3-ae75-2b38bb48d1aa&pf_rd_r=4J0Y8VSAW60TCGBTWJ3G&pd_rd_wg=lxkif&pd_rd_r=90a614d9-c331-4c67-8055-f5e892386516&pd_rd_i=B0D262YX9D&psc=1")

price_money = driver.find_element(By.CLASS_NAME,value="a-price-whole")
product_title = driver.find_element(By.ID,value="productTitle")
#print(price_money)
print(f"The product :\n {product_title.text} \n price is : \n {price_money.text}")


#driver.close()
driver.quit()