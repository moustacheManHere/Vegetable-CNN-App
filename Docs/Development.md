Creating Development Container:
    - docker pull python:3.9.18 -> using cuz its same as my mac
    - Ran 
    ```docker run -it -v /var/run/docker.sock:/var/run/docker.sock --name Web_Server python:3.9.18 sh -c "apt-get update ; apt-get install docker.io -y ; bash" ```
    - Used VSCode Remote Explorer to open up container and pulled my git repo
    - python -m venv env -> in the root not project folder as I dont want my env to be in the git
    - git clone https://gitlab.com/4618-devops/ca2-daaa2b01-2214618-jeyakumarsriram.git
    - source ./env/bin/activate
    - python -m pip install flask
    - pip install -U Flask-SQLAlchemy Flask-WTF
    - pip install gunicorn flask_cors Pillow
    - pip freeze >> ca2-daaa2b01-2214618-jeyakumarsriram/requirements.txt
    - apt-get install iputils-ping
    - docker network connect dl_network Web_Server
    - Later if needed can setup again but simply using the requirements.txt file

Storing Static Files:
    - To store static files like images, we will be using git lfs. it is not good practice to commit them as they are not like normal files and will be very ineffcient. 
    - `curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash` to download it inside our dev container
    - `apt-get install git-lfs` to install it.
    - `git lfs install` to init lfs in my repo
    - `git lfs track "application/static/images/*"` to track all images in my folder
    - `git lfs track "Docs/Screenshots/*"`

Setting up Docker Container to run app:
    - I faced quite some challenge trying to run my docker image cuz port 5000 was always not aviaalble. apparently on apple, the port 5000 is used by airplay. It is very weird cuz I can run my flask app directly from command line without worrying but the docker image doesn't allow me to map to port 5000. One quick and easy fix i foudn was just changing it to 5001 and it worked. 

Deployment:
    - Initially I faced some error trying to deploy the app and tried for a while. Eventually solved it by making "relases" a protected branch.

Secrets Management:
    - I faced a secutiry issue when deploying my docker app. in my local docker image, i configured the aws cli manually. but on docker, i will need to pass in those arguments to run.
    - A solution I am considering is passing my aws credntial sinto the gitlab secrets file and then building a image based on it. then saving the image to my gitlab image registry and deploying to render based on it. 
    - The previous solutij didnt work out. Another simpler solution i found is using environment varibales as stated on the aws documentation. the boto3.resource will auto detect env variabls.
    - Even tho the tests passed in gitlab, there was a strange error with render. for somereaosn gunicorn was running out off memory. it ws very strange

Database Persistence:
    - To ensur that my DB is persistent across the deployments, I will be using the Disks feature from render which mounts a persistance storage to each deplyoment. This allows my app to keep user data without wiping eveyrhting out everytime.
    - Nvm I will abandon this experiment as most of such services are paid and im not allowed to use them for assignment. 