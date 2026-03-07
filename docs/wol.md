# Wake on LAN (WoL)
I added WoL to remotely power on devices on my network.
Typically used with [RustDesk](/docs/rustdesk.md).

## WoL Configuration

The WoL service uses Python's `http.server` library on port 8080 to host a web server that features a GUI with 2 buttons, one per user.

When the buttons are pressed, the code uses the _etherwake_ tool to send a magic packet via the MAC address of the target machine.

Because `http.server` doesn't persist after the terminal session is closed, I've configured it as a systemd service.

`.service` file: [wol-server.service.example](/configs/wol-server/wol-server.service.example)

The WoL code: [wol-server.py](/configs/wol-server/wol-server.py)

## Web Interface

![Site Preview](/images/WoL/SitePreview.png)
