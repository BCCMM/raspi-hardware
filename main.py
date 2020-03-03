import requests

URL  = 'https://i-toast.herokuapp.com/get-toast'

def make_toast():
    ''' Enables the motor to begin making toast'''
    pass

def check_website():
    ''' Makes a request to the webserver, returns whether or not the toast is requested'''
    info = requests.get(URL)
    return info.json()['flushToast']

if __name__ == '__main__':
	check = check_website()
	if (check):
		make_toast()
        #TODO: Initiate timer on Webserver through post request