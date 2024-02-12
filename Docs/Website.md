Concept:
    - To abit of backstory to a boring image prediction site, I added a fictional character called "Tommy the Tomato"
    - The website will revolve around this Tomato predicting what vegetable photo you uploaded
    - Website will ideally be red themed around tomatos
    - The vegetable catalogue will accordinly be themed to be called "Tomato's Friends". The backstory is that just like our dataset has only 15 classes, there are only 15 vegetables in tomato's gang. This branding helps us add more vegetables to this dataset and widen tomato's gang. 
    - Login/Signup will be renamed as "Join Tomato's Gang"

Run App with `flask --debug run`

Pages
    - Home
    - Profile
    - Login
    - Logout
    - Vegetables supported -> click to view info -> order alphabetically
    - Predict -> show fruit and link to pic
    - Info/{id} -> fruit id
    - History page
    - Error HTML
    - Not Authorised HTML

History Search:
    - Contains:
        - Image (low res)
        - Image_path_name
        - Comment
        - Date
        - Prediction Name
        - Prediction %
        - Remove?

Ideas:
    - In the /includes folder create a template that will take in any form and display its values

User Authentication:
    - For user auth, its mostly the same as CA2
    - I edited the handling of permissions. So like if the user goes to a route they are not supposed to it will show a nice error page instead of reidrecting them to the home page. 
    - I also edited the pytest to be more effective and only test boundary cases

Search Feature:
    - Initially I wanted to add tags. so user can add tags to the images and search them easily later. but instead of doing this, i decided to have comments and then when the user searchs, it will find the best match.
    - As advised for ca1, i will be dynamically generating the options instead of hard coding them for this form.
    - For the comments search, i will be using TF-IDF to find the best match. basically it will calculate the frequency of terms and i will rank it using cosine similiarty to the original query. This ranking mechanism ensures that even if the user enters a weird query, there will still be reults show albeit not in the desired order. 