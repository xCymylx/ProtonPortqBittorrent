import sqlite3
import os
import time

# Path to notifications database
db_path = os.path.expandvars(r'$LOCALAPPDATA\Microsoft\Windows\Notifications\wpndatabase.db')

# Start database connection
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("SELECT payload FROM notification")
rows = cursor.fetchall()

# Extract active port from payload and set port number to lastest port
for row in rows:
    payload = row[0]
    if isinstance(payload, bytes):
        payload = payload.decode('utf-8', errors='ignore')
    if "Active port: " in payload:
        start_index = payload.index("Active port: ") + len("Active port: ")
        end_index = start_index + 5
        active_port = payload[start_index:end_index]
        if not active_port.isdigit():
            exit()

# Close database connection
conn.close()

print(f"Active port: {active_port}")

# Path to qBittorrent configuration file
qbittorrent_config_path = os.path.expandvars(r'$APPDATA\qBittorrent\qBittorrent.ini')

# Read and modify the configuration file
with open(qbittorrent_config_path, 'r') as file:
    lines = file.readlines()

with open(qbittorrent_config_path, 'w') as file:
    for line in lines:
        if line.startswith("Session\\Port="):
            line = f"Session\\Port={active_port}\n"
        file.write(line)

# Kill qBittorrent
os.system("taskkill /IM qbittorrent.exe /F")
time.sleep(1)  # Wait for the process to terminate

# Start qBittorrent with the updated configuration
os.system(r'start "" "C:\Program Files\qBittorrent\qbittorrent.exe"')
