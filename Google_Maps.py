from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\shan2\\Downloads\\Selejars\\chromedriver.exe")

driver.get("https://www.google.com/maps/@12.8412514,80.2209766,15z")
driver.maximize_window()
time.sleep(2)


def search_place():
    location = driver.find_element_by_class_name("tactile-searchbox-input")
    location.send_keys("Chennai")
    submit = driver.find_element_by_class_name("searchbox-searchbutton")
    submit.click()

search_place()


def directions():
    time.sleep(5)
    direction = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/div/button/img")
    direction.click()

directions()


def my_place():
    time.sleep(5)
    my_place = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
    my_place.clear()
    my_place.send_keys("Ranchi")
    time.sleep(5)
    search = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
    search.click()

my_place()

def distance():
    time.sleep(5)
    distance = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]/div[2]/div/div[1]/div[1]/div[2]/div")
    print("Total Distance: ", distance.text)
    road = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]/div[2]/div/div[1]/div[1]/div[1]/span[1]")
    print("Time by Road: ", road.text )
    train = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]/div[1]/div/div[2]/div[1]/div")
    print("Time by train: ", train.text)
    air = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]/div[3]/div/div[4]/div[1]/div/div[1]")
    print("Time by air: ", air.text)

distance()

driver.quit()