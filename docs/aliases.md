# Bash Aliases

<p align="center">
    <img src="../images/aliases/Gnu-bash-logo.png" width="400">
</p>

I configured my user's bashrc file (~/.bashrc) since my brother and I administrate the Raspberry Pi on separate accounts.

## Bash Aliases in My Homelab

```bash
#general aliases
    alias update='sudo apt update'
    alias upgrade='sudo apt upgrade -y'
    alias lah='ls -lah'

#docker aliases
    alias dcup='(cd /services && docker compose up -d)'
    alias dcpull='(cd /services && docker compose pull)'
    alias dcdown='(cd /services && docker compose down)'
```

### Explanation of Each Alias
#### General Aliases

- **update** - Updates the system's package list

- **upgrade** - Upgrades all available packages and automatically confirms (`-y` flag)

- **lah** - Lists the directory content with more details (`-l`), hidden files (`-a`), and in human-readable format (`-h`)


#### Docker Aliases

- **dcup** - Starts the services in detached mode (`-d`) to run in the background

- **dcpull** - Pulls latest images of used services (requires restart to apply updates)

- **dcdown** - Stops the services

> [!NOTE]
>
> My Docker aliases use subshells `()` to keep me in the original directory after execution.