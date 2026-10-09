# RustDesk

RustDesk is a self-hosted remote desktop solution, which provides more security over my remote sessions by relaying the traffic through a locally installed server.

## RustDesk Installation
For installation and initial setup, please refer to the [official RustDesk documentation](https://rustdesk.com/docs/en/).

## RustDesk Setup
RustDesk is set up for 2 scenarios:
1. When I'm home, and I remote into one of my devices within the local network - which then the connection is direct (peer-to-peer).

2. When I'm away, and I use RustDesk over my Twingate tunnel, which then relays the traffic through the Raspberry Pi instead of RustDesk's public servers.

> [!NOTE]
>
> Twingate provides access to LAN resources but doesn't place the client directly in the LAN, so direct peer-to-peer connection in RustDesk is unavailable.

## RustDesk Configuration

RustDesk runs 2 services:

1. hbbr - RustDesk relay server, that acts as the bridge if peer-to-peer connection fails.

2. hbbs - RustDesk ID server, which uses the rendezvous protocol to help clients find each other over the network.

### RustDesk in Docker Compose
```yaml
services:
  hbbs:
    container_name: hbbs
    image: rustdesk/rustdesk-server:latest
    command: hbbs
    volumes:
      - ./data:/root
    network_mode: "host"
    depends_on:
      - hbbr
    restart: unless-stopped

  hbbr:
    container_name: hbbr
    image: rustdesk/rustdesk-server:latest
    command: hbbr
    volumes:
      - ./data:/root
    network_mode: "host"
    restart: unless-stopped
```
