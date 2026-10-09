# Twingate

Twingate is a zero-trust platform, combining a secure split-tunnel to my home network, without exposing any internal services to the internet, like standard port forwarding would've done.

---

Initially, Twingate ran as a Docker container. One time I was working remotely on my homelab, and I wanted to restart the Docker compose.

Instead of using `docker compose up -d` to restart, I ran:

```bash
docker compose down
docker compose up -d
```

Because Twingate ran on Docker, the moment I shut down the Docker compose file, I couldn't turn it back on.

Since that incident, Twingate is running as a systemd service.

## Twingate Installation
For installation and initial setup, please refer to the [official Twingate documentation](https://www.twingate.com/docs/quick-start).

## Twingate Configuration
`.service` file that runs Twingate connector as a systemd daemon: [twingate-connector.service.example](/configs/Twingate/twingate-connector.service.example)

Twingate environment file that contains placeholder values for Twingate access tokens: [connector.conf.example](/configs/Twingate/connector.conf.example)

### Resource Access

For the Raspberry Pi resource, I allow all the ports my services use.
<p align="center">
    <img  src="../images/Twingate/RaspberryPiResource.png">
</p>

> [!NOTE]
>
> Twingate's port restrictions control traffic over the tunnel, while [UFW](/docs/security-hardening.md#firewall) controls traffic at OS level. 

For my PC resource, I only allow RustDesk's ports.
<p align="center">
    <img  src="../images/Twingate/EliahPCResource.png">
</p>
