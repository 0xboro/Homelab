# Homelab's Security & Hardening

## Zero Trust Network Access
Using [Twingate](/docs/twingate.md), my home network is completely separated from the internet.

## Secure Shell (SSH)
SSH is a cryptographic network protocol that enables users to securely connect to a device remotely.

### SSH Installation
To install SSH, use the following command:

On the server (Raspberry Pi):

```bash
sudo apt install openssh-server
```

SSH client is pre-installed on modern operating systems.

### SSH Configuration & Hardening

- **Generate SSH (ed25519) key on the client's machine**

    Windows & Linux:
    ```bash
    ssh-keygen -t ed25519 -C "<user>@<hostname / IP>"
    ```

- **Copy the SSH key**

    Windows:
    ```powershell
    type $env:USERPROFILE\.ssh\id_ed25519.pub
    ```
    Linux:
    ```bash
    cat /home/<user>/.ssh/id_ed25519.pub
    ```

- **Configurations on the Pi**

    SSH directory creation and permissions setup: (skip if already configured)
    ```bash
    mkdir -p /home/<user>/.ssh
    touch /home/<user>/.ssh/authorized_keys
    chmod 700 /home/<user>/.ssh
    chmod 600 /home/<user>/.ssh/authorized_keys
    ```
    Copy the key into `authorized_keys`:
    ```bash
    echo "<public_key>" >> /home/<user>/.ssh/authorized_keys
    ```

After the key is successfully added to the `authorized_keys` file, we can disable the password authentication and only use key authentication.

> [!CAUTION]
>
> Before proceeding, make sure the key authentication works before disabling password authentication using the command:
>
> ```bash
> ssh -i <private_key_file> <user>@<hostname / IP>
> ```

- **Enter the SSH daemon configuration file**
    ```bash
    sudo nano /etc/ssh/sshd_config
    ```

    **Change the following settings**
    ```diff
    - #PubkeyAuthentication yes
    + PubkeyAuthentication yes

    - PasswordAuthentication yes
    + PasswordAuthentication no
    ```

    Another recommended change in the file is removing the SSH login as Root option:
    ```diff
    - PermitRootLogin prohibit-password
    + PermitRootLogin no
    ```

After the configuration is complete, enable the SSH on startup and run it:

```bash
sudo systemctl enable --now ssh
```
> [!NOTE]
>
> The Configuration process happens before the SSH is running. If your SSH is already running, after configuration, run this command instead:
>
> ```bash
> sudo systemctl restart ssh
> ```

## Firewall
I chose Uncomplicated Firewall (UFW) since I only need to allow certain ports and UFW is the simplest firewall that does the job.

### UFW Installation
To install UFW, use the following command:

```bash
sudo apt install ufw
```

### UFW Configuration
First, I've disabled IPv6 since it's not used in my homelab

**Enter the UFW configuration file**
```bash
sudo nano /etc/default/ufw
```
**Change the following settings**
```diff
- IPV6=yes 
+ IPV6=no
```

After that, we can configure our rules.
My firewall would use a whitelist approach, meaning the content of the firewall is permitted, and the rest is prohibited (denied in firewall's terms).

Here are the services configured in my homelab and their ports:
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

Hence the Firewall rules configuration:
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
```

> [!NOTE]
>
> The rule `sudo ufw default deny incoming` denies all incoming traffic, changing the firewall's approach to whitelist. 
>
> The rule `sudo ufw default allow outgoing` allows all outgoing traffic.
>
> Important to mention, both settings are the UFW's default, I've configured them again for documentation purposes.


After everything is setup, we have to enable the firewall:

```bash
sudo ufw enable
```

## Self-Hosted Remote Desktop Service
Using [RustDesk](/docs/rustdesk.md)'s self-hosted relay server in the homelab, I have complete control over my remote desktop traffic.