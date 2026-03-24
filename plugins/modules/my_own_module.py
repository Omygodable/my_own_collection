#!/usr/bin/python

# Copyright: (c) 2025 Your Name <your.email@example.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: Creates a text file on a remote host

version_added: "1.0.0"

description:
    - This module creates a file on the remote host with specified content.

options:
    path:
        description:
            - The absolute path where the file should be created.
        required: true
        type: str
    content:
        description:
            - The content to write to the file.
        required: true
        type: str

author:
    - Your Name (@yourGitHubHandle)
'''

EXAMPLES = r'''
- name: Create a file with content
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/example.txt
    content: "Hello, Ansible!"
'''

RETURN = r'''
path:
    description: The path of the created/modified file.
    type: str
    returned: always
    sample: "/tmp/example.txt"
content:
    description: The content written to the file.
    type: str
    returned: always
    sample: "Hello, Ansible!"
changed:
    description: Whether the file was changed.
    type: bool
    returned: always
'''

from ansible.module_utils.basic import AnsibleModule
import os

def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        path='',
        content=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']

    result['path'] = path
    result['content'] = content

    if module.check_mode:
        # В check mode просто проверяем, существует ли файл и совпадает ли содержимое
        if os.path.exists(path):
            with open(path, 'r') as f:
                existing_content = f.read()
            if existing_content == content:
                result['changed'] = False
            else:
                result['changed'] = True
        else:
            result['changed'] = True
        module.exit_json(**result)

    # Режим выполнения
    changed = False
    if not os.path.exists(path):
        changed = True
    else:
        with open(path, 'r') as f:
            existing_content = f.read()
        if existing_content != content:
            changed = True

    if changed:
        with open(path, 'w') as f:
            f.write(content)
        result['changed'] = True
    else:
        result['changed'] = False

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()