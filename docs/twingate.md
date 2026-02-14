# Twingate

At the beginning, Twingate ran on Docker, and one time I was working remotely on my Raspberry Pi, and I wanted to restart the Docker compose.

Up until now, everything sounds normal, the problem was, that instead of just using the command:

```bash
docker compose up -d
```
to restart it, I firstly turned it off, then tried to turn it back on with the commands:

```bash
docker compose down
docker compose up -d
```
The problem is, because Twingate ran on Docker, the second I shut down the Docker compose file, I couldn't turn it back on :)

Since then, Twingate is running as a systemd service.

---

All jokes aside, I chose Twingate as a part of NetworkChuck's tutorial (link in [overview](overview.md)) for secure remote access to my network.

Twingate is a great zero-trust platform, combining a secure split-tunnel to my home network, without exposing any internal services to the internet, like standard port forwarding would've done.

## Twingate Configuration
For installation and initial setup, please refer to the [official Twingate documentations](https://www.twingate.com/docs/quick-start).

**systemd file**

```bash
# /usr/lib/systemd/system/twingate-connector.service
[Unit]
Description=Twingate Connector service
After=network.target
StartLimitIntervalSec=0

[Service]
Restart=always
RestartSec=10
Environment=TWINGATE_API_ENDPOINT=/var/run/twingate/connector.sock
EnvironmentFile=<REDACTED>
ExecStart=/usr/bin/twingate-connector --systemd-watchdog
DynamicUser=yes
ProtectSystem=full
ProtectHome=yes
ProtectKernelLogs=yes
ProtectKernelModules=yes
ProtectHostname=yes
ProtectClock=yes
ProtectKernelTunables=yes
RestrictAddressFamilies=AF_INET AF_INET6 AF_UNIX AF_NETLINK
RestrictNamespaces=true
RestrictSUIDSGID=yes
SystemCallArchitectures=native
SystemCallFilter=~@clock @debug @module @mount @raw-io @reboot @privileged @resources @cpu-emulation @obsolete
LockPersonality=yes
MemoryDenyWriteExecute=yes
RestrictRealtime=yes
CapabilityBoundingSet=
DevicePolicy=closed
PrivateUsers=yes
PrivateTmp=yes
PrivateDevices=yes
NoNewPrivileges=yes
UMask=0777
RuntimeDirectory=twingate
WatchdogSec=30s

[Install]
WantedBy=multi-user.target
```

**Environment File**
```bash
TWINGATE_NETWORK=Network_Name
TWINGATE_ACCESS_TOKEN=Access_Token
TWINGATE_REFRESH_TOKEN=Refresh_Token
TWINGATE_LOG_ANALYTICS=v2 #Enhanced logging - remove for standard
```
> Environment file is also shown [here](/configs/connector.conf.example) 