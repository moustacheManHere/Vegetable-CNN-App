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