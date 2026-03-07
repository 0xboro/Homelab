# Uptime Kuma

<p align="center">
    <img src="../images/UptimeKuma/UptimeKuma_Logo.png" width="300">
</p>
I chose Uptime Kuma to monitor both my connectivity and services status.

## Uptime Kuma Installation
For installation and initial setup, please refer to the [official Uptime Kuma GitHub repository](https://github.com/louislam/uptime-kuma).

## Uptime Kuma Overview
![Uptime Kuma Overview](/images/UptimeKuma/UptimeKumaOverview.png)

## Monitor Configuration
I have 2 types of monitors - monitors for my services, and for my general connectivity.

### Services
| Service | Type | Interval (seconds) | Explanation |
|---------|------|--------------------|-------------|
| Glances    | HTTP     | 60     | Glances' web UI  |
| hbbr | TCP | 60 | RustDesk Relay (port 21117) |
| hbbs | TCP | 60 | RustDesk ID server (port 21116) |
| Portainer | HTTPS | 60 | Portainer's web UI |
| Twingate | HTTPS | 120 | Twingate home network connection |

### General Connectivity
- Internet 1 & 2 - Redundant ping to 2 public DNS servers (8.8.8.8 & 1.1.1.1) every 120 seconds to distinguish between an outage of my internet connection and a single provider. 

- Pi - Ping to the Raspberry Pi's localhost (127.0.0.1) every 60 seconds to separate Pi-level problems from service-level issues.

### Uptime Kuma in Docker Compose

```yaml
services:
  uptime-kuma:
    image: louislam/uptime-kuma:latest
    container_name: uptime-kuma
    volumes:
      - uptime-kuma-data:/app/data
    ports:
      - "3001:3001"
    restart: unless-stopped
volumes:
  uptime-kuma-data:
```
Full Docker Compose: [docker-compose.yml](/configs/docker-compose.yml).