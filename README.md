# ansible-test-connections
Ansible script to validate the connection between servers

#Run example:

ansible-playbook test-conn-master.yml -e "@vars/varfile1.json"

#Run multiple var files:

for files in $(ls -1 vars/*.json); do ansible-playbook test-conn-master.yml -e "@$files" ; done
