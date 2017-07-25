package net.floodlightcontroller.reactive;

import org.projectfloodlight.openflow.types.DatapathId;
import org.projectfloodlight.openflow.types.EthType;
import org.projectfloodlight.openflow.types.IPv4Address;
import org.projectfloodlight.openflow.types.IpProtocol;
import org.projectfloodlight.openflow.types.MacAddress;
import org.projectfloodlight.openflow.types.OFBufferId;
import org.projectfloodlight.openflow.types.OFPort;
import org.projectfloodlight.openflow.types.TransportPort;
import org.projectfloodlight.openflow.types.U64;

public class FlowMap {
	MacAddress eth_src, eth_dst;
	IPv4Address ipv4_src, ipv4_dst;
	IpProtocol ip_proto;
	TransportPort tp_src, tp_dst;
	EthType eth_type;
	OFPort out_port, in_port;
	U64 cookie;
	Integer priority, idle_timeout, hard_timeout;
	DatapathId DPID;
	OFBufferId buffer;
	
	
	String name, active, hibrido;

	public MacAddress getEth_src() {
		return eth_src;
	}

	public void setEth_src(String eth_src) {
		this.eth_src = MacAddress.of(eth_src);
	}

	public MacAddress getEth_dst() {
		return eth_dst;
	}

	public void setEth_dst(String eth_dst) {
		this.eth_dst = MacAddress.of(eth_dst);
	}

	public String getHibrido() {
		return hibrido;
	}

	public void setHibrido(String hibrido) {
		this.hibrido = hibrido;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getActive() {
		return active;
	}

	public void setActive(String active) {
		this.active = active;
	}

	public Integer getIdle_timeout() {
		return idle_timeout;
	}

	public void setIdle_timeout(String idle_timeout) {
		this.idle_timeout = Integer.valueOf(idle_timeout);
	}

	public Integer getHard_timeout() {
		return hard_timeout;
	}

	public void setHard_timeout(String hard_timeout) {
		this.hard_timeout = Integer.valueOf(hard_timeout);
	}

	public Integer getPriority() {
		return priority;
	}

	public void setPriority(String priority) {
		this.priority = Integer.valueOf(priority);
	}

	public U64 getCookie() {
		return cookie;
	}

	public void setCookie(String cookie) {
		this.cookie = U64.parseHex(cookie);
	}

	public EthType getEth_type() {
		return eth_type;
	}

	public void setEth_type(String eth_type) {
		this.eth_type = EthType.of(Integer.decode(eth_type));
	}

	public IpProtocol getIp_proto() {
		return ip_proto;
	}

	public void setIp_proto(String ip_proto) {
		this.ip_proto = IpProtocol.of(Short.valueOf(ip_proto));
	}

	public TransportPort getTp_src() {
		return tp_src;
	}

	public void setTp_src(String tp_src) {
		this.tp_src = TransportPort.of(Integer.valueOf(tp_src));
	}

	public TransportPort getTp_dst() {
		return tp_dst;
	}

	public void setTp_dst(String tp_dst) {
		this.tp_dst = TransportPort.of(Integer.valueOf(tp_dst));
	}

	public IPv4Address getIpv4_src() {
		return ipv4_src;
	}

	public void setIpv4_src(String ipv4_src) {
		this.ipv4_src = IPv4Address.of(ipv4_src);
	}

	public IPv4Address getIpv4_dst() {
		return ipv4_dst;
	}

	public void setIpv4_dst(String ipv4_dst) {
		this.ipv4_dst = IPv4Address.of(ipv4_dst);
	}

	public DatapathId getDPID() {
		return DPID;
	}

	public void setDPID(String dPID) {
		if(!dPID.contains(":")){
			String dpid = "";
			for(int i=0; i < 6; i++){
				String temp = dPID.substring(14 - 2*i, 16 - 2*i);
				dpid = ":" + temp + dpid;
			}
			dpid = dPID.substring(0, 2) + dpid;
			dPID = dpid;
		}
		DPID = DatapathId.of(dPID);
	}

	public OFPort getOut_port() {
		return out_port;
	}

	public void setOut_port(String out_port) {
		this.out_port = OFPort.of(Integer.valueOf(out_port));
	}

	public OFPort getIn_port() {
		return in_port;
	}

	public void setIn_port(String in_port) {
		this.in_port = OFPort.of(Integer.valueOf(in_port));
	}
	
	public OFBufferId getBuffer() {
		return buffer;
	}

	public void setBuffer(OFBufferId buffer) {
		this.buffer = buffer;
	}

}