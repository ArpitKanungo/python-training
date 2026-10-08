'''
Read network configuration from network.cfg and store it in a dictionary.
1. Create an empty dictionary to store the network configuration.
2. Then do the following tasks:
 2.1. Update the interface to eth1
 2.2. Update onboot to yes
 2.3. Update bootproto to static
 2.4. Add IPADDR -> 192.168.1.10
 2.5. Add PREFIX -> 24
 2.6. DNS1 = 122.33.344.555
3. Use pprint to display the configuration.
4. Dict operation
5. Use pprint to display the dictionary after performing dict operations.
6. Create new configuration file with the updated settings.
'''
import pprint
def read_file():
    fobj = open('network.cfg', 'r')
    config_dict = {}
    for line in fobj.readlines():
        k ,v = line.strip().split('=')
        config_dict[k] = v
    fobj.close()
    return config_dict

def update_configurations(config_dict):
    config_dict['Interface'] = 'eth1'
    config_dict['onboot'] = 'yes'
    config_dict['bootproto'] = 'static'
    config_dict['IPADDR'] = '192.168.1.10'
    config_dict['PREFIX'] = '24'
    config_dict['DNS1'] = '122.33.344.555'
    return config_dict

def write_to_file(config_dict, filename):
    with open(filename, 'w') as wobj:
        for k, v in config_dict.items():
            wobj.write(f"{k}={v}\n")

config_dict = read_file()

pprint.pprint(config_dict)

# Updation of network configuration and addition of new parameters
config_dict = update_configurations(config_dict)

# Writing the updated configuration back to the file
write_to_file(config_dict, 'new_network.cfg')

pprint.pprint(config_dict)
