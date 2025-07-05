import xml.etree.ElementTree as ET

def extract_coordinates_from_kml(kml_content):
    """
    Extracts names and coordinates from KML content.

    Args:
        kml_content (str): A string containing the KML data.

    Returns:
        list: A list of dictionaries, where each dictionary has
              'name' and 'coordinates' keys.
              Returns an empty list if parsing fails or no data is found.
    """
    extracted_data = []
    try:
        # The KML file has a default namespace, which needs to be handled.
        # We can register it or find elements using the full namespace URI.
        # For simplicity in finding, we'll remove the namespace from tags if possible,
        # or use it explicitly.
        # A common way to handle namespaces is to find them first.
        # However, for this specific structure, we can directly search for tags.

        # Removing default namespace for easier parsing if it exists
        # This is a common trick but might not be robust for all XMLs.
        # A more robust way is to use namespace maps.
        kml_content = kml_content.replace(' xmlns="http://www.opengis.net/kml/2.2"', '', 1)
        kml_content = kml_content.replace(' xmlns:gx="http://www.google.com/kml/ext/2.2"', '', 1)
        kml_content = kml_content.replace(' xmlns:kml="http://www.opengis.net/kml/2.2"', '', 1)
        kml_content = kml_content.replace(' xmlns:atom="http://www.w3.org/2005/Atom"', '', 1)

        root = ET.fromstring(kml_content)

        # KML documents often have a 'Document' root element,
        # and Placemarks can be inside a 'Folder' or directly under 'Document'.
        # We will search for 'Placemark' elements anywhere in the document.
        for placemark in root.findall('.//Placemark'):
            name_element = placemark.find('name')
            point_element = placemark.find('Point') # Coordinates are inside Point

            if name_element is not None and point_element is not None:
                name = name_element.text.strip() if name_element.text else "N/A"
                
                coordinates_element = point_element.find('coordinates')
                if coordinates_element is not None and coordinates_element.text:
                    coordinates = coordinates_element.text.strip()
                    extracted_data.append({'name': name, 'coordinates': coordinates})
                else:
                    # Handle cases where coordinates might be missing within a Point
                    extracted_data.append({'name': name, 'coordinates': "Coordinates not found"})
            # else:
                # Optionally handle Placemarks that don't have a name or Point
                # print(f"Skipping Placemark without name or Point: {ET.tostring(placemark, encoding='unicode')}")


    except ET.ParseError as e:
        print(f"Error parsing KML: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

    return extracted_data

# The KML content from the uploaded file
kml_file_content = """
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
<Document>
	<name>InspectionPathNodes.kml</name>
	<Style id="IconStyle10">
		<IconStyle>
			<scale>0.75</scale>
			<Icon>
				<href>Layer1_Symbol_83228420_0.png</href>
			</Icon>
		</IconStyle>
		<LabelStyle>
			<color>ff000000</color>
			<scale>0.833333</scale>
		</LabelStyle>
		<PolyStyle>
			<color>ff000000</color>
			<outline>0</outline>
		</PolyStyle>
	</Style>
	<Style id="IconStyle11">
		<IconStyle>
			<scale>0.75</scale>
			<Icon>
				<href>Layer1_Symbol_83228888_0.png</href>
			</Icon>
		</IconStyle>
		<LabelStyle>
			<color>ff000000</color>
			<scale>0.833333</scale>
		</LabelStyle>
		<PolyStyle>
			<color>ff000000</color>
			<outline>0</outline>
		</PolyStyle>
	</Style>
	<Style id="IconStyle14">
		<IconStyle>
			<scale>0.75</scale>
			<Icon>
				<href>Layer1_Symbol_832279d8_0.png</href>
			</Icon>
		</IconStyle>
		<LabelStyle>
			<color>ff000000</color>
			<scale>0.833333</scale>
		</LabelStyle>
		<PolyStyle>
			<color>ff000000</color>
			<outline>0</outline>
		</PolyStyle>
	</Style>
	<Folder id="FeatureLayer1">
		<name>InspectionPathNodes</name>
		<Snippet maxLines="0"></Snippet>
		<Placemark id="ID_10000">
			<name>TL 05</name>
			<Snippet maxLines="0"></Snippet>
			<description><![CDATA[...]]></description>
			<styleUrl>#IconStyle10</styleUrl>
			<Point>
				<coordinates>-94.81597283894307,29.31551836064612,-27.46499999999651</coordinates>
			</Point>
		</Placemark>
		<Placemark id="ID_10001">
			<name>BEND 01</name>
			<Snippet maxLines="0"></Snippet>
			<description><![CDATA[...]]></description>
			<styleUrl>#IconStyle11</styleUrl>
			<Point>
				<coordinates>-94.8164793486261,29.31438920688152,0</coordinates>
			</Point>
		</Placemark>
		<Placemark id="ID_10002">
			<name>TL 03</name>
			<Snippet maxLines="0"></Snippet>
			<description><![CDATA[...]]></description>
			<styleUrl>#IconStyle10</styleUrl>
			<Point>
				<coordinates>-94.81717911736781,29.30786240294634,-26.99000000000524</coordinates>
			</Point>
		</Placemark>
		<Placemark id="ID_10003">
			<name>BEND 03</name>
			<Snippet maxLines="0"></Snippet>
			<description><![CDATA[...]]></description>
			<styleUrl>#IconStyle11</styleUrl>
			<Point>
				<coordinates>-94.81564172531924,29.3170487068911,0</coordinates>
			</Point>
		</Placemark>
		<Placemark id="ID_10004">
			<name>RED 02</name>
			<Snippet maxLines="0"></Snippet>
			<description><![CDATA[...]]></description>
			<styleUrl>#IconStyle14</styleUrl>
			<Point>
				<coordinates>-94.81625971503074,29.31434967067828,0</coordinates>
			</Point>
		</Placemark>
		<Placemark id="ID_10005">
			<name>TL 04</name>
			<Snippet maxLines="0"></Snippet>
			<description><![CDATA[...]]></description>
			<styleUrl>#IconStyle10</styleUrl>
			<Point>
				<coordinates>-94.81638801960614,29.31437279319067,-26.56299999999464</coordinates>
			</Point>
		</Placemark>
		<Placemark id="ID_10006">
			<name>TL 06 - EXT</name>
			<Snippet maxLines="0"></Snippet>
			<description><![CDATA[...]]></description>
			<styleUrl>#IconStyle10</styleUrl>
			<Point>
				<coordinates>-94.81657933740547,29.3182391411681,0</coordinates>
			</Point>
		</Placemark>
		<Placemark id="ID_10007">
			<name>RED 01</name>
			<Snippet maxLines="0"></Snippet>
			<description><![CDATA[...]]></description>
			<styleUrl>#IconStyle14</styleUrl>
			<Point>
				<coordinates>-94.81649421933736,29.31434120965462,0</coordinates>
			</Point>
		</Placemark>
		<Placemark id="ID_10008">
			<name>TL 04A</name>
			<Snippet maxLines="0"></Snippet>
			<description><![CDATA[...]]></description>
			<styleUrl>#IconStyle10</styleUrl>
			<Point>
				<coordinates>-94.81642674238479,29.31438005343917,-26.61000000000058</coordinates>
			</Point>
		</Placemark>
		<Placemark id="ID_10009">
			<name>TL 01 - INS</name>
			<Snippet maxLines="0"></Snippet>
			<description><![CDATA[...]]></description>
			<styleUrl>#IconStyle10</styleUrl>
			<Point>
				<coordinates>-94.81712726032143,29.30774255530421,-27.13300000000163</coordinates>
			</Point>
		</Placemark>
		<Placemark id="ID_10010">
			<name>TL 02</name>
			<Snippet maxLines="0"></Snippet>
			<description><![CDATA[...]]></description>
			<styleUrl>#IconStyle10</styleUrl>
			<Point>
				<coordinates>-94.81715924124386,29.3078201742485,-26.90099999999802</coordinates>
			</Point>
		</Placemark>
		<Placemark id="ID_10011">
			<name>BEND 02</name>
			<Snippet maxLines="0"></Snippet>
			<description><![CDATA[...]]></description>
			<styleUrl>#IconStyle11</styleUrl>
			<Point>
				<coordinates>-94.81621857398737,29.31434302373828,0</coordinates>
			</Point>
		</Placemark>
		<Placemark id="ID_10012">
			<name>BEND 04</name>
			<Snippet maxLines="0"></Snippet>
			<description><![CDATA[...]]></description>
			<styleUrl>#IconStyle11</styleUrl>
			<Point>
				<coordinates>-94.81542103710169,29.31710364567801,0</coordinates>
			</Point>
		</Placemark>
		<Placemark id="ID_10013">
			<name>BEND 05</name>
			<Snippet maxLines="0"></Snippet>
			<description><![CDATA[...]]></description>
			<styleUrl>#IconStyle11</styleUrl>
			<Point>
				<coordinates>-94.81583255982493,29.31837583363667,0</coordinates>
			</Point>
		</Placemark>
		<Placemark id="ID_10014">
			<name>OTL 01</name>
			<Snippet maxLines="0"></Snippet>
			<description><![CDATA[...]]></description>
			<styleUrl>#IconStyle10</styleUrl>
			<Point>
				<coordinates>-94.81557008377702,29.31706622298464,0</coordinates>
			</Point>
		</Placemark>
		<atom:link rel="app" href="https://www.google.com/earth/about/versions/#earth-pro" title="Google Earth Pro 7.3.6.10201"></atom:link>
	</Folder>
</Document>
</kml>
""" # Note: CDATA content is truncated for brevity in this example string

# How to use the function:
# 1. If your KML data is in a file:
# with open('InspectionPathNodes.txt', 'r', encoding='utf-8') as f:
#     kml_file_content = f.read()

# 2. Call the extraction function
extracted_data = extract_coordinates_from_kml(kml_file_content)

# 3. Print the results
if extracted_data:
    for item in extracted_data:
        print(f"Name: {item['name']}, Coordinates: {item['coordinates']}")
else:
    print("No data extracted or an error occurred.")

# Example of how to get the data into a CSV format string
if extracted_data:
    csv_output = "Name,Longitude,Latitude,Altitude\n" # CSV Header
    for item in extracted_data:
        name = item['name']
        # Coordinates are usually lon,lat,alt
        coords_parts = item['coordinates'].split(',')
        lon = coords_parts[0] if len(coords_parts) > 0 else ""
        lat = coords_parts[1] if len(coords_parts) > 1 else ""
        alt = coords_parts[2] if len(coords_parts) > 2 else "" # Altitude might not always be present
        csv_output += f"\"{name}\",{lon},{lat},{alt}\n"
    
    print("\nCSV formatted output:")
    print(csv_output)

    # To save to a CSV file:
    # with open('extracted_coordinates.csv', 'w', encoding='utf-8') as f_out:
    #     f_out.write(csv_output)
    # print("\nData saved to extracted_coordinates.csv")

