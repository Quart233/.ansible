#!/usr/bin/python

# Import AnsibleModule class
from ansible.module_utils.basic import AnsibleModule
import os

WORKDIR = '/etc/wireguard'

def main():
  # Define module arguments
  argument_spec = dict(
    path=dict(required=True, type='str'),
    content=dict(required=False, type='str'),
  )

  # Create AnsibleModule object
  module = AnsibleModule(argument_spec=argument_spec)

  # Get arguments passed from playbook
  name = module.params.get('name')

  # Attempt to create the file
  match  module.params['task']:
    case "init":
      try:
        result, output = module.run_command(executable="/usr/bin/wg", args=["genkey"])
        print(result)
        print(output)
        # with open(os.path.join(WORKDIR, name), 'w') as f:
        #     f.write(f'PrivateKey = {}')
        module.exit_json(changed=True, msg="File created successfully")
        # module.exit_json(changed=True, msg="File created successfully")
      except Exception as e:
        module.fail_json(msg="Failed to create file: {}".format(e))

if __name__ == '__main__':
  main()
