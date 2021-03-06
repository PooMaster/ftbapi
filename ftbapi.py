import requests
import xml.etree.ElementTree as ET

BASE_URL = 'http://www.creeperrepo.net/FTB2/'
STATIC_URL = BASE_URL + 'static/'
MODPACK_URL = STATIC_URL + 'modpacks.xml'
THIRD_PARTY_URL = STATIC_URL + 'thirdparty.xml'
#MAPS_URL = STATIC_URL + 'maps.xml'
#TEXTUREPACK_URL = STATIC_URL + 'texturepack.xml'

def get_modpacks(session=None):
    return _make_modpacks(MODPACK_URL, session=session)

def get_third_party_modpacks(session=None):
    return _make_modpacks(THIRD_PARTY_URL, session=session)

def _make_modpacks(modpack_xml, session=None):
    if session is None:
        session = requests.Session()
    r = session.get(modpack_xml)
    if r.status_code != 200:
        raise Exception("Bad response: {} {}".format(r.status_code, r.reason))

    root = ET.fromstring(r.text)
    return [FTBModPack(elem) for elem in root if elem.attrib['serverPack']]

class FTBModPack:
    def __init__(self, element):
        attrs = element.attrib
        self.name = attrs['name']
        self.version = attrs['version']
        self.old_versions = attrs['oldVersions'].split(';')
        self.minecraft_version = attrs['mcVersion']
        self.description = attrs['description']

        server_parts = ('modpacks',
                        attrs['dir'],
                        attrs['repoVersion'],
                        attrs['serverPack'])
        self.server_url = BASE_URL + '%5E'.join(server_parts)

        self.mods = [mod.strip() for mod in attrs['mods'].split(';') if mod]
        
        self.icon_url = STATIC_URL + attrs['logo']
        self.splash_url = STATIC_URL + attrs['image']
        if 'squareImage' in attrs:
            self.panel_url = STATIC_URL + attrs['squareImage']
        else:
            self.panel_url = None
        
        self.dir = attrs['dir']

if __name__ == '__main__':
    for modpack in get_modpacks():
        print("{} v{} for Minecraft {}".format(modpack.name, modpack.version, 
                                               modpack.minecraft_version))
        print(modpack.description)
        print(modpack.server_url)
        print()
