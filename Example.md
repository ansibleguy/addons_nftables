# NFTables Add-Ons Example

## Off-Screen

Installed NFTables using the [ansibleguy.infra_nftables](https://github.com/ansibleguy/infra_nftables) role!

## Config

### SRV01
```yaml
nftables_addons:
  enable:
    dns: true
    dns_v6: true
    iplist: true
    iplist_v6: true
    timer: true
    systemd: true
    cron: false

  appendix:
    ipv4: 'v4'
    ipv6: 'v6'

  config:
    iplists:
      tor_exit_nodes:
        urls: ['https://check.torproject.org/torbulkexitlist']
      spamhaus_edrop:
        urls: 'https://www.spamhaus.org/drop/edrop.txt'
        comment: ';'

    dns_records:
      site_github: ['github.com', 'codeload.github.com']
      repo_debian: 'deb.debian.org'
      ntp_pool: 'europe.pool.ntp.org'
      site_ansibleguy: 'ansibleguy.net'
```

### SRV02

```yaml
nftables_addons:
  enable:
    dns: true
    dns_v6: false
    iplist: true
    iplist_v6: false
    timer: true
    systemd: false
    cron: true

  config:
    iplists:
      tor_exit_nodes:
        urls: 'https://check.torproject.org/torbulkexitlist'

    dns_records:
      site_ansibleguy: 'ansibleguy.net'
```

----

## Result

### Files

```bash
guy@ansible:~# tree /etc/nftables.d/
> /etc/nftables.d/
> |-- addons
> |   |-- dns.json
> |   |-- dns.nft
> |   |-- iplist.json
> |   `-- iplist.nft
> `-- example.nft

guy@ansible:~# tree /usr/lib/nftables/
> /usr/lib/nftables/
> |-- dns.py
> |-- dns_resolver.py
> |-- iplist.py
> `-- util.py
```

#### SRV01 (systemd)

```bash
guy@ansible:~# cat /etc/systemd/system/ansibleguy.addons_nftables-dns.service 
> # Ansible managed: Do NOT edit this file manually!
> # ansibleguy.addons_nftables
> 
> [Unit]
> Description=Service to process NFTables Add-On 'dns'
> Documentation=https://github.com/ansibleguy/addons_nftables
> Requires=nftables.service
> 
> [Service]
> Type=simple
> User=root
> Group=root
> ExecStart=python3 /usr/lib/nftables/dns.py
> StandardOutput=journal
> StandardError=journal
> SyslogIdentifier=nftables_addon_dns

guy@ansible:~# cat /etc/systemd/system/ansibleguy.addons_nftables-dns.timer 
> # Ansible managed: Do NOT edit this file manually!
> # ansibleguy.addons_nftables
> 
> [Unit]
> Description=Timer to process NFTables Add-On 'dns'
> 
> [Timer]
> OnCalendar=*:0/15
> Persistent=false
> WakeSystem=false
> 
> [Install]
> WantedBy=multi-user.target

guy@ansible:~# cat /etc/systemd/system/ansibleguy.addons_nftables-iplist.service 
> # Ansible managed: Do NOT edit this file manually!
> # ansibleguy.addons_nftables
> 
> [Unit]
> Description=Service to process NFTables Add-On 'iplist'
> Documentation=https://github.com/ansibleguy/addons_nftables
> Requires=nftables.service
> 
> [Service]
> Type=simple
> User=root
> Group=root
> ExecStart=python3 /usr/lib/nftables/iplist.py
> StandardOutput=journal
> StandardError=journal
> SyslogIdentifier=nftables_addon_iplist

guy@ansible:~# cat /etc/systemd/system/ansibleguy.addons_nftables-iplist.timer   
> # Ansible managed: Do NOT edit this file manually!
> # ansibleguy.addons_nftables
> 
> [Unit]
> Description=Timer to process NFTables Add-On 'iplist'
> 
> [Timer]
> OnCalendar=*-*-* 00,12:00:00
> Persistent=false
> WakeSystem=false
> 
> [Install]
> WantedBy=multi-user.target
```

#### SRV02 (crontab)

```bash
guy@ansible:~# crontab -e
> #Ansible: nftables_addon_dns
> */15 * * * * python3 /usr/lib/nftables/dns.py
> #Ansible: nftables_addon_iplist
> 0 0,12 * * * python3 /usr/lib/nftables/iplist.py
```

### Running

#### SRV01 (systemd)

```bash
guy@ansible:~# systemctl status ansibleguy.addons_nftables-dns.service --no-pager --full
> * ansibleguy.addons_nftables-dns.service - Service to process NFTables Add-On 'dns'
>      Loaded: loaded (/etc/systemd/system/ansibleguy.addons_nftables-dns.service; static)
>      Active: inactive (dead)
> TriggeredBy: * ansibleguy.addons_nftables-dns.timer
>        Docs: https://github.com/ansibleguy/addons_nftables

guy@ansible:~# systemctl status ansibleguy.addons_nftables-dns.timer --no-pager --full
> * ansibleguy.addons_nftables-dns.timer - Timer to process NFTables Add-On 'dns'
>      Loaded: loaded (/etc/systemd/system/ansibleguy.addons_nftables-dns.timer; enabled; vendor preset: enabled)
>      Active: active (waiting) since Sat 2023-01-21 18:47:01 UTC; 6min ago
>     Trigger: Sat 2023-01-21 19:00:00 UTC; 6min left
>    Triggers: * ansibleguy.addons_nftables-dns.service
> 
> Jan 21 18:47:01 test-ag-nftablesaddons-systemd systemd[1]: Started Timer to process NFTables Add-On 'dns'.

guy@ansible:~# systemctl status ansibleguy.addons_nftables-iplist.service --no-pager --full
> * ansibleguy.addons_nftables-iplist.service - Service to process NFTables Add-On 'iplist'
>      Loaded: loaded (/etc/systemd/system/ansibleguy.addons_nftables-iplist.service; static)
>      Active: inactive (dead)
> TriggeredBy: * ansibleguy.addons_nftables-iplist.timer
>        Docs: https://github.com/ansibleguy/addons_nftables

guy@ansible:~#  systemctl status ansibleguy.addons_nftables-iplist.timer --no-pager --full
> * ansibleguy.addons_nftables-iplist.timer - Timer to process NFTables Add-On 'iplist'
>      Loaded: loaded (/etc/systemd/system/ansibleguy.addons_nftables-iplist.timer; enabled; vendor preset: enabled)
>      Active: active (waiting) since Sat 2023-01-21 18:47:30 UTC; 7min ago
>     Trigger: Sun 2023-01-22 00:00:00 UTC; 5h 5min left
>    Triggers: * ansibleguy.addons_nftables-iplist.service
> 
> Jan 21 18:47:30 test-ag-nftablesaddons-systemd systemd[1]: Started Timer to process NFTables Add-On 'iplist'.
```

### Config

```bash
guy@ansible:~# cat /etc/nftables.conf 
> #!/usr/sbin/nft -f
> 
> # Ansible managed: Do NOT edit this file manually!
> 
> flush ruleset
> 
> 
> include "/etc/nftables.d/*.nft"
> # BEGIN ANSIBLE MANAGED BLOCK ansibleguy.addons_nftables
> include "/etc/nftables.d/addons/*.nft"
> # END ANSIBLE MANAGED BLOCK ansibleguy.addons_nftables
```

#### SRV01

```bash
guy@ansible:~# cat /etc/nftables.d/addons/dns.json 
> {"dns": {"site_github": ["github.com", "codeload.github.com"], "repo_debian": "deb.debian.org", "ntp_pool": "europe.pool.ntp.org", "site_ansibleguy": "ansibleguy.net"}}

guy@ansible:~# cat /etc/nftables.d/addons/iplist.json 
> {"iplist": {"tor_exit_nodes": {"urls": ["https://check.torproject.org/torbulkexitlist"]}, "spamhaus_edrop": {"urls": "https://www.spamhaus.org/drop/edrop.txt", "comment": ";"}}}

guy@ansible:~# cat /etc/nftables.d/addons/iplist.nft 
> # Auto-Generated config - DO NOT EDIT MANUALLY!
> 
> define tor_exit_nodes_v4 = { 102.130.113.9, 102.130.127.117, 102.130.127.238, ..., 95.216.107.148, 95.217.186.208 }
> define tor_exit_nodes_v6 = { ::/0 }
> define spamhaus_edrop_v4 = { 109.206.243.0/24, 119.227.224.0/19, 120.128.128.0/17, ..., 95.161.128.0/24, 95.214.24.0/24 }
> define spamhaus_edrop_v6 = { ::/0 }

guy@ansible:~# cat /etc/nftables.d/addons/dns.nft    
> # Auto-Generated config - DO NOT EDIT MANUALLY!
> 
> define site_github_v4 = { 140.82.121.3, 140.82.121.10 }
> define site_github_v6 = { ::/0 }
> define repo_debian_v4 = { 151.101.86.132 }
> define repo_debian_v6 = { 2a04:4e42:14::644 }
> define ntp_pool_v4 = { 158.43.128.33, 178.62.250.107, 194.58.207.20, 37.252.127.156 }
> define ntp_pool_v6 = { ::/0 }
> define site_ansibleguy_v4 = { 135.181.170.217 }
> define site_ansibleguy_v6 = { ::/0 }
```

#### SRV02

```bash
guy@ansible:~# cat /etc/nftables.d/addons/dns.json 
> {"dns": {"site_ansibleguy": "ansibleguy.net"}}

guy@ansible:~# cat /etc/nftables.d/addons/iplist.json 
> {"iplist": {"tor_exit_nodes": {"urls": "https://check.torproject.org/torbulkexitlist"}}}

guy@ansible:~# cat /etc/nftables.d/addons/iplist.nft 
> # Auto-Generated config - DO NOT EDIT MANUALLY!
> 
> define tor_exit_nodes = { 102.130.113.9, 102.130.127.117, 102.130.127.238, ..., 95.216.107.148, 95.217.186.208 }

guy@ansible:~# cat /etc/nftables.d/addons/dns.nft    
> # Auto-Generated config - DO NOT EDIT MANUALLY!
> 
> define site_ansibleguy = { 135.181.170.217 }
```