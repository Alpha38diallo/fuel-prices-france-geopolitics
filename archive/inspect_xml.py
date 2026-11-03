import xml.etree.ElementTree as ET

file_path = "data/raw/PrixCarburants_annuel_2021.xml"

context = ET.iterparse(file_path, events=("start",))

count = 0

for event, elem in context:
    print(elem.tag, elem.attrib)
    count += 1

    if count >= 20:
        break