import undetected_chromedriver as uc
import pickle

driver = uc.Chrome(use_subprocess=True)
driver.get("https://google.com/")

while True:
    inp = input()
    if (inp == "go"):
        pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
        print("Cookies have been saved")
