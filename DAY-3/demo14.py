'''This is network configuration'''
import pprint

def f1():
    '''Return an empty dict'''
    network_params = {}
    return network_params

def f2(network_params):
    '''This f2 block received dictionary name as argument to
    perform network static configuration from the file 'network.cfg'.'''
    with open('network.cfg','r') as fobj:
        for var in fobj.readlines():
            var = var.strip()
            K,V = var.split("=")
            network_params[K] = V # Adding new data to dict
    return network_params

def f3(network_params):
    '''display network parameters'''
    pprint.pprint(network_params)

def f4(network_params):
    '''dict operation'''
    network_params['Interface'] = 'eth1'
    network_params['bootproto'] = 'static'
    network_params['onboot'] = 'yes'
    network_params['IPADD'] = '192.168.1.10'
    network_params['PREFIX'] = 24
    network_params['DNS1']= '122.33.344.555'
    return network_params

def f5(network_params):
    '''write new config file from updated dict'''
    with open('new_network.cfg','w') as wobj:
        for var in network_params:
            wobj.write(f'{var} = {network_params.get(var)}\n')