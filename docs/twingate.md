# Twingate

<p align="center">
    <img  src="../images/Twingate/TwingateLogo.png" width="300">
</p>

At the beginning, Twingate ran on Docker, and one time I was working remotely on my Raspberry Pi, and I wanted to restart the Docker compose.

Up until now, everything sounds normal, the problem was, that instead of just using the command:

```bash
docker compose up -d
```
to restart it, I firstly turned it off, then tried to turn it back on with the commands:

```bash
docker compose down
docker compose up -d
```
The problem is, because Twingate ran on Docker, the second I shut down the Docker compose file, I couldn't turn it back on :)

Since then, Twingate is running as a systemd service.

---

All jokes aside, I chose Twingate as a part of NetworkChuck's tutorial (link in [overview](overview.md)) for secure remote access to my network.

Twingate is a great zero-trust platform, combining a secure split-tunnel to my home network, without exposing any internal services to the internet, like standard port forwarding would've done.

## Twingate Configuration
For installation and initial setup, please refer to the [official Twingate documentations](https://www.twingate.com/docs/quick-start).



Systemd `.service` file shown [here](/configs/Twingate/twingate-connector.service.example)

Environment file is shown [here](/configs/Twingate/connector.conf.example)