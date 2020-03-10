import os
import stem.control

# It is designed to work with a the proxy onion-grater and a strong apparmor profile
# For this reason we can only read and write the hidden service private key in one specific directory
# For simplicity and by design, it will only create ephemral hidden service.
class OnionServices
    
    def __init(bind_port = {}, private_key = None):
        # authenticate
        controller = None # is instance var
        if os.path.exists(private_key):
            # create ephmeral hidden service with key_file and key_type
        else:
            # create a new hidden ephpemeral service

    # Persist the private key of the ephemeral hidden service to the dir path of *get_config_key_directory()*
    # the name of the key is the host name with the .key extension
    def persist_hidden_service():

    # Return *True* if the service is started from a key file
    def is_existing_service():

    # Return *True* if we are authenticated to the Tor control port
    def is_authenticated():

    # Return the hidden service address without the .onion suffix
    def get_host():

    # The port of the .onion address
    def get_external_port():

    # The port on which our application run locally
    def get_internal_port():

    # Return the name of the private key of the service
    def get_private_key_name():

    # The directory where we can read and write the private key
    def get_config_key_directory():

