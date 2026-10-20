# Twingate

Twingate is a zero-trust platform, providing a secure split-tunnel to my home network, without exposing any internal services to the internet, unlike standard port forwarding.

**Installation:** [official Twingate documentation](https://www.twingate.com/docs/quick-start).

---

## Why Twingate runs as systemd service

Initially, Twingate ran as a Docker container. One time I was working remotely on my homelab, and I wanted to restart the Docker compose.

Instead of using `docker compose up -d` to restart, I ran:

```bash
docker compose down
docker compose up -d
```

Because Twingate ran on Docker, the moment I shut down the Docker compose file, I couldn't turn it back on.

Since that incident, Twingate has been running as a systemd service.

## Twingate Configuration

Twingate environment file that the systemd service uses: [connector.conf.example](/configs/Twingate/connector.conf.example) (placeholder values).

### Resource Access

| Resource | Allowed ports | Access | Used for |
|---|---|---|---|
| Pi - users | 8080/TCP, 21115-21117/TCP, 21116/UDP, ICMP | Everyone | WoL, RustDesk (relay), ping |
| Pi - admins | 22/TCP | Admins | SSH |
| NAS - users | 445/TCP, ICMP | Everyone | SMB, ping |
| NAS - admins | 80/TCP (IP redirect), 8543/TCP (hostname) | Admins | Web interface |
| PC | ICMP | Me | ping |

RustDesk sessions are relayed through the Pi, so the PC resource no longer needs any RustDesk ports as it did before.

> [!NOTE]
>
> The Twingate connector runs on the Pi, so all its traffic is sourced from the Pi's IP, and traffic specifically towards the services hosted on the Pi goes through the loopback interface.
>
> UFW allows all loopback traffic by default, so its rules don't apply to traffic within the Pi.
>
> To overcome this obstacle, I've configured the same ports in the Twingate console, and separated resources and ports by groups (admins / users).
>
> I'm facing one problem in the LAN: everyone can reach the admin services, but authentication like SSH keys or a login page blocks them from actually entering the service.
