#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
#

PROJECTNAME = "ZenPacks.oie.KannelMonitor"
SKINS_DIR = 'skins'
SKINNAME = PROJECTNAME
GLOBALS = globals()

# all the individual values we're interested in
DATAPOINTS = ('recvqueue', 'sentqueue', 'storesize', 'recv', 'sent')

# which graph's we're gong to apply the above values to
GRAPHPOINTS = {'smsc': ('recvqueue', 'sentqueue', 'recv', 'sent'),
               'store': ('storesize',)}
