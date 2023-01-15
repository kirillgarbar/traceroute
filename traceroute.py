import select
import socket
import struct
import argparse
from utils import calculate_checksum


def ping(destination_address, icmp_socket, ttl):
    # Creating icmp message
    initial_checksum = 0
    # Header is type(8), code(0), checksum, id(ttl), sequence number(1)
    initial_header = struct.pack("bbHHh", 8, 0, initial_checksum, ttl, 1)

    calculated_checksum = calculate_checksum(initial_header)
    header = struct.pack("bbHHh", 8, 0, calculated_checksum, ttl, 1)

    # Sending icmp message
    icmp_socket.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, ttl)
    icmp_socket.sendto(header, (destination_address, 1))

    # Checking for timeout
    socketResponseReady = select.select([icmp_socket], [], [], 5)

    if socketResponseReady[0] == []:
        print(f'Hop {ttl}: Unknown (timeout)')
        return False

    # Message received
    recv_packet, addr = icmp_socket.recvfrom(1024)

    print(f'Hop {ttl}: {addr[0]}')

    if addr[0] == destination_address:
        return True

    return False


def main(dst):

    destination_address = socket.gethostbyname(dst)
    icmp_proto = socket.getprotobyname("icmp")
    print(f"Tracing to {destination_address}")

    ttl = 1
    while(ttl < 30):
        icmp_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp_proto)

        if (ping(destination_address, icmp_socket, ttl)):
            icmp_socket.close()
            break

        ttl += 1
        icmp_socket.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dst")
    args = parser.parse_args()

    main(args.dst)