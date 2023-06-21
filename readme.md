# Sri Lanka Administrative Data API

👋 Welcome to the Sri Lanka Administrative Data API repository! This API provides access to provinces, districts, and division data in Sri Lanka.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/sudeepaviraj/gn-extract.git
```

2. Navigate to the project directory:

```bash
cd gn-extract
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Config

You Need to config this before use

1. Import ```srilanka.sql``` to your own sql server


2. Update connection values in ```database.py```

```
connection = mysql.connector.connect(
        host="YOUR_DATABSE_HOST",
        port=3306,
        user="YOUR DATABASE USER",
        password="YOUR DATABASE PASSWORD",
        database="YOUR DATABASE"
    )
```

## Usage

1. Run the application:

```bash
python app.py
```

2. Once the application is running, you can access the API endpoints:

- **Get all provinces**: `/provinces`
- **Get all districts**: `/districts`
- **Get all divisions**: `/divisions`
- **Get all districts in a province**: `/getdistricts?province={province_id}`
- **Get all divisions in a district**: `/getdivisons?district={district_id}`

3. Make HTTP GET requests to the desired endpoints using tools like `curl` or `Postman` to retrieve the administrative data.

Example request using `curl`:

```bash
curl http://localhost:5000/provinces
```

Example response:

```json
[
    {
        "id": 1,
        "name": "Western"
    },
    {
        "id": 2,
        "name": "Central"
    },
]
```


## *Special Note*

**You can run sql queries form your own mysql server directly. To do that please use database file ```srilanka.sql``` to your own mysql server**

## Contributing

We welcome contributions to improve this project! If you'd like to contribute, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature:

```bash
git checkout -b feature/your-feature-name
```

3. Make your changes and commit them:

```bash
git commit -m "Add your commit message"
```

4. Push your changes to your forked repository:

```bash
git push origin feature/your-feature-name
```

5. Open a pull request, and we'll review your changes.

## License

This project is licensed under the [MIT License](LICENSE).
