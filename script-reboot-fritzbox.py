#!/usr/bin/python
# coding=utf-8

#README
        # python script to restart fritz.box via webscraping (webdriver pretends to be an user)
        # cause of development
            # no programmable interface to restart fritz.box via protocol
            # no possibility for a restart schedule w/ fritz.box
        # useful to restart your fritz.box sometimes, to reset network protocols

        # developed for MAC
        # by /flo (@slashflo)

        # dependencies (install before using)
        # recommended order:        << terminal commands >>
            # homebrew:             /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
            # python3&pip3:         brew install python
            # selenium:             pip3 install selenium
            # webdriver-manager:    pip3 install webdriver-manager
            # chromedriver:         brew install chromedriver

        # values (change before using)
            # line 70          (NOT NECESSARY) 192.168.0.1 basic fritz.box IP Adress
            # line 74          (NOT NECESSARY) "LOCATION 1" -> change Location Name for log.txt (not necessary)
            # line 90          (ONLY REMOTE) "USERNAME" -> change only if you want to use this script for remote myfritz.net
            # line 96          (NECESSARY) "PASSWORD" -> change to your Password for your fritz.box

        # run program by these commands
            # change directory to file location (for example):     
                # cd /Users/USERNAME/Desktop
            # run program with this command:
                # python3 script-reboot-fritzbox.py

# import modules
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

# just needed to reboot multiple remote fritzbox's via MYFRITZ!NET
    # websites = ["https://1234testtest1234.myfritz.net:12345/", 
    #             "https://4321tsettset4321.myfritz.net:67891/", 
    #             "https://1220testtest1220.myfritz.net:54321/"]

# website list
websites = ["http://192.168.0.1/"]  # local network standard IP for fritz.box login |OR| standard address "http://fritz.box/"

# change settings that chrome webdriver starts as maximized window
options = Options()
options.add_argument("start-maximized")

# starts chrome webdriver for every website in "websites list"
for IPAddress in websites:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) 
    driver.get(IPAddress)

    # opens a log file in the same directory as file location
    logFile = open("log.txt", "a")
    now = datetime.now()
    dt_time = now.strftime("%Y-%m-%d, %H:%M:%S")

    # give IPAdress a name for log.txt
    if IPAddress == "http://192.168.0.1/":
        # LocationName is the value to name the location in log.txt
            # you can change "LOCATION 1" to a logical adress, for example "Berlin"
            # than the log.txt would write "Router restarted @ Berlin"
        LocationName = "LOCATION 1"

    # just for multiple locations
    # elif IPAddress == "http://fritz.box/":
    #    LocationName = "LOCATION 2"
    # elif IPAddress == "https://1234testtest1234.myfritz.net:12345/":
    #    LocationName = "LOCATION 3"
    
    else:
        LocationName = "RoadToNowHere"

    try:
        # just needed when using multiple remote reboots via MYFRITZ!NET
            # element = WebDriverWait(driver, 20).until(                    
            #    ec.visibility_of_element_located((By.ID, "uiViewUser"))
            # )
            # element.send_keys("USERNAME")

        element = WebDriverWait(driver, 20).until(
            ec.visibility_of_element_located((By.ID, "uiPass"))
        )
        # types password for fritzbox
        element.send_keys("PASSWORD")
        
        # construction following element segments
            # WebDriverWait -> waits up to for example 20 sec for the next button
            # ec.visibility_of_element_located((By.ID, "By.ID-Name")) -> chooses element depending on the ID Name
            # to find the ID names use right click on the Button/Field, than select Inspect Element
                # |OR| use F12 in your browser, than expand the html code till you find the ID of the Button/Field you need
            # element.click() -> executes click on the selected element

        #element = WebDriverWait(driver, 20).until(
        #    ec.visibility_of_element_located((By.ID, "submitLoginBtn"))
        #)
        #element.click()

        #test vodafone
        element = WebDriverWait(driver, 20).until(
            ec.visibility_of_element_located((By.ID, "LoginBtn_m"))
        )
        element.click()

        element = WebDriverWait(driver, 20).until(
            ec.visibility_of_element_located((By.ID, "sys"))
        )
        element.click()

        element = WebDriverWait(driver, 20).until(
            ec.visibility_of_element_located((By.ID, "mSave"))
        )
        element.click()

        element = WebDriverWait(driver, 30).until(
            ec.visibility_of_element_located((By.ID, "uiDoConfigExport"))
        )

        element = WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located((By.ID, "reboot"))
        )
        element.click()

        element = WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located((By.ID, "btnReboot"))
        )
        element.click()

        # wait 7 seconds that the restart can be executed formerly
        time.sleep(7)

        # appends Date, Time, Router restarted @ Location to log.txt
        logFile.write(dt_time+ " Router restarted @ " +LocationName+ "\n")

        # closes logFile writer
        logFile.close()

        # closes ChromeDriver "webdriver"
        driver.quit()

    except:
        # appends Date, Time ERROR RESTARTING @ Location to log.txt
        logFile.write(dt_time+ " ERROR RESTARTING @ " +LocationName+ "\n")
        logFile.close()
        driver.quit()
        
    finally:
        driver.quit()
