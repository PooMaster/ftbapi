import requests
import xml.etree.ElementTree as ET

#BASE_URL = 'http://ftb.cursecdn.com/FTB2/static/'
BASE_URL = 'http://www.creeperrepo.net/FTB2/static/'
MOD_LIST_URL = BASE_URL + 'modpacks.xml'
SERVER_BASE_URL = 'http://www.creeperrepo.net/FTB2/'

def get_modpacks():
    r = requests.get(MOD_LIST_URL)
    if r.status_code != 200:
        raise Exception("Bad response:\n" + r.text)

    root = ET.fromstring(r.text)
    return [FTBModPack(elem) for elem in root]

class FTBModPack:
    def __init__(self, element):
        attrs = element.attrib
        self.name = attrs['name']
        self.version = attrs['version']
        self.old_versions = attrs['oldVersions'].split(';')
        self.minecraft_version = attrs['mcVersion']

        server_parts = ('modpacks',
                        attrs['dir'],
                        attrs['repoVersion'],
                        attrs['serverPack'])
        self.server_url = SERVER_BASE_URL + '%5E'.join(server_parts)
        
        self.icon_url = BASE_URL + attrs['logo']
        self.splash_url = BASE_URL + attrs['image']
        if 'squareImage' in attrs:
            self.panel_url = BASE_URL + attrs['squareImage']
        else:
            self.panel_url = None
        self.description = attrs['description']
