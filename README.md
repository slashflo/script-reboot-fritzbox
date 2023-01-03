# script-reboot-fritzbox
# python script to restart fritz.box via webscraping (webdriver pretends to be an user)
# cause of development
    # no programmable interface to restart fritz.box via protocol
    # no possibility for a restart schedule w/ fritz.box
# useful to restart your fritz.box sometimes, to reset network protocols

# developed for MAC
# by /flo (@slashflo)

# dependencies (install before using)
    # recommended order:    << terminal commands >>
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
