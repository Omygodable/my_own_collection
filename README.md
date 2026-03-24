# Ansible Collection - my_own_namespace.yandex_cloud_elk

# Yandex Cloud ELK Collection

## Description
This collection provides modules and roles for managing files on remote hosts.

## Modules
- `my_own_module`: Creates a text file with specified content on a remote host.

## Roles
- `my_own_role`: A role that uses `my_own_module` to create a file with configurable path and content

Создание модуля Ansible для файла
Помощь с заданием поэтапно
Помощь в выполнении домашнего задания по тестированию ролей
Настройка тестирования роли Vector
Автоматизация задач на работе с помощью скриптов
Создание ролей Ansible для ClickHouse Vector и Lighthouse
Шуточное выражение о себе
Помощь в подготовке к собеседованию DevOps
Выбор фразы о медленном сервере
Анализ и улучшение резюме
Помощь с английским тестом
Помощь с фото для анализа проблемы
Решение конфликтов в Bitbucket с помощью IntelliJ
Уведомление о изменениях в воинском учете
Приветствие и обсуждение самочувствия
Создание модуля Ansible для файла

Хорошо, структура коллекции создана. Теперь нужно добавить роль и заполнить файлы.
Выполните следующие шаги:
1. Создайте структуру роли:
bash

cd ~/my_own_namespace/yandex_cloud_elk
mkdir -p roles/my_own_role/{tasks,defaults}

2. Создайте файл roles/my_own_role/tasks/main.yml:
bash

cat > roles/my_own_role/tasks/main.yml << 'EOF'
---
- name: Create file using my_own_module
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: "{{ file_path | default('/tmp/test.txt') }}"
    content: "{{ file_content | default('Hello from role') }}"
EOF

3. Создайте файл roles/my_own_role/defaults/main.yml:
bash

cat > roles/my_own_role/defaults/main.yml << 'EOF'
---
file_path: /tmp/test.txt
file_content: "Hello from role"
EOF

4. Обновите playbook.yml:
bash

cat > playbook.yml << 'EOF'
---
- name: Test my_own_role
  hosts: localhost
  gather_facts: false
  roles:
    - my_own_role
EOF

5. Убедитесь, что модуль находится в правильном месте:
bash

ls -la plugins/modules/

Если модуля там нет, скопируйте его:
bash

cp ~/ansible/ansible/my_own_module.py plugins/modules/

6. Проверьте структуру:
bash

tree ~/my_own_namespace/yandex_cloud_elk/
# или если tree нет:
find ~/my_own_namespace/yandex_cloud_elk/ -type f

После выполнения пришлите:

    Результат команды tree ~/my_own_namespace/yandex_cloud_elk/ или find

    Содержимое файла plugins/modules/my_own_module.py (первые 30 строк, чтобы убедиться, что DOCUMENTATION заполнена правильно)

Важное замечание:

В файле модуля my_own_module.py в секции DOCUMENTATION должно быть указано правильное имя модуля и автор. Убедитесь, что там есть:
python

module: my_own_module
author:
    - Your Name (@yourGitHubHandle)

Если нет — отредактируйте файл перед копированием в коллекцию.
mike@Netology:~/my_own_namespace/yandex_cloud_elk$ find ~/my_own_namespace/yandex_cloud_elk/ -type f
/home/mike/my_own_namespace/yandex_cloud_elk/galaxy.yml
/home/mike/my_own_namespace/yandex_cloud_elk/roles/my_own_role/defaults/main.yml
/home/mike/my_own_namespace/yandex_cloud_elk/roles/my_own_role/tasks/main.yml
/home/mike/my_own_namespace/yandex_cloud_elk/plugins/modules/my_own_module.py
/home/mike/my_own_namespace/yandex_cloud_elk/plugins/README.md
/home/mike/my_own_namespace/yandex_cloud_elk/playbook.yml
/home/mike/my_own_namespace/yandex_cloud_elk/meta/runtime.yml
/home/mike/my_own_namespace/yandex_cloud_elk/README.md

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

Отлично! Структура коллекции правильная, и модуль на месте. ✅
Теперь продолжим выполнение задания:
Этап 12. Заполнение документации и выгрузка в репозиторий

1. Отредактируйте README.md в корне коллекции:
bash

cat > README.md << 'EOF'
# Yandex Cloud ELK Collection

## Description
This collection provides modules and roles for managing files on remote hosts.

## Modules
- `my_own_module`: Creates a text file with specified content on a remote host.

## Roles
- `my_own_role`: A role that uses `my_own_module` to create a file with configurable path and content.

## Usage

### Install collection
```bash
ansible-galaxy collection install my_own_namespace.yandex_cloud_elk