import requests
 
class DeviceTracker ():
    def __init__(self,ip_url):
        self.ip_url = ip_url

    def get_json_data(self):
        device_req = requests.get(url = self.ip_url)
        if device_req.status_code == 200:
            device_json = device_req.json()
        else:
            device_json = {}
        return device_json
    def get_device_details(self):
        device_data = self.get_json_data()
        device_details = device_data['status']['country']['countryCode']['region']['regionName']['city']['zip']['lat']['lon']['timezone']['isp']['org']['as']['query']
        return device_details
ip_url = 'http://ip-api.com/json'
my_loc = DeviceTracker(ip_url = ip_url)
print(my_loc.get_device_details)












 


































































































    
    
    
ip_url = 'http://ip-api.com/json'
my_loc = DeviceTracker(ip_url=ip_url)
my_loc.get_json_data()
print(my_loc)

















































    

    

    

