# ansible-role-ncats-webui #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-ncats-webui/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-ncats-webui/actions)
[![CodeQL](https://github.com/cisagov/ansible-role-ncats-webui/workflows/CodeQL/badge.svg)](https://github.com/cisagov/ansible-role-ncats-webui/actions/workflows/codeql-analysis.yml)

An Ansible role for installing
[ncats-webui](https://github.com/cisagov/ncats-webui).

## Requirements ##

None.

## Role Variables ##

None.

<!--
| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| optional_variable | Describe its purpose. | `default_value` | No |
| required_variable | Describe its purpose. | n/a | Yes |
-->

## Dependencies ##

- [cisagov/ansible-role-docker](https://github.com/cisagov/ansible-role-docker)

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: yes
  become_method: sudo
  tasks:
    - name: Install the NCATS WebUI Docker configuration
      ansible.builtin.include_role:
        name: ncats_webui
```

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

## Author Information ##

Shane Frasier - <jeremy.frasier@trio.dhs.gov>
