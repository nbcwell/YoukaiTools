#Copyright (c) <2011> <Nathaniel Caldwell>

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

from YoukaiTools import ImageTools
from YoukaiTools.ImageTools.FileHandlers import All
from .. import Interpolation
from .. import Ranges

def makeDefaultSettings():
    s = {}
    s["markmin"] = False
    s["markmax"] = False
    s["markpoints"] = False
    s["pointcolor"] = (1.0, 0.0, 0.0)
    s["mincolor"] = (.8, .1, .1)
    s["maxcolor"] = (.1, .8, .1)
    s["color"] = (.1, .1, .8)
    s["interpolation"] = Interpolation.linear
    s["tension"] = 0
    s["bias"] = 0
    s["size"] = (800, 600)
    s["domain"] = (None, None)
    s["backgroundcolor"] = (1.0, 1.0, 1.0)
    s["marktopheight"] = 3
    s["markbottomheight"] = 3
    return s

def saveDataGraph1DFile(filename, dg, settings=None):
    fn = All.getFormatName(filename)
    f = open(filename, "w")
    saveDataGraph1D(f, dg, fn, settings)
    f.close()
    return

def saveDataGraph1D(f, dg, format = "png", settings=None):
    usettings = settings
    if settings is None:
        usettings = makeDefaultSettings()
    im = ImageTools.Create.newImage(usettings["size"][0], usettings["size"][1] + usettings["marktopheight"] + usettings["markbottomheight"], usettings["backgroundcolor"])
    max = float('-inf')
    min = float('inf')
    vals = []
    domain = dg.fdomain
    if usettings["domain"] is not None:
        if usettings["domain"][0] is None:
            dmin = dg.fdomain[0]
        else:
            dmin = usettings["domain"][0]
        if usettings["domain"][1] is None:
            dmax = dg.fdomain[1]
        else:
            dmax = usettings["domain"][1]
        domain = (dmin, dmax)
    dt = (float(domain[1])-float(domain[0])) / float(usettings["size"][0])
    for x in range(usettings["size"][0]):
        herex = x*dt + domain[0]
        y = dg.getValue(herex, usettings["interpolation"], usettings["tension"], usettings["bias"])
        vals.append(y)
        if y > max: max = y
        if y < min: min = y
    lastval = None
    for i, y in enumerate(vals):
        herey = __getImageY(y, usettings["size"][1], min, max) + usettings["marktopheight"]
        #print(herex, herey)
        if lastval is not None:
            ImageTools.Modify.drawLine(im, i-1, lastval, i, herey, usettings["color"])
        lastval = herey
    for mi in dg.minima:
        m = dg.xvalues[int(mi)]
        if m >= domain[0] and m <= domain[1]:
            i = int(Ranges.rangeToRange(float(m), domain[0], domain[1], 0.0, float(usettings["size"][0]-1)))
            y = vals[i]
            herey = __getImageY(y, usettings["size"][1], min, max) + usettings["marktopheight"]
            ImageTools.Modify.drawLine(im, i, herey-usettings["marktopheight"], i, herey+usettings["marktopheight"], usettings["maxcolor"])
    for mi in dg.maxima:
        m = dg.xvalues[int(mi)]
        if m >= domain[0] and m <= domain[1]:
            i = int(Ranges.rangeToRange(float(m), domain[0], domain[1], 0.0, float(usettings["size"][0]-1)))
            y = vals[i]
            herey = __getImageY(y, usettings["size"][1], min, max) + usettings["marktopheight"]
            ImageTools.Modify.drawLine(im, i, herey-usettings["marktopheight"], i, herey+usettings["marktopheight"], usettings["maxcolor"])
    if usettings["markpoints"]:
        for m in dg.xvalues:
            if m >= domain[0] and m <= domain[1]:
                i = int(Ranges.rangeToRange(float(m), domain[0], domain[1], 0.0, float(usettings["size"][0]-1)))
                y = vals[i]
                herey = __getImageY(y, usettings["size"][1], min, max) + usettings["marktopheight"]
                ImageTools.Modify.drawBox(im, int(i-1), int(herey-1), int(2), int(2), usettings["pointcolor"])
    All.save(f, im, format)
    return

def __getImageY(val, height, min, max):
    return int(Ranges.rangeToRange(val, min, max, float(height)-1.0, 0.0))
