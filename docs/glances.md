# Glances

<p align="center">
    <img src="../images/Glances/GlancesLogo.png" width="300">
</p>

I added Glances to have a real-time monitor of my Raspberry Pi's performance - essential for my system that runs 24/7.

## Glances Installation
For installation and initial setup, please refer to the [official Glances GitHub repository](https://github.com/nicolargo/glances).

## Glances Configuration
```yaml
services:
  glances:
    image: nicolargo/glances:latest
    container_name: glances
    restart: unless-stopped
    pid: host
    privileged: true
    network_mode: host
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
    environment:
      - GLANCES_OPT=-w
```
Full Docker Compose: [docker-compose.yml](/configs/docker-compose.yml).

## Glances Interface
![Glances Interface](/images/Glances/GlancesOverview.png)