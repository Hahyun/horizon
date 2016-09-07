

# reference : http://docs.openstack.org/developer/python-glanceclient/
# reference v2 : http://docs.openstack.org/developer/python-glanceclient/apiv2.html

from glanceclient import Client
from keystoneauth1 import loading
from keystoneauth1 import session

VERSION=2
USERNAME='admin'
PASSWORD='pasta1234'
PROJECT_NAME='admin'
AUTH_URL='http://192.168.42.201:35357/v3'
USER_DOMAIN_ID='default'
PROJECT_DOMAIN_ID='default'

class GlanceManager(object):
    def __init__(self, username, password, project_name, auth_url, user_domain_id=USER_DOMAIN_ID, project_domain_id=PROJECT_DOMAIN_ID):
        self.username = username
        self.password = password
        self.project_name = project_name
        self.auth_url = auth_url
        self.user_domain_id = user_domain_id
        self.project_domain_id = project_domain_id
        self.glance_client = self.get_client()

    def get_client(self):
        loader = loading.get_plugin_loader('password')
        auth = loader.load_from_options(
            auth_url=self.auth_url,
            username=self.username,
            password=self.password,
            project_name=self.project_name,
            user_domain_id=self.user_domain_id,
            project_domain_id=self.project_domain_id)

        ss = session.Session(auth=auth)
        client = Client('2', session=ss)
        return client

    def get_list_of_images(self):
        return self.glance_client.images.list()

if __name__ == '__main__':
    glance_handle = GlanceManager(USERNAME, PASSWORD, PROJECT_NAME, AUTH_URL)
    images = glance_handle.get_list_of_images()
    for image in images:
        print image
