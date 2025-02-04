# OmniCenter

OmniCenter is a Python-based tool designed to enhance network exploration and management for Windows users, aiding in improving connectivity and speed.

## Features

- **Display Network Information:** Shows the hostname and local IP address.
- **List Network Adapters:** Lists all network adapters along with their IP addresses.
- **Ping Test:** Checks connectivity to a specified host (default is Google's DNS server 8.8.8.8).
- **Speed Test:** Measures the current download and upload speeds using Speedtest.
- **Network Optimization:** Placeholder for future network optimization features.

## Requirements

- Python 3.x
- `psutil` library
- `speedtest-cli` library

## Installation

1. Clone this repository or download the `omnicenter.py` file.
2. Install the required libraries using pip:
   ```
   pip install psutil speedtest-cli
   ```

## Usage

Run the script using Python:

```bash
python omnicenter.py
```

The program will display network information, list network adapters, perform a ping test, conduct a speed test, and attempt network optimization.

## Future Enhancements

- Implement actual network optimization techniques.
- Provide a graphical user interface (GUI).
- Include more detailed network diagnostics.

## Notes

- Ensure you have administrative privileges to run network configuration commands.
- This script is designed for Windows users; functionality on other operating systems may vary.

## Contribution

Feel free to contribute to this project by submitting issues or pull requests. 

## License

This project is open source and available under the MIT License.