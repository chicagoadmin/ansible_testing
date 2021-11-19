Role Name
=========

common

Role Variables
--------------

`common_users` - A dict containing  the following
```
- name: username
  admin: [true|false]
  ssh_key: auth_key_containts 
```

Dependencies
------------
 `ansible-galaxy collection install ansible.posix`

Example Playbook
----------------

    - hosts: servers
      roles:
         - common

License
-------

All Rights
