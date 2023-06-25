# Sri Lanka Administrative Data API

👋 Welcome to the Sri Lanka Administrative Data API repository! This API provides access to provinces, districts, and division data in Sri Lanka.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/sudeepaviraj/administrative-api-srilanka.git
```

2. Navigate to the project directory:

```bash
cd administrative-api-srilanka
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Config

You Need to configure this application before use
1. Create a database named ```srilankav2``` in your sql server 


2. Import ```srilanka.sql``` to your own sql server


3. Create a ```.env``` file and add database connection values 

```
DATABASE_HOST="YOUR DATABASE HOST"
DATABASE_PORT="YOUR DATABASE PORT"
DATABASE_USER="YOUR DATABASE USER"
DATABASE_PASSWORD="YOUR DATABASE PASSWORD"
DATABASE_NAME="srilankav2"
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
- **Get all villages in a division**: `/villages?division={division_id}`

3. Make HTTP GET requests to the desired endpoints using tools like `curl` or `Postman` to retrieve the administrative data.

Example request using `curl`:

```bash
curl http://localhost:5000/provinces
```

Example response:

```json
[   
  [
    63,
    "Western",
    "බස්නාහිර",
    "மேற்கு"
  ],
  [
    64,
    "Central",
    "මධ්‍යම",
    "மத்திய"
  ]
]
```
## Response Structure

```provinces,districts and divisions```
```json
 [
   "PROVINCE_ID",
   "NAME_EN",
   "NAME_SI",
   "NAME_TA"
 ]
```
```villages```
```json
 [
   [
    "LIFE_CODE",
    "GN_CODE",
    "MPA_CODE",
    "NAME_EN",
    "NAME_SI",
    "NAME_TA"
  ]
 ]
```

## Demo API Endpoint

**Under Development**

```http://db.famed.cloud/```

## *Special Note*

**You can run sql queries form your own application directly. To do that please use database file ```srilanka.sql``` to your own mysql server**

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
