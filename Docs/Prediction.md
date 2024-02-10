Image Receving Functionality:
    - I will be using Flask Reuploaded to handle image upload by the user. 
    - Install it using `pip install Flask_Reuploaded`
    - After some struggle with the file saving and loading i realised that the magic is to specify `UPLOADS_DEFAULT_DEST` to application/static cuz I realised it was saving images to the root of the project
    - Another problem was that even after setting `UPLOADED_PHOTOS_DEST` to something like "images" it was creating a subfolder called "uploads" within images and saving it there so I saved to "uploads" instead. 
    - The path of the image taken using send_from_direcotry was not the same as the actual path as the default destination was changed and needs to be uploaded. I tried all workaround but the most only way that worked is manully specifying path. this is bad cuz i were to change the default destination, alot more things will need to be changed. But this is taking too much time and i need to move on. 
    - One problem to potentially fix is the problem with duplicates. when i upload the same images it keep many copies without checking if the images are the same. Maybe try fix this

Problems with Image Receing: 
    - After using the flask reuploaded shit for a while, its quite troublesome. my images directory is filled with images. each time i test the prediction it is saving the image.
    - Unless the user logs in, there should be no need to save the images.
    - I will be removing the image saving shit and just using the bytestring of the image.