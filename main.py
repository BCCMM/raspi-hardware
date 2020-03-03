import requests


def make_toast():
    ''' Enables the motor to begin making toast'''
    pass

def check_website():
    ''' Makes a request to the webserver, returns whether or not the toast is requested'''
    return False

if __name__ == 'main':
    check = check_website()
    if (check):
        make_toast()
        #TODO: Initiate timer on Webserver through post request