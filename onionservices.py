import os
from pathlib import Path
from stem.control import Controller

class OnionServices:
    """
     It is designed to work with a the proxy onion-grater and a strong apparmor profile
     For this reason we can only read and write the hidden service private key in one specific directory
     For simplicity and by design, it will only create ephemral hidden service.
    """

    def __init__(self,bind_port = {}, private_key_name = None):
        self.service = None
        self.is_existing_service = False
        self.is_authenticated = False
        self.private_key_name = private_key_name
        self.bind_port = bind_port
        if os.path.exists(self.get_private_key_path()): self.is_existing_service = True
        
    def start(self):
        with self.connect_to_controller() as controller: 
            controller.authenticate()
            self.is_authenticated = True
            if self.has_existed():
                with open(self.get_private_key_path()) as key_file:
                    key_type, key_content = key_file.read().split(':', 1)
                self.service = controller.create_ephemeral_hidden_service(
                    self.bind_port, await_publication=True, key_type=key_type,
                    key_content=key_content
                )
            else:
                self.service = controller.create_ephemeral_hidden_service(
                    self.bind_port, await_publication=True
                )
                if self.is_running() and self.private_key_name == None:
                    self.private_key_name = self.service.service_id + '.key'

    def stop(self):
        with self.connect_to_controller() as controller:
            if(self.is_running()):
                controller.remove_ephemeral_hidden_service(self.service.service_id)

    def connect_to_controller(self):
        return Controller.from_port(port=9051)

    # Persist the private key of the ephemeral hidden service to the dir path of *get_config_key_directory()*
    # the name of the key is the host name with the .key extension
    def persist(self):
        if not self.is_running(): return
        with open(self.get_private_key_path(), 'w') as key_file:
            key_file.write('%s:%s' % (self.service.private_key_type, self.service.private_key))

    # Return *True* if the service is started from a key file
    def has_existed(self):
        return self.is_existing_service

    # Return *True* if we are authenticated to the Tor control port
    def is_authenticated_to_tor_controller(self):
        return self.is_authenticated

    def is_running(self):
        return self.service and self.service.service_id

    # Return the hidden service address without the .onion suffix
    def get_hostname(self):
        return self.service.service_id

    # The port of the .onion address
    def get_external_port(self):
        return self.external_port

    # The port on which our application run locally
    def get_internal_port(self):
        return self.internal_port

    # Return the name of the private key of the service
    def get_private_key_name(self):
        return self.private_key_name

    def get_private_key_path(self):
        return str(self.get_config_key_directory().joinpath(str(self.get_private_key_name())))

    # The directory where we can read and write the private key
    def get_config_key_directory(self):
        return Path.home().joinpath('.config', 'onionservices')
