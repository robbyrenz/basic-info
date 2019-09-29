import requests


def main():
    header()
    # make a GET request to an API
    info = requests.get("http://ifconfig.co/json")
    info = info.json()

    # extracting all the info
    ip_address = info['ip']
    country = info['country']
    city = info['city']
    lat = info['latitude']
    lon = info['longitude']
    isp = info['asn_org']

    # print the relevant info in a formatted output
    print_info(ip_address, country, city, lat, lon, isp)


def header():
    print()
    print("---------------------------------------------")
    print("        Information About Your Computer")
    print("---------------------------------------------")
    print()


def print_info(ip, country, city, lat, lon, isp):
    print(f"Your public IP address is: {ip}")
    print(f"You are in {city}, {country}")
    print(f"Exact coordinates (latitude, longitude): ({lat}, {lon})")
    print(f"Your internet service provider is {isp}")
    print()


if __name__ == "__main__":
    main()
