# Overview

The main reason I built this homelab was to enable secure remote access to my home network.

## 3 Main Problems I Encountered 

### Problem #1

Imagine this scenario:

You're at work, and you want to remote into your desktop PC, but can't because it's turned off, so you ask a family member to turn the PC on. Sounds simple, right? But what happens when there is no one home?

### Problem #2

Even if the PC is on, using remote desktop over the internet may not be the most secure thing, especially when it's going through public servers.

### Problem #3

In order to use self-hosted remote desktop solution, I'll have to be in my home LAN, and traditional VPN's use port forwarding, forcing me to expose internal services to the internet.

## Solutions to The Problems

### Problem #1 Solution
Configured [Wake on LAN](/docs/wol.md) to remotely turn on the pc.
 
### Problem #2 Solution
Configured [RustDesk](/docs/rustdesk.md) relay / p2p server to have a self-hosted remote desktop service. 

### Problem #3 Solution
Configured [Twingate](/docs/twingate.md) for secure zero-trust access to my network.

>&#x1F6C8; Note
>
> 1. It's important to mention that Twingate is the root of my setup, without it, I could not turn the PC remotely nor use my self-hosted remote desktop service.
> 
> 2. Twingate + RustDesk combination was configured with [NetworkChuck](https://www.youtube.com/@NetworkChuck)'s tutorial.
>       - [Twingate Tutorial](https://youtu.be/1lZ3FQSv-wI?si=8gdykuX-ScusZnPG)
>       - [RustDesk Tutorial](https://youtu.be/EXL8mMUXs88?si=RxT-H71s68EVWPed)

---

## Additional Services

After solving the 3 main problems, I decided to add more services for convenience.

All of the following services were configured on [Docker](/docs/docker.md) - a centralized container management solution:
 
- Configured [Portainer](/docs/portainer.md) for easier Docker management

- Configured [Uptime-kuma](/docs/uptime-kuma.md) to monitor services on the system

- Configured [Glances](/docs/glances.md) to monitor the system's health

>&#x1F6C8; Note
>
>RustDesk also runs as a Docker container.


## Lessons Learned
The setup of this homelab taught me many things.
I made several mistakes along the way, especially since it's my first time using a Raspberry Pi 5. But that's a part of learning :)

From the manual assembly of the Raspberry Pi 5 to the configuration of everything, I can honestly say that it was 100% worth it, both for my learning, and my overall quality of life.

---


***This repository will update as my homelab setup evolves.***
