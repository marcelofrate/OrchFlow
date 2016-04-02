#!/usr/bin/python

import re
import sys

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info, error
from mininet.link import Link, TCLink, Intf
from mininet.util import quietRun

def topology():
    "Create a network."
    net = Mininet( controller=RemoteController, link=TCLink, switch=OVSKernelSwitch )

    print "*** Creating nodes"
    h1 = net.addHost( 'h1', mac='0a:0a:0a:0a:0a:01', ip='192.168.3.1/24' )
    h2 = net.addHost( 'h2', mac='0a:0a:0a:0a:0a:02', ip='192.168.3.2/24' )
    h3 = net.addHost( 'h3', mac='0a:0a:0a:0a:0a:03', ip='192.168.3.3/24' )
    h4 = net.addHost( 'h4', mac='0a:0a:0a:0a:0a:04', ip='192.168.3.4/24' )

    h5 = net.addHost( 'h5', mac='0a:0a:0a:0a:0a:05', ip='192.168.3.5/24' )
    h6 = net.addHost( 'h6', mac='0a:0a:0a:0a:0a:06', ip='192.168.3.6/24' )
    h7 = net.addHost( 'h7', mac='0a:0a:0a:0a:0a:07', ip='192.168.3.7/24' )
    h8 = net.addHost( 'h8', mac='0a:0a:0a:0a:0a:08', ip='192.168.3.8/24' )

    h9 = net.addHost( 'h9', mac='0a:0a:0a:0a:0a:09', ip='192.168.3.9/24' )
    h10 = net.addHost( 'h10', mac='0a:0a:0a:0a:0a:0a', ip='192.168.3.10/24' )
    h11 = net.addHost( 'h11', mac='0a:0a:0a:0a:0a:0b', ip='192.168.3.11/24' )
    h12 = net.addHost( 'h12', mac='0a:0a:0a:0a:0a:0c', ip='192.168.3.12/24' )

    s1 = net.addSwitch( 's1', protocols='OpenFlow13', listenPort=6671, mac='00:00:00:00:00:01' )
    s2 = net.addSwitch( 's2', protocols='OpenFlow13', listenPort=6672, mac='00:00:00:00:00:02' )
    s3 = net.addSwitch( 's3', protocols='OpenFlow13', listenPort=6673, mac='00:00:00:00:00:03' )
    s4 = net.addSwitch( 's4', protocols='OpenFlow13', listenPort=6674, mac='00:00:00:00:00:04' )
    s5 = net.addSwitch( 's5', protocols='OpenFlow13', listenPort=6675, mac='00:00:00:00:00:05' )
    s6 = net.addSwitch( 's6', protocols='OpenFlow13', listenPort=6676, mac='00:00:00:00:00:06' )
    s7 = net.addSwitch( 's7', protocols='OpenFlow13', listenPort=6677, mac='00:00:00:00:00:07' )

    s8 = net.addSwitch( 's8', protocols='OpenFlow13', listenPort=6678, mac='00:00:00:00:00:08' )
    s9 = net.addSwitch( 's9', protocols='OpenFlow13', listenPort=6679, mac='00:00:00:00:00:09' )
    s10 = net.addSwitch( 's10', protocols='OpenFlow13', listenPort=6680, mac='00:00:00:00:00:0a' )
    s11 = net.addSwitch( 's11', protocols='OpenFlow13', listenPort=6681, mac='00:00:00:00:00:0b' )
    s12 = net.addSwitch( 's12', protocols='OpenFlow13', listenPort=6682, mac='00:00:00:00:00:0c' )
    s13 = net.addSwitch( 's13', protocols='OpenFlow13', listenPort=6683, mac='00:00:00:00:00:0d' )
    s14 = net.addSwitch( 's14', protocols='OpenFlow13', listenPort=6684, mac='00:00:00:00:00:0e' )

    s15 = net.addSwitch( 's15', protocols='OpenFlow13', listenPort=6685, mac='00:00:00:00:00:0f' )
    s16 = net.addSwitch( 's16', protocols='OpenFlow13', listenPort=6686, mac='00:00:00:00:00:10' )
    s17 = net.addSwitch( 's17', protocols='OpenFlow13', listenPort=6687, mac='00:00:00:00:00:11' )
    s18 = net.addSwitch( 's18', protocols='OpenFlow13', listenPort=6688, mac='00:00:00:00:00:12' )
    s19 = net.addSwitch( 's19', protocols='OpenFlow13', listenPort=6689, mac='00:00:00:00:00:13' )
    s20 = net.addSwitch( 's20', protocols='OpenFlow13', listenPort=6690, mac='00:00:00:00:00:14' )
    s21 = net.addSwitch( 's21', protocols='OpenFlow13', listenPort=6691, mac='00:00:00:00:00:15' )

    c1 = net.addController( 'c1', controller=RemoteController, ip='192.168.56.101', port=6633 )
    c2 = net.addController( 'c2', controller=RemoteController, ip='192.168.56.102', port=6633 )
    c3 = net.addController( 'c3', controller=RemoteController, ip='192.168.56.103', port=6633 )

    print "*** Creating links"

    net.addLink(s1, s2, 1, 1)
    net.addLink(s1, s3, 2, 1)
    net.addLink(s2, s4, 2, 1)
    net.addLink(s2, s5, 3, 1)
    net.addLink(s3, s6, 2, 1)
    net.addLink(s3, s7, 3, 1)
 
    net.addLink(s8, s9, 1, 1)
    net.addLink(s8, s10, 2, 1)
    net.addLink(s9, s11, 2, 1)
    net.addLink(s9, s12, 3, 1)
    net.addLink(s10, s13, 2, 1)
    net.addLink(s10, s14, 3, 1)

    net.addLink(s15, s16, 1, 1)
    net.addLink(s15, s17, 2, 1)
    net.addLink(s16, s18, 2, 1)
    net.addLink(s16, s19, 3, 1)
    net.addLink(s17, s20, 2, 1)
    net.addLink(s17, s21, 3, 1)

    net.addLink(h1, s4, 0, 2)
    net.addLink(h2, s5, 0, 2)
    net.addLink(h3, s6, 0, 2)
    net.addLink(h4, s7, 0, 2)

    net.addLink(h5, s11, 0, 2)
    net.addLink(h6, s12, 0, 2)
    net.addLink(h7, s13, 0, 2)
    net.addLink(h8, s14, 0, 2)

    net.addLink(h9, s18, 0, 2)
    net.addLink(h10, s19, 0, 2)
    net.addLink(h11, s20, 0, 2)
    net.addLink(h12, s21, 0, 2)


    print "*** Starting network"

    net.build()
    c1.start()
    c2.start()
    c3.start()

    s1.start( [c1] )
    s2.start( [c1] )
    s3.start( [c1] )
    s4.start( [c1] )
    s5.start( [c1] )
    s6.start( [c1] )
    s7.start( [c1] )

    s8.start( [c2] )
    s9.start( [c2] )
    s10.start( [c2] )
    s11.start( [c2] )
    s12.start( [c2] )
    s13.start( [c2] )
    s14.start( [c2] )

    s15.start( [c3] )
    s16.start( [c3] )
    s17.start( [c3] )
    s18.start( [c3] )
    s19.start( [c3] )
    s20.start( [c3] )
    s21.start( [c3] )

    s1.cmd('ovs-vsctl add-port s1 s1-ext1 -- set interface s1-ext1 type=patch options:peer=s8-ext1')
    s1.cmd('ovs-vsctl add-port s1 s1-ext3 -- set interface s1-ext3 type=patch options:peer=s15-ext3')
    s8.cmd('ovs-vsctl add-port s8 s8-ext1 -- set interface s8-ext1 type=patch options:peer=s1-ext1')
    s8.cmd('ovs-vsctl add-port s8 s8-ext2 -- set interface s8-ext2 type=patch options:peer=s15-ext2')
    s15.cmd('ovs-vsctl add-port s15 s15-ext2 -- set interface s15-ext2 type=patch options:peer=s8-ext2')
    s15.cmd('ovs-vsctl add-port s15 s15-ext3 -- set interface s15-ext3 type=patch options:peer=s1-ext3')

    s1.cmdPrint('ovs-vsctl show')

    h1.cmdPrint('ping 192.168.3.12 -c 1')
    h2.cmdPrint('ping 192.168.3.12 -c 1')
    h3.cmdPrint('ping 192.168.3.12 -c 1')
    h4.cmdPrint('ping 192.168.3.12 -c 1')
    h5.cmdPrint('ping 192.168.3.12 -c 1')
    h6.cmdPrint('ping 192.168.3.12 -c 1')
    h7.cmdPrint('ping 192.168.3.12 -c 1')
    h8.cmdPrint('ping 192.168.3.12 -c 1')
    h9.cmdPrint('ping 192.168.3.12 -c 1')
    h10.cmdPrint('ping 192.168.3.12 -c 1')
    h11.cmdPrint('ping 192.168.3.12 -c 1')
    h12.cmdPrint('ping 192.168.3.1 -c 1')


    print "*** Running CLI"
    CLI( net )

    print "*** Stopping network"
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )

    topology()







