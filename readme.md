# Network Control System

The Network Control System is a web-based application designed to manage and monitor network devices. It allows users to add, update, and delete network devices, and provides a system dashboard for monitoring performance data.

## Features

- **Network Device Management:**

  - Add new network devices with details such as name, status, and quantity.
  - Update and delete existing network devices.
- **Performance Monitoring:**

  - View real-time performance data of network devices.
  - Performance data includes CPU usage, memory usage, timestamp, and device details.

## Screenshots

### Network Device List

![Network Device List](https://github.com/Levi-Chinecherem/network-control-system/blob/main/samples/p4.png)

### System Dashboard

![System Dashboard](https://github.com/Levi-Chinecherem/network-control-system/blob/main/samples/p5.png)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Levi-Chinecherem/network-control-system.git

   ```
2. Create a virtual environment and install dependencies:

   ```bash
   cd network-control-system
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
3. Apply migrations:

   ```bash
   python manage.py migrate
   ```
4. Run the development server:

   ```bash
   python manage.py runserver
   ```

   The application will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Usage

1. Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser.
2. Log in or create an account.
3. Explore the Network Device List, add new devices, and navigate to the System Dashboard to monitor performance.

## Contributing

If you'd like to contribute to the project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
