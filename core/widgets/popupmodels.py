from re import search
import modules as GUIs
from core.main import QtGui,QtCore
from core.utils import Refactor
from collections import OrderedDict
from core.widgets.pluginssettings import BDFProxySettings,ResponderSettings
"""
Description:
    This program is a core for wifi-pumpkin.py. file which includes functionality
    for load plugins mitm attack and phishing module.

Copyright:
    Copyright (C) 2015-2017 Marcos Nesster P0cl4bs Team
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>
"""

class PopUpPlugins(QtGui.QVBoxLayout):
    ''' this module control all plugins to MITM attack'''
    sendSingal_disable = QtCore.pyqtSignal(object)
    def __init__(self,FSettings,main,parent=None):
        super(PopUpPlugins, self).__init__(parent)
        self.main_method = main
        self.FSettings = FSettings
        self.layout = QtGui.QVBoxLayout()
        self.layoutform = QtGui.QFormLayout()
        self.layoutproxy = QtGui.QVBoxLayout()
        self.GroupPlugins = QtGui.QGroupBox()
        self.GroupPluginsProxy = QtGui.QGroupBox()
        self.GroupPlugins.setTitle('plugins:')
        self.GroupPluginsProxy.setTitle('Enable proxy server:')
        self.GroupPluginsProxy.setCheckable(True)
        self.GroupPluginsProxy.clicked.connect(self.get_disable_proxyserver)
        self.GroupPluginsProxy.setLayout(self.layoutproxy)
        self.GroupPlugins.setLayout(self.layoutform)

        self.check_netcreds     = QtGui.QCheckBox('net-creds ')
        self.check_responder    = QtGui.QCheckBox('Responder')
        self.check_tcpproxy     = QtGui.QCheckBox('TCP-Proxy')
        self.check_pumpkinProxy = QtGui.QRadioButton('Pumpkin-Proxy')
        self.check_dns2proy     = QtGui.QRadioButton('SSLstrip+|Dns2proxy')
        self.check_sergioProxy  = QtGui.QRadioButton('SSLstrip|Sergio-proxy')
        self.check_bdfproxy     = QtGui.QRadioButton('BDFProxy-ng')
        self.check_noproxy      = QtGui.QRadioButton('No Proxy')

        self.btnBDFSettings    = QtGui.QPushButton('Change')
        self.btnResponderSettings = QtGui.QPushButton('Change')
        self.btnBDFSettings.setIcon(QtGui.QIcon('icons/config.png'))
        self.btnResponderSettings.setIcon(QtGui.QIcon('icons/config.png'))
        self.btnBDFSettings.clicked.connect(self.ConfigOBJBDFproxy)
        self.btnResponderSettings.clicked.connect(self.ConfigOBJBResponder)

        # set text description plugins
        self.check_dns2proy.setObjectName('This tools offer a different features '
        'for post-explotation once you change the DNS server to a Victim. coded by: LeonardoNve')
        self.check_sergioProxy.setObjectName('Sergio proxy is an HTTP proxy that was written '
        'in Python for the Twisted framework. coded by: LeonardoNve')
        self.check_bdfproxy.setObjectName('Patch Binaries via MITM: BackdoorFactory + mitmProxy, '
        'bdfproxy-ng is a fork and review of the original BDFProxy. coded by: secretsquirrel.')
        self.check_pumpkinProxy.setObjectName('Transparent proxy - intercepting HTTP data, '
        'this proxy server that allows to intercept requests and response on the fly')

        # desction plugin checkbox
        self.check_netcreds.setObjectName('Sniff passwords and hashes from an interface or pcap file.'
        ' coded by: Dan McInerney')
        self.check_tcpproxy.setObjectName('sniff for isntercept network traffic on UDP,TCP protocol.'
        ' get password,hash,image,etc...')
        self.check_responder.setObjectName('Responder an LLMNR, NBT-NS and MDNS poisoner. '
        'By default, the tool will only answer to File Server Service request, which is for SMB.')


        # table 1 for add plugins with QradioBtton
        self.THeadersPluginsProxy  = OrderedDict(
        [   ('Plugins',[self.check_pumpkinProxy,self.check_dns2proy,self.check_sergioProxy,self.check_bdfproxy]),
            ('Settings',[QtGui.QPushButton('None'),QtGui.QPushButton('None'),QtGui.QPushButton('None'),self.btnBDFSettings]),
            ('Description',[self.check_pumpkinProxy.objectName(),
            self.check_dns2proy.objectName(),self.check_sergioProxy.objectName(),
            self.check_bdfproxy.objectName()])
        ])

        # table 2 for add plugins with checkbox
        self.THeadersPlugins  = OrderedDict(
        [   ('Plugins',[self.check_tcpproxy,self.check_responder]),
            ('Settings',[QtGui.QPushButton('None'),self.btnResponderSettings]),
            ('Description',[self.check_tcpproxy.objectName(),self.check_responder.objectName(),])
        ])

        self.tableplugins = QtGui.QTableWidget()
        self.tableplugins.setColumnCount(3)
        self.tableplugins.setRowCount(len(self.THeadersPluginsProxy['Plugins']))
        self.tableplugins.resizeRowsToContents()
        self.tableplugins.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        self.tableplugins.horizontalHeader().setStretchLastSection(True)
        self.tableplugins.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableplugins.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableplugins.verticalHeader().setVisible(False)
        self.tableplugins.verticalHeader().setDefaultSectionSize(23)
        self.tableplugins.setSortingEnabled(True)
        self.tableplugins.setHorizontalHeaderLabels(self.THeadersPluginsProxy.keys())
        self.tableplugins.horizontalHeader().resizeSection(0,158)
        self.tableplugins.horizontalHeader().resizeSection(1,80)
        self.tableplugins.resizeRowsToContents()

        self.tableplugincheckbox = QtGui.QTableWidget()
        self.tableplugincheckbox.setColumnCount(3)
        self.tableplugincheckbox.setRowCount(len(self.THeadersPlugins['Plugins']))
        self.tableplugincheckbox.resizeRowsToContents()
        self.tableplugincheckbox.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        self.tableplugincheckbox.horizontalHeader().setStretchLastSection(True)
        self.tableplugincheckbox.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableplugincheckbox.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableplugincheckbox.verticalHeader().setVisible(False)
        self.tableplugincheckbox.verticalHeader().setDefaultSectionSize(23)
        self.tableplugincheckbox.setSortingEnabled(True)
        self.tableplugincheckbox.setHorizontalHeaderLabels(self.THeadersPlugins.keys())
        self.tableplugincheckbox.horizontalHeader().resizeSection(0,158)
        self.tableplugincheckbox.horizontalHeader().resizeSection(1,80)
        self.tableplugincheckbox.resizeRowsToContents()

        # add all widgets in Qtable 1 plgins
        Headers = []
        for n, key in enumerate(self.THeadersPluginsProxy.keys()):
            Headers.append(key)
            for m, item in enumerate(self.THeadersPluginsProxy[key]):
                if type(item) == type(QtGui.QRadioButton()) or type(item) == type(QtGui.QPushButton()):
                    self.tableplugins.setCellWidget(m,n,item)
                else:
                    item = QtGui.QTableWidgetItem(item)
                    self.tableplugins.setItem(m, n, item)
        self.tableplugins.setHorizontalHeaderLabels(self.THeadersPluginsProxy.keys())
        # add all widgets in Qtable 2 plugin
        Headers = []
        for n, key in enumerate(self.THeadersPlugins.keys()):
            Headers.append(key)
            for m, item in enumerate(self.THeadersPlugins[key]):
                if type(item) == type(QtGui.QCheckBox()) or type(item) == type(QtGui.QPushButton()):
                    self.tableplugincheckbox.setCellWidget(m,n,item)
                else:
                    item = QtGui.QTableWidgetItem(item)
                    self.tableplugincheckbox.setItem(m, n, item)
        self.tableplugins.setHorizontalHeaderLabels(self.THeadersPlugins.keys())

        self.proxyGroup = QtGui.QButtonGroup()
        self.proxyGroup.addButton(self.check_pumpkinProxy)
        self.proxyGroup.addButton(self.check_dns2proy)
        self.proxyGroup.addButton(self.check_sergioProxy)
        self.proxyGroup.addButton(self.check_noproxy)
        self.proxyGroup.addButton(self.check_bdfproxy)

        self.check_tcpproxy.clicked.connect(self.checkBoxTCPproxy)
        self.check_pumpkinProxy.clicked.connect(self.checkGeneralOptions)
        self.check_dns2proy.clicked.connect(self.checkGeneralOptions)
        self.check_sergioProxy.clicked.connect(self.checkGeneralOptions)
        self.check_bdfproxy.clicked.connect(self.checkGeneralOptions)
        self.check_noproxy.clicked.connect(self.checkGeneralOptions)
        self.check_responder.clicked.connect(self.checkBoxResponder)

        self.layoutproxy.addWidget(self.tableplugins)
        self.layoutproxy.addWidget(self.tableplugincheckbox)
        self.layout.addWidget(self.GroupPluginsProxy)
        self.addLayout(self.layout)

    def get_disable_proxyserver(self):
        ''' set disable or activate plugin proxy '''
        self.check_noproxy.setChecked(True)
        self.tableplugincheckbox.setEnabled(True)
        self.sendSingal_disable.emit(self.check_noproxy.isChecked())
        self.checkBoxTCPproxy()

    # control checkbox plugins
    def checkGeneralOptions(self):
        ''' settings plugins proxy options and rules iptables '''
        self.unset_Rules('dns2proxy')
        self.unset_Rules('sslstrip')
        self.unset_Rules('bdfproxy')
        self.FSettings.Settings.set_setting('plugins','pumpkinproxy_plugin',self.check_pumpkinProxy.isChecked())
        self.FSettings.Settings.set_setting('plugins','sergioproxy_plugin',self.check_sergioProxy.isChecked())
        self.FSettings.Settings.set_setting('plugins','dns2proxy_plugin',self.check_dns2proy.isChecked())
        self.FSettings.Settings.set_setting('plugins','bdfproxy_plugin',self.check_bdfproxy.isChecked())
        self.FSettings.Settings.set_setting('plugins','noproxy',self.check_noproxy.isChecked())
        if self.check_sergioProxy.isChecked():
            self.main_method.set_proxy_statusbar('SSLstrip|Sergio-proxy')
            self.main_method.PumpkinProxyTAB.tabcontrol.setEnabled(False) # disable ProxyPumpkinTAB
            self.main_method.ProxyPluginsTAB.scrollwidget.setEnabled(True) # enable SSLSTRIP Proxy TAB
            self.set_sslStripRule()
        elif self.check_dns2proy.isChecked():
            self.main_method.set_proxy_statusbar('SSLstrip+|Dns2-proxy')
            self.main_method.PumpkinProxyTAB.tabcontrol.setEnabled(False)
            self.main_method.ProxyPluginsTAB.scrollwidget.setEnabled(True)
            self.set_sslStripRule()
            self.set_Dns2proxyRule()
        elif self.check_bdfproxy.isChecked():
            self.main_method.set_proxy_statusbar('BDF-proxy-ng')
            self.main_method.PumpkinProxyTAB.tabcontrol.setEnabled(False)
            self.main_method.ProxyPluginsTAB.scrollwidget.setEnabled(False)
            self.unset_Rules('dns2proxy')
            self.unset_Rules('sslstrip')
            self.set_BDFproxyRule()
        elif self.check_pumpkinProxy.isChecked():
            self.main_method.set_proxy_statusbar('Pumpkin-Proxy')
            self.main_method.PumpkinProxyTAB.tabcontrol.setEnabled(True)
            self.main_method.ProxyPluginsTAB.scrollwidget.setEnabled(False)
            self.unset_Rules('dns2proxy')
            self.unset_Rules('sslstrip')
            self.set_PumpkinProxy()
        elif self.check_noproxy.isChecked():
            self.main_method.set_proxy_statusbar('',disabled=True)
            self.main_method.PumpkinProxyTAB.tabcontrol.setEnabled(False)
            self.main_method.ProxyPluginsTAB.scrollwidget.setEnabled(False)
            self.unset_Rules('dns2proxy')
            self.unset_Rules('sslstrip')
            self.unset_Rules('bdfproxy')

    def ConfigOBJBDFproxy(self):
        ''' show BDFproxy settings page '''
        self.SettingsBDFProxy  = BDFProxySettings()
        self.SettingsBDFProxy.show()

    def ConfigOBJBResponder(self):
        ''' show REsponder settings page '''
        self.SettingsResponder  = ResponderSettings()
        self.SettingsResponder.show()

    def checkBoxTCPproxy(self):
        if self.check_tcpproxy.isChecked():
            self.FSettings.Settings.set_setting('plugins','tcpproxy_plugin',True)
            self.main_method.PacketSnifferTAB.tabcontrol.setEnabled(True)
            self.main_method.ImageCapTAB.TableImage.setEnabled(True)
        else:
            self.FSettings.Settings.set_setting('plugins','tcpproxy_plugin',False)
            self.main_method.PacketSnifferTAB.tabcontrol.setEnabled(False)
            self.main_method.ImageCapTAB.TableImage.setEnabled(False)

    def checkBoxResponder(self):
        if self.check_responder.isChecked():
            self.FSettings.Settings.set_setting('plugins','responder_plugin',True)
        else:
            self.FSettings.Settings.set_setting('plugins','responder_plugin',False)

    def optionsRules(self,type):
        ''' add rules iptable by type plugins'''
        search = {
        'sslstrip': str('iptables -t nat -A PREROUTING -p tcp'+
        ' --destination-port 80 -j REDIRECT --to-port '+self.FSettings.redirectport.text()),
        'dns2proxy':str('iptables -t nat -A PREROUTING -p udp --destination-port 53 -j REDIRECT --to-port 53'),
        'bdfproxy':str('iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080'),
        'PumpkinProxy' : str('iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080')}
        return search[type]

    # set rules to sslstrip
    def set_sslStripRule(self):
        items = []
        for index in xrange(self.FSettings.ListRules.count()):
            items.append(str(self.FSettings.ListRules.item(index).text()))
        if self.optionsRules('sslstrip') in items:
            return
        item = QtGui.QListWidgetItem()
        item.setText(self.optionsRules('sslstrip'))
        item.setSizeHint(QtCore.QSize(30,30))
        self.FSettings.ListRules.addItem(item)

    # set redirect port rules dns2proy
    def set_Dns2proxyRule(self):
        item = QtGui.QListWidgetItem()
        item.setText(self.optionsRules('dns2proxy'))
        item.setSizeHint(QtCore.QSize(30,30))
        self.FSettings.ListRules.addItem(item)

    # set redirect port rules bdfproxy
    def set_BDFproxyRule(self):
        items = []
        for index in xrange(self.FSettings.ListRules.count()):
            items.append(str(self.FSettings.ListRules.item(index).text()))
        if self.optionsRules('bdfproxy') in items:
            return
        item = QtGui.QListWidgetItem()
        item.setText(self.optionsRules('bdfproxy'))
        item.setSizeHint(QtCore.QSize(30,30))
        self.FSettings.ListRules.addItem(item)

    def set_PumpkinProxy(self):
        items = []
        for index in xrange(self.FSettings.ListRules.count()):
            items.append(str(self.FSettings.ListRules.item(index).text()))
        if self.optionsRules('PumpkinProxy') in items:
            return
        item = QtGui.QListWidgetItem()
        item.setText(self.optionsRules('PumpkinProxy'))
        item.setSizeHint(QtCore.QSize(30,30))
        self.FSettings.ListRules.addItem(item)

    def unset_Rules(self,type):
        ''' remove rules from Listwidget in settings widget'''
        items = []
        for index in xrange(self.FSettings.ListRules.count()):
            items.append(str(self.FSettings.ListRules.item(index).text()))
        for position,line in enumerate(items):
            if self.optionsRules(type) == line:
                self.FSettings.ListRules.takeItem(position)
