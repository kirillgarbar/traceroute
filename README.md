# Traceroute

This is the homework implementation of traceroute for Linux

## Requirements

- Python 3 or later

## Usage
```
sudo python3 traceroute.py --dst <destination>
```

### Example

```
sudo python3 traceroute.py --dst pornhub.com
```

or

```
sudo python3 traceroute.py --dst 66.254.114.41
```

### Output

```
Tracing to 66.254.114.41
Hop 1: 172.22.64.1
Hop 2: 192.168.0.1
Hop 3: 217.197.4.1
Hop 4: 172.24.31.5
Hop 5: 172.24.25.32
Hop 6: 172.24.25.38
Hop 7: 195.70.196.3
Hop 8: 81.211.104.177
Hop 9: 79.104.225.15
Hop 10: 81.211.45.63
Hop 11: Unknown (timeout)
Hop 12: 195.89.119.221
Hop 13: 195.2.27.225
Hop 14: Unknown (timeout)
Hop 15: 149.29.8.2
Hop 16: 66.254.122.141
Hop 17: 66.254.114.41