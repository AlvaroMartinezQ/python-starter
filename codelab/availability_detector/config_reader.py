# script to read values from configuration files

from configparser import ConfigParser

def read_properties():
    parser = ConfigParser()
    parser.read('.env')

    print (parser.get('mail_creds', 'email_host'))


if __name__ == '__main__':
    read_properties()