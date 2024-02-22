from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import unittest

class TestInput1(unittest.TestCase):
    def test_input1(self):
        service = Service('D:\webdriver\chromedriver.exe')
        options = Options()
        options.headless = False
        driver = webdriver.Chrome(service=service, options=options)
        
        driver.get("http://127.0.0.1/customerphp/customer.php")
        
        name = driver.find_element(By.ID, "firstName")
        last = driver.find_element(By.ID, "lastName")
        age = driver.find_element(By.ID, "age")
        drp_title = Select(driver.find_element(By.ID, "title"))
        drp_title.select_by_index(0)
        
        name.send_keys("johnjohn")
        last.send_keys("canonc")
        age.send_keys("2")
        
        submit = driver.find_element(By.ID, "submit")
        submit.click()
        
        driver.save_screenshot("john_Test1.png")  # Save screenshot
        
        result = driver.find_element(By.ID, "firstName").text
        self.assertEqual("First Name: johnjohn", result)
        
        driver.close()

    def test_input2(self):
        service = Service('D:\webdriver\chromedriver.exe')
        options = Options()
        options.headless = False
        driver = webdriver.Chrome(service=service, options=options)
        
        driver.get("http://127.0.0.1/customerphp/customer.php")
        
        name = driver.find_element(By.ID, "firstName")
        last = driver.find_element(By.ID, "lastName")
        age = driver.find_element(By.ID, "age")
        drp_title = Select(driver.find_element(By.ID, "title"))
        drp_title.select_by_index(0)
        
        name.send_keys("Johnj")
        last.send_keys("canoncanoncano")
        age.send_keys("149")
        
        submit = driver.find_element(By.ID, "submit")
        submit.click()
        
        driver.save_screenshot("john_Test2.png")  # Save screenshot
        
        result = driver.find_element(By.ID, "firstName").text
        self.assertEqual("First Name: Johnj", result)
        
        driver.close()

    def test_input3(self):
        service = Service('D:\webdriver\chromedriver.exe')
        options = Options()
        options.headless = False
        driver = webdriver.Chrome(service=service, options=options)
        
        driver.get("http://127.0.0.1/customerphp/customer.php")
        
        name = driver.find_element(By.ID, "firstName")
        last = driver.find_element(By.ID, "lastName")
        age = driver.find_element(By.ID, "age")
        drp_title = Select(driver.find_element(By.ID, "title"))
        drp_title.select_by_index(0)
        
        name.send_keys("johnjo")
        last.send_keys("canoncanoncanon")
        age.send_keys("150")
        
        submit = driver.find_element(By.ID, "submit")
        submit.click()
        
        driver.save_screenshot("john_Test3.png")  # Save screenshot
        
        result = driver.find_element(By.ID, "firstName").text
        self.assertEqual("First Name: johnjo", result)
        
        driver.close()

    def test_input4(self):
        service = Service('D:\webdriver\chromedriver.exe')
        options = Options()
        options.headless = False
        driver = webdriver.Chrome(service=service, options=options)
        
        driver.get("http://127.0.0.1/customerphp/customer.php")
        
        name = driver.find_element(By.ID, "firstName")
        last = driver.find_element(By.ID, "lastName")
        age = driver.find_element(By.ID, "age")
        drp_title = Select(driver.find_element(By.ID, "title"))
        drp_title.select_by_index(0)
        
        name.send_keys("johnjohnjohnjo")
        last.send_keys("canoncan")
        age.send_keys("75")
        
        submit = driver.find_element(By.ID, "submit")
        submit.click()
        
        driver.save_screenshot("john_Test4.png")  # Save screenshot
        
        result = driver.find_element(By.ID, "firstName").text
        self.assertEqual("First Name: johnjohnjohnjo", result)
        
        driver.close()

    def test_input5(self):
        service = Service('D:\webdriver\chromedriver.exe')
        options = Options()
        options.headless = False
        driver = webdriver.Chrome(service=service, options=options)
        
        driver.get("http://127.0.0.1/customerphp/customer.php")
        
        name = driver.find_element(By.ID, "firstName")
        last = driver.find_element(By.ID, "lastName")
        age = driver.find_element(By.ID, "age")
        drp_title = Select(driver.find_element(By.ID, "title"))
        drp_title.select_by_index(0)
        
        name.send_keys("johnjohnjohnjoh")
        last.send_keys("canoncan")
        age.send_keys("75")
        
        submit = driver.find_element(By.ID, "submit")
        submit.click()
        
        driver.save_screenshot("john_Test5.png")  # Save screenshot
        
        result = driver.find_element(By.ID, "firstName").text
        self.assertEqual("First Name: johnjohnjohnjoh", result)
        
        driver.close()

    def test_input6(self):
        service = Service('D:\webdriver\chromedriver.exe')
        options = Options()
        options.headless = False
        driver = webdriver.Chrome(service=service, options=options)
        
        driver.get("http://127.0.0.1/customerphp/customer.php")
        
        name = driver.find_element(By.ID, "firstName")
        last = driver.find_element(By.ID, "lastName")
        age = driver.find_element(By.ID, "age")
        drp_title = Select(driver.find_element(By.ID, "title"))
        drp_title.select_by_index(0)
        
        name.send_keys("John")
        last.send_keys("cannoncan")
        age.send_keys("75")
        
        submit = driver.find_element(By.ID, "submit")
        submit.click()
        
        driver.save_screenshot("john_Test6.png")  # Save screenshot
        
        result = driver.find_element(By.ID, "header").text
        self.assertEqual("Customer Detail Form", result)
        
        driver.close()

    @unittest.skip("Skipping Test")
    def test_input7(self):
        service = Service('D:\webdriver\chromedriver.exe')
        options = Options()
        options.headless = False
        driver = webdriver.Chrome(service=service, options=options)
        
        driver.get("http://127.0.0.1/customerphp/customer.php")
        
        name = driver.find_element(By.ID, "firstName")
        last = driver.find_element(By.ID, "lastName")
        age = driver.find_element(By.ID, "age")
        drp_title = Select(driver.find_element(By.ID, "title"))
        drp_title.select_by_index(0)
        
        name.send_keys("johnjohnjohnjohn")
        last.send_keys("cannoncan")
        age.send_keys("75")
        
        submit = driver.find_element(By.ID, "submit")
        submit.click()
        
        driver.save_screenshot("john_Test7.png")  # Save screenshot
        
        result = driver.find_element(By.ID, "header").text
        self.assertEqual("Customer Detail Form", result)
        
        driver.close()
        pass

    def test_input8(self):
        service = Service('D:\webdriver\chromedriver.exe')
        options = Options()
        options.headless = False
        driver = webdriver.Chrome(service=service, options=options)
        
        driver.get("http://127.0.0.1/customerphp/customer.php")
        
        name = driver.find_element(By.ID, "firstName")
        last = driver.find_element(By.ID, "lastName")
        age = driver.find_element(By.ID, "age")
        drp_title = Select(driver.find_element(By.ID, "title"))
        drp_title.select_by_index(0)
        
        name.send_keys("johnjohn")
        last.send_keys("cano")
        age.send_keys("75")
        
        submit = driver.find_element(By.ID, "submit")
        submit.click()
        
        driver.save_screenshot("john_Test8.png")  # Save screenshot
        
        result = driver.find_element(By.ID, "header").text
        self.assertEqual("Customer Detail Form", result)
        
        driver.close()

    @unittest.skip("Skipping Test")
    def test_input9(self):
        service = Service('D:\webdriver\chromedriver.exe')
        options = Options()
        options.headless = False
        driver = webdriver.Chrome(service=service, options=options)
        
        driver.get("http://127.0.0.1/customerphp/customer.php")
        
        name = driver.find_element(By.ID, "firstName")
        last = driver.find_element(By.ID, "lastName")
        age = driver.find_element(By.ID, "age")
        drp_title = Select(driver.find_element(By.ID, "title"))
        drp_title.select_by_index(0)
        
        name.send_keys("johnjohn")
        last.send_keys("canoncanoncanonc")
        age.send_keys("75")
        
        submit = driver.find_element(By.ID, "submit")
        submit.click()
        
        driver.save_screenshot("john_Test9.png")  # Save screenshot
        
        result = driver.find_element(By.ID, "header").text
        self.assertEqual("Customer Detail Form", result)
        
        driver.close()
        pass

    def test_input10(self):
        service = Service('D:\webdriver\chromedriver.exe')
        options = Options()
        options.headless = False
        driver = webdriver.Chrome(service=service, options=options)
        
        driver.get("http://127.0.0.1/customerphp/customer.php")
        
        name = driver.find_element(By.ID, "firstName")
        last = driver.find_element(By.ID, "lastName")
        age = driver.find_element(By.ID, "age")
        drp_title = Select(driver.find_element(By.ID, "title"))
        drp_title.select_by_index(0)
        
        name.send_keys("johnjohn")
        last.send_keys("canoncan")
        age.send_keys("0")
        
        submit = driver.find_element(By.ID, "submit")
        submit.click()
        
        driver.save_screenshot("john_Test10.png")  # Save screenshot
        
        result = driver.find_element(By.ID, "header").text
        self.assertEqual("Customer Detail Form", result)
        
        driver.close()

    def test_input11(self):
        service = Service('D:\webdriver\chromedriver.exe')
        options = Options()
        options.headless = False
        driver = webdriver.Chrome(service=service, options=options)
        
        driver.get("http://127.0.0.1/customerphp/customer.php")
        
        name = driver.find_element(By.ID, "firstName")
        last = driver.find_element(By.ID, "lastName")
        age = driver.find_element(By.ID, "age")
        drp_title = Select(driver.find_element(By.ID, "title"))
        drp_title.select_by_index(0)
        
        name.send_keys("johnjohn")
        last.send_keys("canoncan")
        age.send_keys("151")
        
        submit = driver.find_element(By.ID, "submit")
        submit.click()
        
        driver.save_screenshot("john_Test11.png")  # Save screenshot
        
        result = driver.find_element(By.ID, "header").text
        self.assertEqual("Customer Detail Form", result)
        
        driver.close()

if __name__ == "__main__":
    unittest.main()