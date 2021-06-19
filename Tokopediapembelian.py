from os import wait
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
# from pyvirtualdisplay import Display
import time


driver = webdriver.Chrome('/Applications/chromedriver90')
driver.get('https://www.tokopedia.com/')
driver.maximize_window()
wait = WebDriverWait(driver, 10)

def Login(Email, password):
    btnLgn = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Masuk')]")))
    btnLgn.click()

    fillEmail = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#email-phone")))
    fillEmail.send_keys(Email)

    driver.find_element_by_xpath("//span[contains(text(),'Selanjutnya')]").click()

    fillPass = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#password-input")))
    fillPass.send_keys(password)

    driver.find_element_by_xpath("//span[contains(text(),'Masuk')]").click()
    time.sleep(30)

def PembelianwithPromo(noHp,KodePos, AlamatHome,PromoVoucer):

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".css-15kuy91"))).click()

    # checkAll = wait.until(EC.visibility_of_element_located((By.XPATH, "#check-all-items")))
    # checkAll.click()

    jumlahBrg = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "css-iustv6")))
    jumlahBrg.send_keys(Keys.DELETE)

    inputBarang = driver.find_element_by_class_name("css-iustv6")
    inputBarang.send_keys("400")

    btnBuy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label='buy'] span")))
    btnBuy.click()

    checkout = wait.until(EC.visibility_of_element_located((By.TAG_NAME,"h1"))).text
    print(checkout)

    chooseNewAdress= wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Pilih Alamat Lain']")))
    chooseNewAdress.click()

    # assert "Alamat Pengiriman" in driver.find_element_by_tag_name("h2").text
    pengiriman = wait.until(EC.visibility_of_element_located((By.TAG_NAME,"h2"))).text
    print(pengiriman)

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".address-list-adder"))).click()

    noTelp = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-testid='txtModalAddrFormAddrPhone']")))
    noTelp.send_keys(noHp)

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Tulis Nama Alamat / Kota / Kecamatan tujuan pengiriman']")))
    time.sleep(10)

    kodePost = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Kode Pos']")))
    kodePost.send_keys(KodePos)

    alamat = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR , "input[placeholder='Isi dengan nama jalan, nomor rumah, nomor kompleks, nama gedung, lantai atau nomor unit.']")))
    alamat.send_keys(AlamatHome)

    driver.find_element_by_css_selector("button[data-testid='btnClickSubmit'] span").click()
    time.sleep(5)

    pengiriman = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ddsd-cap-text")))
    pengiriman.click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Reguler')]"))).click()

    promo =wait.until(EC.visibility_of_element_located((By.XPATH,"//span[contains(text(),'Makin hemat pakai promo')]")))
    promo.click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Pakai Promo')]")))

    InputPromo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input[placeholder='Masukkan kode promo']")))
    InputPromo.send_keys(PromoVoucer)
    
    btnTerapkan = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"button[class='css-hywtfd-unf-btn e1ggruw00'] span")))
    btnTerapkan.click()

    btnBeli = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"button[class='css-ti28tv-unf-btn e1ggruw00'] span")))
    btnBeli.click()
    driver.quit()
def PembelianNoPromo(noHp,KodePos, AlamatHome):
    
    
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".css-15kuy91"))).click()

    # checkAll = wait.until(EC.visibility_of_element_located((By.XPATH, "#check-all-items")))
    # checkAll.click()

    jumlahBrg = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "css-iustv6")))
    jumlahBrg.send_keys(Keys.DELETE)

    inputBarang = driver.find_element_by_class_name("css-iustv6")
    inputBarang.send_keys("400")

    btnBuy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label='buy'] span")))
    btnBuy.click()

    checkout = wait.until(EC.visibility_of_element_located((By.TAG_NAME,"h1"))).text
    print(checkout)

    chooseNewAdress= wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Pilih Alamat Lain']")))
    chooseNewAdress.click()

    # assert "Alamat Pengiriman" in driver.find_element_by_tag_name("h2").text
    pengiriman = wait.until(EC.visibility_of_element_located((By.TAG_NAME,"h2"))).text
    print(pengiriman)

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".address-list-adder"))).click()

    noTelp = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-testid='txtModalAddrFormAddrPhone']")))
    noTelp.send_keys(noHp)

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Tulis Nama Alamat / Kota / Kecamatan tujuan pengiriman']")))
    time.sleep(10)

    kodePost = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Kode Pos']")))
    kodePost.send_keys(KodePos)

    alamat = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR , "input[placeholder='Isi dengan nama jalan, nomor rumah, nomor kompleks, nama gedung, lantai atau nomor unit.']")))
    alamat.send_keys(AlamatHome)

    driver.find_element_by_css_selector("button[data-testid='btnClickSubmit'] span").click()
    time.sleep(5)

    pengiriman = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ddsd-cap-text")))
    pengiriman.click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Reguler')]"))).click()

    btnBeli = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"button[class='css-ti28tv-unf-btn e1ggruw00'] span")))
    btnBeli.click()
    driver.quit()
Email =  #fill you email tokopedia account here 
password = #fill you password tokopedia account here
noHp = #fill you number phone  here
KodePos = #fill you kodepos here
AlamatHome = #fill you address here
PromoVoucer = #fill you voucher promo here

Login(Email, password)
PembelianwithPromo(noHp, KodePos, AlamatHome, PromoVoucer)
PembelianNoPromo(noHp, KodePos, AlamatHome)
