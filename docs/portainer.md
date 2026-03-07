# Portainer

<p align="center">
    <img src="../images/Portainer/Portainerlogo.png" width="600">
</p>

I use Portainer since it provides a web UI for Docker container management.

## Portainer Installation
For installation and initial setup, please refer to the [official Portainer documentation](https://docs.portainer.io/start/install-ce).


## My Containers
![Containers](/images/Portainer/Containers.png)


## Portainer Configuration

```yaml
services:
  portainer:
    image: portainer/portainer-ce:latest
    container_name: portainer
    restart: unless-stopped
    ports:
      - "9443:9443"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - portainer-data:/data
volumes:
  portainer-data:
```
Full Docker Compose: [docker-compose.yml](/configs/docker-compose.yml).