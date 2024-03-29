<a href="https://netfilter.org/projects/nftables/index.html">
<img src="https://netfilter.org/images/netfilter-logo3.png" alt="NFTables logo" width="400"/>
</a>

# Ansible Role - NFTables Add-Ons

Role to deploy Addons for NFTables on Linux servers.

<a href='https://ko-fi.com/ansible0guy' target='_blank'><img height='35' style='border:0px;height:46px;' src='https://az743702.vo.msecnd.net/cdn/kofi3.png?v=0' border='0' alt='Buy me a coffee' />

[![Molecule Test Status](https://badges.ansibleguy.net/addons_nftables.molecule.svg)](https://github.com/ansibleguy/_meta_cicd/blob/latest/templates/usr/local/bin/cicd/molecule.sh.j2)
[![YamlLint Test Status](https://badges.ansibleguy.net/addons_nftables.yamllint.svg)](https://github.com/ansibleguy/_meta_cicd/blob/latest/templates/usr/local/bin/cicd/yamllint.sh.j2)
[![PyLint Test Status](https://badges.ansibleguy.net/addons_nftables.pylint.svg)](https://github.com/ansibleguy/_meta_cicd/blob/latest/templates/usr/local/bin/cicd/pylint.sh.j2)
[![Ansible-Lint Test Status](https://badges.ansibleguy.net/addons_nftables.ansiblelint.svg)](https://github.com/ansibleguy/_meta_cicd/blob/latest/templates/usr/local/bin/cicd/ansiblelint.sh.j2)
[![Ansible Galaxy](https://badges.ansibleguy.net/galaxy.badge.svg)](https://galaxy.ansible.com/ui/standalone/roles/ansibleguy/addons_nftables)

Molecule Logs: [Short](https://badges.ansibleguy.net/log/molecule_addons_nftables_test_short.log), [Full](https://badges.ansibleguy.net/log/molecule_addons_nftables_test.log)

**Tested:**
* Debian 11
* Debian 12

## Install

```bash
# latest
ansible-galaxy role install git+https://github.com/ansibleguy/addons_nftables

ä from galaxy
ansible-galaxy install ansibleguy.addons_nftables

# or to custom role-path
ansible-galaxy install ansibleguy.addons_nftables --roles-path ./roles
```

## Documentation

* NFTables: [Wiki](https://wiki.nftables.org/wiki-nftables/index.php/Quick_reference-nftables_in_10_minutes)
* Check out the [Example](https://github.com/ansibleguy/addons_nftables/blob/stable/Example.md)!
* Ansible-manage all of NFTables: [ansibleguy.infra_nftables](https://github.com/ansibleguy/infra_nftables/blob/main/README.md)


## Functionality

* **Configuration**

  * **Default config**:
    * Systemd Timer to run the addons
    * Logging to Syslog
    * Appendix for IPv6 variables: '_v6'
      * Per example: variable 'repo_debian' => 'repo_debian_v6'
    * Timers
      * DNS => updated every 15 minutes
      * IP-List => updated twice a day
    * Systemd
      * Syslog ID: 'nftables_addon_{ addon }'
      * Service/Timer Prefix: 'ansibleguy.addons_nftables-'

  * **Default opt-ins**:
    * Timer to automatically update variables
    * Systemd Timer
    * Adding include into '/etc/nftables.conf'


  * **Default opt-outs**:
    * **Add-Ons**
      * DNS
        * DNS IPv6 processing
      * IP-Lists
        * IP-List IPv6 processing
    * Cron-Job Timer

## Info

* **Note:** this role currently only supports debian-based systems


* **Note:** Most of the role's functionality can be opted in or out.

  For all available options - see the default-config located in the main defaults-file!


* **Warning:** Not every setting/variable you provide will be checked for validity. Bad config might break the role!


* **Note:** **Every defined variable will be created** as a missing one might break your config!

  If a DNS-record cannot be resolved or no entry is returned - a fallback value (_IPv4: 0.0.0.0, IPv6: ::_) will be set.


## Usage

You can manage the NFTables base-config using the [ansibleguy.infra_nftables](https://github.com/ansibleguy/infra_nftables) role!

### Config

You can find a more detailed example here: [Example](https://github.com/ansibleguy/addons_nftables/blob/stable/Example.md)!

Define the config as needed:

```yaml
nftables_addons:
  enable:
    dns: true  # enable DNS-addon
    dns_v6: true  # enable IPv6-processing of DNS-addon
    iplist: true  # enable IPList-addon
    iplist_v6: true  # enable IPv6-processing of IPList-addon
    # timer: true  # you could disable the timer-management if you want to do it yourself
    # systemd: true  # update addons using a systemd-timer
    # cron: false  # update addons using a cron-job
    # include: true  # disable auto-include of addons in /etc/nftables.conf

  config:
    iplists:
      iplist_tor_exit_nodes:  # var-name
        urls: ['https://check.torproject.org/torbulkexitlist']
        separator: "\n"
        comment: '#'
    dns_records:
      ntp_servers: ['0.europe.pool.ntp.org', '1.europe.pool.ntp.org']
      repo_debian: ['deb.debian.org', 'debian.map.fastlydns.net', 'security.debian.org']

  ext: 'nft'  # extension used by nftables config-files
  path:
    base:
      config: '/etc/nftables.conf'
      dir: '/etc/nftables.d'
    addon:
      dir: '/etc/nftables.d/addons'

  timer:
    systemd:
      dns: '*:0/15'  # update every 15min
      iplist: '*-*-* 00,12:00:00'  # update twice a day

    # cron:
    #   dns:  # every 15min
    #     minute: '*/15'
    #   iplist:  # twice a day
    #     minute: '0'
    #     hour: '0,12'

```

### Execution

Run the playbook:
```bash
ansible-playbook -K -D -i inventory/hosts.yml playbook.yml
```

There are also some useful **tags** available:
* dns
* iplist
* config (_only update addon-config_)

To debug errors - you can set the 'debug' variable at runtime:
```bash
ansible-playbook -K -D -i inventory/hosts.yml playbook.yml -e debug=yes
```
