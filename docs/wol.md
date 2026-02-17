# Wake on LAN (WoL)

The WoL code is shown [here](/configs/wol-server/wol-server.py), and it uses Python to host a web server that features a GUI with 2 buttons, each for me and my brother.
When the buttons are pressed, the code uses the _etherwake_ tool, to send a magic packet via the MAC address of the selected person's PC.

For stability, I chose to run it as a systemd service, `.service` file is shown [here](/configs/wol-server/wol-server.service.example)


## Site for Reference

![Site Preview](/images/WoL/SitePreview.png)

_Names are hidden._