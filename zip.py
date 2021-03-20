from Samples.geocoder import geocode


def get_address_postal_code(address):
    toponym = geocode(address)
    postal_code = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["postal_code"]
    return postal_code


def main():
    address = ""
    postal_code = get_address_postal_code(address)
    print(f"{address} имеет индекс: {postal_code}")


if __name__ == "__main__":
    main()