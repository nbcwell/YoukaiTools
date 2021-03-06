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

class BaseChip:
    def __init__(self):
        return
    
    #The derived class should call this
    def setup(self, inputs, outputs):
        self.bnuminputs = len(inputs)
        self.binputstoset = self.bnuminputs
        self.inputs = {}
        self.input_set = {}
        for x in inputs:
            self.inputs[x] = 0
            self.input_set[x] = False
        
        self.outputs = {}
        for x in outputs:
            self.outputs[x] = 0
        self.output_set = False
        return
    
    def reset(self):
        for k in self.inputs:
            self.input_set[k] = False
        self.binputstoset = self.bnuminputs
        self.output_set = False
        return
    
    def getInputList(self):
        return self.inputs.keys()
    
    def getOutputList(self):
        return self.outputs.keys()
    
    def setInput(self, name, value):
        self.inputs[name] = value
        if not self.input_set[name]:
            self.input_set[name] = True
            self.binputstoset -= 1
        self.output_set = False
        return
    
    def getOutput(self, name):
        return self.outputs[name]
    
    def needsCalc(self):
        if self.output_set:
            return False
        inp = self.binputstoset == 0
        return inp
    
    def calculate(self):
        if not self.needsCalc():
            return False
        self.doCalculation()
        self.output_set = True
        for k in self.inputs:
            self.input_set[k] = False
        self.binputstoset = self.bnuminputs
        return True
    
    #override this. This is where the magic happens.
    #Take the values in inputs, and work the magic on them
    def doCalculation(self):
        return
    