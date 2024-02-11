PyTest:
    - As in CA1 I will be using pytest to manage all my tests. 
    - For GUI, i wil use selenium to autmate interactions with webpage like clikcing and whatever
    - For the rest I will just use the test_client of the app and test it 
    - One error when testing the app is the csrf error. Initially I fixed it by disabling csrf for the testing app but Later i found a way around it. 

Getting Selenium Working:
    - I couldnt get selenium to work within my python docker image and faced many download issues
    - Decided to use selenium separately using the selenium image. so i did `docker pull selenium/standalone-chrome` but it wasn't compatible wiht my ARM chip so i had to use a arm compatible one whcih is   `docker pull seleniarm/standalone-chromium:latest`
    - inside the containde i ran 
        sudo apt-get update
        sudo apt-get install -y python3-pip
    - after setting up pip, i will install pytest `sudo apt install python3-pytest` have to do it this way cuz pip cannot install shit system-wide
    - then i download selenium `sudo apt install python3-selenium`
    - Ok all this is very painful and doesnt seem to be working
    - I dont belieive this is the right approahc and  iwill revisit this later

Struggles with DB Testing:
    - I know for my CA1 the apporahc of adding and chaging a production db is not the best idea. So I wanted a diff approahc
    - First I tried creating a new db during pytest and using that for the tests. As you can see in my previous commit files, it was a giant mess. idk wth i was doing and sought a simpler approach
    - I simply use a db create and tear down function. this way when the test runs,. the db will be populated correctly and then torn down after doing so. i tested to see if it changes the actual db and it doesn't seem to . 
