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
    