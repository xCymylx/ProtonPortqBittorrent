# qBittorrent Port Sync with ProtonVPN

This script is a quick and simple solution to automatically set the qBittorrent port to match the port provided by ProtonVPN.

## Features
- Dynamically retrieves the port number from ProtonVPN.
- Updates the qBittorrent settings to use the specified port.
- Restarts qBittorrent after applying the port

## Requirements
- **ProtonVPN**: Ensure ProtonVPN is installed and running.
- **qBittorrent**: The script modifies qBittorrent's settings, so it must be installed.
- **Windows**: The script uses Windows notifications.

## Usage
1. Run the script while ProtonVPN is active.
2. The script will fetch the port from the Windows notification ProtonVPN sends when setting a port and update qBittorrent's settings accordingly.

## Disclaimer
This script is intended as a quick and dirty solution. It may not handle edge cases or errors gracefully. Use it at your own risk.