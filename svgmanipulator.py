#!/usr/bin/python

from lxml import etree

class svgCreator:

    x = 0
    y = 150
    use_number = 1
    x_trans = 1800

    def compute_x_of_symbol(self):
        self.x += 150
        return str(self.x)

    def compute_y_of_symbol(self):
        return str(self.y)

    def assign_group(self, name):
        if "VAC" in name:
            return "VAC"
        elif "DIA" in name:
            return "DIA"
        elif "RF" in name:
            return "RF"
        elif "MAG" in name:
            return "MAG"
        else:
            return "DIA"

    def compute_translate_values(self):
        y_trans  = 3435
        ret = "translate(" + str(self.x_trans) + "," + str(y_trans) + ")"
        self.x_trans += 50
        return ret

    def add_device(self, device, group):
        deviceElement = etree.SubElement(group, "use")
        deviceElement.attrib["id"] = "use" + str(self.use_number)
        deviceElement.attrib["{http://www.w3.org/1999/xlink}href"] = "#" + device[3]
        deviceElement.attrib["x"] = "0"
        deviceElement.attrib["y"] = "0"
        deviceElement.attrib["width"] = "17000"
        deviceElement.attrib["height"] = "10000"
        deviceElement.attrib["transform"] = self.compute_translate_values()

        print etree.tostring(group) + "\n\n"

        #self.add_text_label(device, )
        self.use_number += 1



    def parse_devices(self, devices):

        # sorting by x-coordinate
        devices = sorted(devices, key=lambda devices: devices[1])

        for device in devices:
            name = device[0]
            x = device[1]
            y = device[2]
            icon = device[3]
            group_name = self.assign_group(name)

            print "Name=" + name + ", icon=" + icon + ", x=" + str(x) + ", group=" + group_name

            group_node = None
            for group in self.svgRoot[3]:
                if group.attrib["{http://www.inkscape.org/namespaces/inkscape}label"] == group_name:
                    group_node = group
                    break

            zoom_node = None
            for group in group_node:
                if group.attrib["{http://www.inkscape.org/namespaces/inkscape}label"] == "zoom2":
                    zoom_node = group

            self.add_device(device, zoom_node)



    def run(self):
        blankSVGpath = './blank2.svg'
        #devicesAndIconsPath = "/home/maciej/prog/synchrotron/GuiIconDrawer/devicesandicons.xml"
        #iconsDirPath = "/home/maciej/Pobrane/kits-maxiv-app-maxiv-linacsynoptic/linacsynoptic/images/icons/"

        devicesAndIconsPath = "/home/Operator/workspace/GuiIconDrawer/devicesandicons.xml"
        iconsDirPath = "/home/Operator/workspace/GuiIconDrawer/resources/"

        svgTree = etree.parse(blankSVGpath)
        self.svgRoot = svgTree.getroot()

        print "SVG file loaded "
        symbols = None
        for group in self.svgRoot[3]:
            if group.attrib["id"] == "symbols":
                symbols = group
                break
        print "Found group " + str(symbols.attrib["id"])


        devicesTree = etree.parse(devicesAndIconsPath)
        print("XML DevicesAndIcons loaded")
        devicesRoot = devicesTree.getroot()
        symbolsDict = {}

        for device in devicesRoot:
            print "########################################"
            deviceName = device.find("deviceName").text
            pictureFile = device.find("pictureFile").text
            symbolsDict[deviceName] = pictureFile
            print "Device name=" + deviceName + ", pictureFile=" + pictureFile


        for picture in symbolsDict.values():
            print picture
            gElement = etree.SubElement(symbols, "g")
            gElement.attrib["style"] = "display:inline"
            gElement.attrib["id"] = picture
            #gElement.attrib["transform"] = "translate(746.99999,-227.99999)"

            imgElement = etree.SubElement(gElement, "image")
            imgElement.attrib["{http://www.w3.org/1999/xlink}href"] = iconsDirPath + picture + ".svg"
            imgElement.attrib["id"] = "11"
            imgElement.attrib["x"] = self.compute_x_of_symbol()
            imgElement.attrib["y"] = self.compute_y_of_symbol()
            imgElement.attrib["width"] = "30"
            imgElement.attrib["height"] = "30"
            print etree.tostring(symbols)

        # fakeDevices = [
        #     ["sys/MAG/1", 330, 13, "symbol-solenoid"],
        #     ["sys/tg_test/2", 400, 12, "symbol-quadrupole"],
        #     ["sys/VAC/3", 150, 53, "symbol-quadrupole"],
        #     ["sys/tg_test/4", 250, 88, "symbol-dipole"],
        # ]

        fakeDevices = [
            ["sys/MAG/1", 330, 13, "test123"],
            ["sys/tg_test/2", 400, 12, "icon123"],
            ["sys/VAC/3", 150, 53, "test123"],
            ["sys/tg_test/4", 250, 88, "icon123"],
        ]

        self.parse_devices(fakeDevices)

        toWrite = etree.tostring(self.svgRoot, pretty_print=True)
        fd = open("new.svg", 'w')
        fd.write(toWrite)


svgC = svgCreator()
svgC.run()