# Tommy's Vege Game

Welcome to Tommy's Vege Game! This web application is designed to assist users in identifying various vegetables by analyzing images uploaded by the user. Whether you're a vegetable enthusiast or just looking to expand your knowledge, Tommy's Vege Game has got you covered.

## Features

- **Predict Vegetable**: Upload an image containing a vegetable, and our deep learning model will predict its type.
- **Catalogue**: Explore a catalogue of various vegetables our model can predict.
- **Vegetable Information**: Get detailed information about a specific vegetable.
- **User System**: Create an account to view your prediction history, including previously uploaded images and their predictions.

## Getting Started

To play Tommy's Vege Game, please go to [this link](https://tommyvegetablegame.onrender.com)

If you are a developer, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using the following command:

   ```
   git clone https://gitlab.com/4618-devops/ca2-daaa2b01-2214618-jeyakumarsriram.git
   ```

2. **Setup Development Environment**: Ensure you have docker installed and run the following:

    ```bash
    docker run -it -v /var/run/docker.sock:/var/run/docker.sock --name Web_Server python:3.9.18 sh -c "apt-get update ; apt-get install docker.io -y ; bash"
    ```

    Once done, use VSCode's Remote Explorer to code inside this container.

3. **Install Dependencies**: Navigate to the project directory and install the required dependencies using pip:

   ```
   python -m venv env
   source /env/bin/activate
   pip install -r requirements.txt
   ```

4. **Run the Application**: Start the Flask application by running the following command:

   ```
   flask --debug run
   ```

5. **Access the Application**: Open your web browser and navigate to [http://localhost:5000](http://localhost:5000) to access Tommy's Vege Game.

6. **Testing Application**: To test the application run:

    ```bash
    python -m pytest
    ```

### Project Structure

| Folder                | Purpose                                        |
| --------------------- | ---------------------------------------------- |
| Docs                  | Project documentation with Screenshots         |
| Wireframes            | Wireframes for UI design                       |
| application           | Main application directory                     |
| application/static    | Static files (CSS, images) for the application |
| application/templates | Jinja templates for the application            |
| instance              | SQLite DB for Flask App                        |
| tests                 | PyTest scripts and fixtures for application    |
| temp_imgs             | Temporary images used to initialise S3 Bucket  |

## Usage

Once the application is running, you can start using the various features provided:

- Upload an image containing a vegetable to get a prediction.
- Explore the catalogue to learn about different vegetables.
- Click on a vegetable to view detailed information about it.
- Log in to access your prediction history and manage your profile.
- Sign up for a new account if you don't have one already.

## Contributing

We welcome contributions from the community to improve Tommy's Vege Game. If you have any ideas, suggestions, or bug fixes, please feel free to submit a pull request or open an issue on GitHub.

A special thanks to Mr Sng Yong Meng for his guidance throughout the projects.

## License

This project is licensed under the MIT License.
