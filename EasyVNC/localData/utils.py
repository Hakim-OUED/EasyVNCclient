from configparser import ConfigParser
import socket
import os
chemin = os.path.dirname(os.path.realpath(__file__)) + '/data.ini'

def read_data(filename=chemin, section='global'):
    # creation de parser et lecture du fichier de configuration
    parser = ConfigParser()
    parser.read(filename)
    data = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            data[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    return data


def save_config(user_id, usermail, session_id, filename = chemin, section='global'):
    # creation de parser et lecture du fichier de configuration
    parser = ConfigParser()
    parser.read(filename)
    if parser.has_section(section):
        parser.set(section,'user_id', user_id)
        parser.set(section, 'usermail', usermail)
        parser.set(section, 'session_id', session_id)
        with open(chemin, 'w') as configfile:
            parser.write(configfile)
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

def read_socket_data(filename=chemin, section='socket'):
    # creation de parser et lecture du fichier de configuration
    parser = ConfigParser()
    parser.read(filename)
    data = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            data[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    return data