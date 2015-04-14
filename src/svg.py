#!/usr/bin/python

def singleton(class_):
  instances = {}
  def getinstance(*args, **kwargs):
    if class_ not in instances:
        instances[class_] = class_(*args, **kwargs)
    return instances[class_]
  return getinstance

@singleton
class SVG:
    def __init__(self):
        self.svg = None

    def getSvg(self):
        return self.svg

    def setSvg(self, svg):
        self.svg = svg