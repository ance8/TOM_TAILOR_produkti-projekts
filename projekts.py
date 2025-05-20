from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import re

def load_all_products(driver):
   last_height = driver.execute_script("return document.body.scrollHeight")
   for _ in range(10):
       driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
       new_height = driver.execute_script("return document.body.scrollHeight")
       if new_height == last_height:
           break
       last_height = new_height
      
def accept_cookies(driver):
   try:
       cookie_button = driver.find_element(By.XPATH, '//button[contains(text(), "Accept All Cookies")]')
       cookie_button.click()
   except Exception:
       pass
      
def extract_products(html):
   pattern = r'"name"\s*:\s*"([^"]+)"[^}]*?"currency"\s*:\s*"EUR",\s*"price"\s*:\s*(\d+\.\d{2})'
   matches = re.findall(pattern, html)
   products = []
   for name, price in matches:
       price = float(price)
       products.append((name, price))
   return products
   
def sort_products(products, mode_number):
   if mode_number == "1":
       return sorted(products, key=lambda x: x[1])
   elif mode_number == "2":
       return sorted(products, key=lambda x: x[1], reverse=True)
   elif mode_number == "3":
       return sorted(products, key=lambda x: x[0].lower())
   else:
       return products
      
def product_search_loop():
   URLS = {
       "women": "https://www.tom-tailor.eu/women/new",
       "men": "https://www.tom-tailor.eu/men/new",
       "kids": "https://www.tom-tailor.eu/kids/new"
   }
   while True:
       choice = input("Enter category (women, men or kids): ").strip().lower()
       if choice not in URLS:
           print("Invalid choice. Try again.")
           continue
       sort_mode = input("Enter sorting mode: 1 - price↑  2 - price↓  3 - alphabetical: ").strip()
       if sort_mode not in {"1", "2", "3"}:
           print("Invalid sort mode. Defaulting to 1 (price↑).")
           sort_mode = "1"
          
       options = Options()
       options.add_argument("--headless=new")
       options.add_argument("--disable-gpu")
       options.add_argument("--window-size=1920,1080")
       options.add_argument("--disable-extensions")
       options.add_argument("--no-sandbox")
       options.add_argument("--disable-dev-shm-usage")
       driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
       driver.get(URLS[choice])
       accept_cookies(driver)
       load_all_products(driver)
       html = driver.page_source
       driver.quit()
       products = extract_products(html)
      
       if not products:
           print("No products found. Page saved.")
           with open("page_dump.html", "w", encoding="utf-8") as f:
               f.write(html)
           continue
          
       products = sort_products(products, sort_mode)
      
       while True:
           search = input("Enter product name (or 'all' to show all products, 'back' to choose category again): ").strip().lower()
           if search == "back":
               break
           elif search == "all":
               print(f"\n--- All Products (sort mode {sort_mode}) ---")
               for name, price in products:
                   print(f"{name} — {price:.2f} €")
           else:
               filtered = [prod for prod in products if search in prod[0].lower()]
               if filtered:
                   print(f"\n--- Found Products (sort mode {sort_mode}) ---")
                   for name, price in filtered:
                       print(f"{name} — {price:.2f} €")
               else:
                   print("No matching products. Try another search term.")
                  
product_search_loop()
