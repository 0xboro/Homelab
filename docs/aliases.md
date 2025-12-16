# Bash Aliases

Bash aliases are a powerful way of making the developer's life easier by giving the ability to shortcut commands.

Here's a quick problem & solution situation for better understanding:

**Problem:**
The `rm` command deletes files instantly without being able to recover them and because of that I deleted an important file by mistake.
I always forget to add the `-i` flag to run interactive mode.

**Solution:**
Create an alias that makes `rm` equal to `rm -i`, making each `rm` interactive automatically.

>&#x1F6C8; **Note** 
>
>Interactive mode adds confirmation before executing desired command.
--- 

In order to configure aliases, we will use the following command:

`alias ____='Command'`

In our example, the command would be:
`alias rm='rm -i'`

It's important to mention, that aliases that are configured in the terminal are **volatile** and configured only for the running session, meaning they are removed after closing the terminal.

Don't be fooled, there is a way to make them permanent, using the shell's rc (run commands) file , which is the configuration startup file for each shell.

**There are 2 ways of configuring aliases permanently:**

>&#x1F6C8; **Note**
>
>To ease the example, I'll explain using `Bash` shell. If you're using a different shell, please check the shell's documentation:

1. **Per-user** - The `bashrc` file is **hidden** in the user's home directory (`~/.bashrc`)
    >In case you didn't know, the `.` at the start of a file name indicates that the file is hidden.

2. **System-wide** - The system-wide `bashrc` file is located at `/etc/bash.bashrc`

---

Since I'm using `Bash` as my shell and there are multiple users on the Pi, I'll configure my user's `bashrc` file (`~/.bashrc`).

Inside the bashrc file, we will have to find this specific if statement:
`if [ -x /usr/bin/dircolors ]; then` 

right under the following comment: `# enable color support of ls and also add handy aliases`

***(for me, those are at lines 75,76)***

There we could start and add our aliases, with the same syntax used in the regular terminal, the only difference now is that they are restart-proof.

## Bash Aliases in The Homelab
```
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

    >&#x1F6C8; **Note**
    >
    >Both `update` and `upgrade` run as root using the prefix `sudo`, and it's recommended to update before upgrading.

- **lah** - Lists the directory content with:
    - more details (`-l`)
    - shows hidden files (`-a`)
    - human-readable format (`-h`) - paired with `-l` 

        **In order to understand better, here are visual examples for each `ls` output:**

        ##### Regular `ls`:
        ![ls](/images/aliases/ls.png)
        
        ---
        
        ##### More details (Long-format):
        ![ls -l](/images/aliases/ls-l.png)
        
        ---
        
        ##### All files (Hidden files included):
        ![ls -a](/images/aliases/ls-a.png)
        
        ---
        
        ##### More details + human-readable format:
        ![ls -lh](/images/aliases/ls-lh.png)
        
        ---
        
        ##### All 3 flags combined:
        ![ls -lah](/images/aliases/ls-lah.png)

---

#### Docker Aliases

- **dcup** - Starts the services in the docker compose file and runs it in the background (`-d` flag for detached mode)

- **dcpull** - Pulls the latest images for the services in the docker compose file (to update, the services must restart)

- **dcdown** - Stops the services in the docker compose file

>&#x1F6C8; Note
>
> All docker aliases first `cd` into the `/services` directory, then run the commands using a subshell (commands inside `()`). 
>
>This keeps the user in the same directory as the commands were executed in.

---

![Bash Logo](/images/aliases/Gnu-bash-logo.png)

---