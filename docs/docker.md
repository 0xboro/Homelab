# Docker

<p align="center">
    <img src="../images/Docker/Docker_Logo.png" width="500">
</p>

Docker is used in my lab to run the following services:

- [Glances](/docs/glances.md)
- [Portainer](/docs/portainer.md)
- [RustDesk](/docs/rustdesk.md)
- [Uptime Kuma](/docs/uptime-kuma.md)

Those services run on a single docker compose file, shown [here](/configs/docker-compose.yml).

I chose Docker to run those services specifically since Docker is a very convenient and practical way to run multiple services.
Combined with Portainer, managing containers becomes even easier than it already is.

## Docker Installation
For installation and initial setup, please refer to the [official Docker documentations](https://docs.docker.com/engine/install/).