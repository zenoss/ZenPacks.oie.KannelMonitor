#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
#

import Globals, os, logging
from config import *

from Acquisition import aq_base
from Products.CMFCore import utils
from Products.ZenModel.ZenPack import ZenPackBase
from Products.CMFCore.DirectoryView import registerDirectory
from Products.CMFCore.permissions import AddPortalContent

logger = logging.getLogger(PROJECTNAME)
logger.info('Installing KannelMonitor')

for directory in (SKINS_DIR, os.path.join(os.path.dirname(__file__), SKINS_DIR)):
    try:
        registerDirectory(directory, GLOBALS)
    except:
        pass

from lbn.zenoss import packutils
import setuphandlers


class ZenPack(ZenPackBase):
    """ Zenoss eggy thing """
    packZProperties = [
        ('zKannelPlugin', '/usr/lib64/nagios/plugins/contrib/check_kannel', 'string'),
        ('zKannelPort', '13000', 'int'),
        ]

    def install(self, zport):
        """
        Set the collector plugin
        """
        ZenPackBase.install(self, zport)

	setuphandlers.install(zport, self)

def initialize(context):
    """ Zope Product """
    
    zport = packutils.zentinel(context)
    if zport and not packutils.hasZenPack(zport, __name__):
        zpack =  ZenPack(__name__)
        packutils.addZenPack(zport, zpack, SKINS_DIR, SKINNAME, GLOBALS)
        setuphandlers.install(zport, zpack)


