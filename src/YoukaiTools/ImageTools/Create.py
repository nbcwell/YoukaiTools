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

#This file contains functions that create new images either from simple
#parameters, or from simple modifications to given input images

#if channels = none, initialcolor is a full array of the base color
#if channels = some int, then channels is the number of channels,
#and initial color is ust some single value
#If indata != None, then it just uses that as the full data. If channels is
#set, it uses that as channel num, else it tried to calculate it
def newImage(width, height, initialcolor=[0, 0, 0], channels=None, indata=None):
    if indata != None:
        c = channels
        if channels is None:
            c = len(indata[0])
        return [width, height, c] + indata
    if channels is None: 
        ic = initialcolor
        number_channels = len(initialcolor)
    else:
        ic = [initialcolor]*channels
        number_channels = channels
    head = [width, height, number_channels]
    body = []
    for i in xrange(width*height):
        body += [ic[:]]
    return head + body
