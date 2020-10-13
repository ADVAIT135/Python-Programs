import requests
class DeviceTracker():
    def __init__(self, ip_url):
        self.ip_url = ip_url
    def get_json_data(self):
        device_req = requests.get(url=self.ip_url)
        if device_req.status_code == 200:
            device_json = device_req.json()
        else:
            device_json = {}
        return device_json
    def get_city_name(self):
        device_data = self.get_json_data()
        city_name = device_data['city']
        return city_name
ip_url = 'http://ip-api.com/json'
my_loc = DeviceTracker(ip_url=ip_url)
my_loc.get_city_name()
