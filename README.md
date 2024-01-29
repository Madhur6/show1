# Anime
 Load External JSON data into the Django Models


## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/your-repository.git

2. **Navigate to the Project Directory:**
   ```bash
   cd your-repository

3. **Create a Virtual Environment:**
   ```bash
   python -m venv venv

4. **Activate the Virtual Environment:**

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

6. **Run Migrations:**
   ```bash
   python manage.py makemigrations network/app-name
   python manage.py migrate

7. **Run the Development Server:**
   ```bash
   python manage.py runserver

8. **Access the App:**
   Open your web browser and navigate to http://127.0.0.1:8000/.

The API will be accessible at `http://127.0.0.1:8000/`.

## API Endpoints

### Get List of Animes

- **URL:** `/`
- **Method:** `GET, POST`
- **Response:{
    "animes": [
      {
        "title": "My Hero Academia",
        "genre": ["Action", "Superhero", "Shonen"],
        "studio": "Bones",
        "episodes": 100
      }, ...
    ]
}**
  ```json


### Get Specific Anime via id
- **URL:** `addData/<int:id>`
- **Method:** `GET, PUT, DELETE`
- **Response:**
  ```json

## License

This project is licensed under the MIT License.
