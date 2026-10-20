# Wake on LAN (WoL)

I added WoL to remotely power on devices on my network.
Typically used to wake a PC up before connecting to it via [RustDesk](/docs/rustdesk.md).

## WoL Configuration

The WoL service uses Python's `http.server` library on port 8080 to host a web server that features a GUI with 2 buttons, one per user.

When a button is pressed, the code uses the `etherwake` tool to send a magic packet to the target machine's MAC address.

Previously, the users' MAC addresses were hardcoded in the Python script. Now they are saved in an environment file, and are read by the `os` module.

WoL environment file example: [wol.env.example](/configs/wol-server/wol.env.example)

The WoL code: [wol-server.py](/configs/wol-server/wol-server.py)

> [!NOTE]
>
> The code was generated with [Claude AI](https://claude.ai), and adjusted to my homelab needs. 
>
> The code is built for 2 users. If you plan on using this code, make sure to adjust it to your needs.

## Running as a systemd Service

Because `http.server` doesn't persist after the terminal session is closed, I've configured it as a systemd service.

Previously, the service ran as root. Now it runs with least privilege by using a dynamic user with a single capability, `CAP_NET_RAW`, which `etherwake` needs to send raw packets.

Systemd service file example: [wol-server.service.example](/configs/wol-server/wol-server.service.example)

## Web Interface

![Site Preview](/images/WoL/SitePreview.png)

> [!NOTE]
>
> Button labels are placeholders.