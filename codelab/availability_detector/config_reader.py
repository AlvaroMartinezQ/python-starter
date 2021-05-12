# script to read values from configuration files

from configparser import ConfigParser

def read_propertie():
    parser = ConfigParser()
    parser.read('.env')

    print (parser.get('mail_creds', 'email_host'))

def read_properties():
    parser = ConfigParser()
    parser.read('.env')

    data = {}
    data["email"] = parser.get('mail_creds', 'email_host')
    data["passw"] = parser.get('mail_creds', 'email_password')
    data["port"] = parser.get('mail_creds', 'email_host_port')
    print(data)
    return data

if __name__ == '__main__':
    read_properties()