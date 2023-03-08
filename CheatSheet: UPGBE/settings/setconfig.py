#put this file inside bgelogic folder; then create an empty object and set this python script as aways on Logic Bricks

from configparser import ConfigParser
from bge import logic, render

parser = ConfigParser()
#parser.read(logic.expandPath('//') + "../settings.ini")
parser.read(logic.expandPath('//') + "settings.ini")

for section in parser:
  if section == 'graphics':
    render.setAnisotropicFiltering(parser.getint(section, 'anisotropicfilter'))
    render.setMipmapping(parser.getint(section, 'mipmapping'))
    render.setFullScreen(parser.getboolean(section, 'fullscreen'))
    render.setVsync(parser.getint(section, 'vsync'))
    render.showFramerate(parser.getboolean(section, 'showfps'))
    render.setWindowSize(parser.getint(section, 'width'), parser.getint(section, 'height'))
