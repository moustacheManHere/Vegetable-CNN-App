Image Storage:
    - To store all the images submitted by the user, I will be using a cloud database like AWS S3
    - For the first part, i will upload some vegetable images to the databse to store inside
    - I just signed up for a AWS account under my school email. 
    - To install AWS CLI `curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o "awscliv2.zip"`
    - `unzip awscliv2.zip`
    - `./aws/install`
    - Run `aws configure` and paste in secret keys
    - thats it now we have the aws cli installed. 
    - Default region is ap-southeast-1
    - We will also run  `pip install boto3`
    - Refer to test.ipynb for code on interacting with db
    - to create the environment to run this, you need to pass in the secret user auth details. 

Vegetable DB:
    - To display a catalogue of vegetables right now supported as well as letting user know more details, I will be usign a vege database. The initial info for this db is in the vegeDB. but i will try to make a function to add more info as time goes on. 
    - I will init the database using this csv