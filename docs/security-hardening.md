# Homelab's Security & Hardening

## Zero Trust Network Access

Using [Twingate](/docs/twingate.md), my home network has no ports exposed to the internet.

## Secure Shell (SSH) 

I use SSH as my remote management tool for the Raspberry Pi.

### SSH Hardening

I hardened SSH beyond its default configuration with `ed25519` key-based authentication instead of the standard password-based authentication to eliminate the risk of a brute-force attack, and I disabled root login to prevent direct administrative access.

My SSH private key is protected by a passphrase and loaded via `ssh-agent`, and sudo requires a password.

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

**`/etc/ssh/sshd_config`**

```diff
- #PubkeyAuthentication yes
+ PubkeyAuthentication yes

- PasswordAuthentication yes
+ PasswordAuthentication no

- PermitRootLogin prohibit-password
+ PermitRootLogin no
```

After the configuration is complete:

```bash
# Ensure sshd file syntax validity
sudo sshd -t

# Restart ssh service
sudo systemctl restart ssh
```

## Firewall

I chose Uncomplicated Firewall (UFW) since I only need to allow certain ports and UFW is the simplest firewall that does the job.

### UFW Configuration

I've configured the firewall using a whitelist approach, explicitly allowing specific services.

#### Services

| Service | Port(s) | Allowed source |
| :--- | :--- | :--- |
| SSH | 22/TCP | LAN
| WoL | 8080/TCP | LAN
| RustDesk | 21115-21117/TCP, 21116/UDP | LAN

#### Firewall Configuration

The firewall rules are managed with GitOps and automatically applied by Ansible (`ansible-pull`).
IPv4 rules are generated from a template, while IPv6 uses a rule file with no rules, so IPv6 traffic hits the default deny policy.

## Self-Hosted Remote Desktop Service

Using [RustDesk](/docs/rustdesk.md)'s self-hosted relay server in the homelab, I have complete control over my remote desktop traffic.
