<a href="https://netfilter.org/projects/nftables/index.html">
<img src="https://netfilter.org/images/netfilter-logo3.png" alt="NFTables logo" width="400"/>
</a>

# Ansible Role - NFTables Add-Ons

Role to deploy Addons for NFTables on Linux servers.

# REPLACE: GALAXY_ID & ROLE

[![Molecule Test Status](https://badges.ansibleguy.net/addons_nftables.molecule.svg)](https://github.com/ansibleguy/_meta_cicd/blob/latest/templates/usr/local/bin/cicd/molecule.sh.j2)
[![YamlLint Test Status](https://badges.ansibleguy.net/addons_nftables.yamllint.svg)](https://github.com/ansibleguy/_meta_cicd/blob/latest/templates/usr/local/bin/cicd/yamllint.sh.j2)
[![Ansible-Lint Test Status](https://badges.ansibleguy.net/addons_nftables.ansiblelint.svg)](https://github.com/ansibleguy/_meta_cicd/blob/latest/templates/usr/local/bin/cicd/ansiblelint.sh.j2)
[![Ansible Galaxy](https://img.shields.io/ansible/role/GALAXY_ID)](https://galaxy.ansible.com/ansibleguy/ROLE)
[![Ansible Galaxy Downloads](https://img.shields.io/badge/dynamic/json?color=blueviolet&label=Galaxy%20Downloads&query=%24.download_count&url=https%3A%2F%2Fgalaxy.ansible.com%2Fapi%2Fv1%2Froles%2FGALAXY_ID%2F%3Fformat%3Djson)](https://galaxy.ansible.com/ansibleguy/addons_nftables)


**Tested:**
* Debian 11

## Install

```bash
ansible-galaxy install ansibleguy.addons_nftables

# or to custom role-path
ansible-galaxy install ansibleguy.addons_nftables --roles-path ./roles
```

## Functionality

* **Package installation**
  * 


* **Configuration**
  * 


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


## Usage

You can 

### Config

Define the config as needed:

```yaml
app:

```

You might want to use 'ansible-vault' to encrypt your passwords:
```bash
ansible-vault encrypt_string
```

### Execution

Run the playbook:
```bash
ansible-playbook -K -D -i inventory/hosts.yml playbook.yml
```

There are also some useful **tags** available:
* 
*

To debug errors - you can set the 'debug' variable at runtime:
```bash
ansible-playbook -K -D -i inventory/hosts.yml playbook.yml -e debug=yes
```
