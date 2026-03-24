# Ansible Collection - my_own_namespace.yandex_cloud_elk

# Yandex Cloud ELK Collection

## Description

This collection provides modules and roles for managing files on remote hosts.

## Modules
- `my_own_module`: Creates a text file with specified content on a remote host.

## Roles
- `my_own_role`: A role that uses `my_own_module` to create a file with configurable path and content

## Usage

### Install collection
```bash
ansible-galaxy collection install my_own_namespace.yandex_cloud_elk