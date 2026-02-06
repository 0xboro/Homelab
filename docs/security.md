# Homelab's Security & Hardening

## Zero Trust Network Access
Using [Twingate](/docs/twingate.md), my home network is completely separated from the internet.

## Secure Shell (SSH) 
I use SSH as my remote management tool for the Raspberry Pi.

### SSH Hardening
I hardened SSH beyond its default configuration with ed25519 key-based authentication instead of the standard password-based authentication to eliminate the risk of a brute-force attack, and I disabled Root login to prevent direct administrative access.

> [!CAUTION]
>
> Before disabling password authentication, make sure the key authentication works using the command:
>
> ```bash
> ssh -i <private_key_file> <user>@<hostname / IP>
> ```

> [!TIP]
>
> Always keep a backup session open when changing SSH settings to avoid lockouts.
---

**/etc/ssh/sshd_config**

```diff
- #PubkeyAuthentication yes
+ PubkeyAuthentication yes

- PasswordAuthentication yes
+ PasswordAuthentication no

- PermitRootLogin prohibit-password
+ PermitRootLogin no
```

After the configuration is complete, restart the SSH service:

```bash
sudo systemctl restart ssh
```

## Firewall
I chose Uncomplicated Firewall (UFW) since I only need to allow certain ports and UFW is the simplest firewall that does the job.

### UFW Configuration
Firstly, I've disabled IPv6 (not used in my homelab):

**/etc/default/ufw**
```diff
- IPV6=yes 
+ IPV6=no
```

Then I've configured the firewall using a whitelist approach, explicitly allowing specific services.

#### Services:
> SSH (Secure Shell) - Port 22/TCP
>
> Uptime-Kuma - Port 3001/TCP
>
> WoL (Wake on LAN) Website - Port 8080/TCP
>
> Portainer - Port 9443/TCP
>
> RustDesk - Ports 21115/TCP, 21116/TCP, 21116/UDP, 21117/TCP 
>
> Glances - Port 61208/TCP

#### Firewall Configuration:
```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp comment "Allow SSH"
sudo ufw allow 3001/tcp comment "Allow Uptime-Kuma"
sudo ufw allow 8080/tcp comment "Allow WoL"
sudo ufw allow 9443/tcp comment "Allow Portainer HTTPS"
sudo ufw allow 21115:21117/tcp comment "Allow RustDesk"
sudo ufw allow 21116/udp comment "Allow RustDesk"
sudo ufw allow 61208/tcp comment "Allow Glances"
sudo ufw enable
```

## Self-Hosted Remote Desktop Service
Using [RustDesk](/docs/rustdesk.md)'s self-hosted relay server in the homelab, I have complete control over my remote desktop traffic.