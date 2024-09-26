
# FitGirl Repacks API

This is a simple API for fetching torrent links and magnet links from FitGirl Repacks.

## Features
- Fetch torrent links using `/torrent/<link-to-page>`
- Fetch magnet links using `/magnet/<link-to-page>`

## Installation

1. Clone the repository:

   ```bash
   git clone [<repository-url>](https://github.com/blazturk/fitgirl-repacks-api)
   cd fitgirl-repacks-api
   ```

2. Install the necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the API:

   ```bash
   python app.py
   ```

## API Endpoints

### Fetch Torrent Link

- **Endpoint:** `/torrent/<link-to-page>`
- **Method:** `GET`
- **Description:** This endpoint fetches the torrent link from the provided FitGirl Repack page URL.
- **Example:**

   ```bash
   curl http://localhost:5000/torrent/<link-to-page>
   ```

### Fetch Magnet Link

- **Endpoint:** `/magnet/<link-to-page>`
- **Method:** `GET`
- **Description:** This endpoint fetches the magnet link from the provided FitGirl Repack page URL.
- **Example:**

   ```bash
   curl http://localhost:5000/magnet/<link-to-page>
   ```

## Usage Example

1. Fetch a torrent link:

   ```bash
   curl http://localhost:5000/torrent/fitgirl-repacks.site/red-dead-redemption-2/
   ```

2. Fetch a magnet link:

   ```bash
   curl http://localhost:5000/magnet/fitgirl-repacks.site/red-dead-redemption-2/
   ```

## Contributing

Contributions are welcome! Feel free to open a pull request or create an issue if you encounter any bugs or have suggestions for new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
