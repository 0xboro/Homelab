# RustDesk

RustDesk is a self-hosted remote desktop solution, which provides more security over my remote sessions by relaying the traffic through a locally installed server.

**Installation:** [official guide](https://rustdesk.com/docs/en/self-host/rustdesk-server-oss/install/) (I used Method 3: `.deb` packages from the [RustDesk server releases](https://github.com/rustdesk/rustdesk-server/releases)).

## RustDesk Setup

RustDesk is set up for 2 scenarios:
1. When I'm home, and I remote into one of my devices within the local network - which then the connection is direct (peer-to-peer).

2. When I'm away, and I use RustDesk over my Twingate tunnel, which then relays the traffic through the Raspberry Pi instead of RustDesk's public servers.

> [!NOTE]
>
> Twingate provides access to LAN resources but doesn't place the client directly in the LAN, so direct peer-to-peer connection in RustDesk is unavailable.

## RustDesk Configuration

RustDesk runs 2 services:

1. `hbbr` - RustDesk relay server, that acts as the bridge if peer-to-peer connection fails.

2. `hbbs` - RustDesk ID server, which uses the rendezvous protocol to help clients find each other over the network.

## Running as a systemd Service

Originally, RustDesk ran in Docker. I moved it to a systemd service so the core of my homelab, the remote-access chain (Twingate, RustDesk and WoL), keeps working independently of any container runtime.
This follows the lesson from the [Twingate incident](/docs/twingate.md#why-twingate-runs-as-systemd-service).

By copying the server's existing keys from the Docker volume, I kept every trusted client-server relationship uninterrupted, making the transition to systemd a seamless experience.