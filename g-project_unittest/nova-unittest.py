

# reference : http://docs.openstack.org/developer/python-novaclient/api.html

from novaclient import client

VERSION=2
USERNAME='admin'
PASSWORD='pasta1234'
PROJECT_ID='admin'
AUTH_URL='http://192.168.42.201:35357/v2.0'

class NovaManager(object):
    def __init__(self, username, password, project_id, auth_url):
        self.username = username
        self.password = password
        self.project_id = project_id
        self.auth_url = auth_url
        self.nova_client = self.get_client()

    def get_client(self):
        with client.Client(2, self.username, self.password,
                           self.project_id, self.auth_url) as nc:
            return nc

    def get_list_of_flavor(self):
        return self.nova_client.flavors.list()

    def get_list_of_vm(self):
        return self.nova_client.servers.list()

if __name__ == '__main__':
    nova_handle = NovaManager(USERNAME, PASSWORD, PROJECT_ID, AUTH_URL)
    flavors = nova_handle.get_list_of_flavor()
    print flavors

    vms = nova_handle.get_list_of_vm()
    print vms