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

import YoukaiTools.AdvMath
from YoukaiTools.AdvMath import Intersect as Intersect
import unittest

class TestRect(unittest.TestCase):
    def test_rectXRect(self):
        testc = ( (([10, 10, 20, 20], [15, 12, 22, 24], False),True), (([8, 14, 3, 7], [16, 18, 5, 10], False),False), (([0, 2, 0, 2], [2, 4, 0, 2], False),False), (([1, 2, 3, 4], [2, 3, 5, 6], True),(True,(2,3,3,4))) )
        for c in testc:
            self.assertEquals(Intersect.rectxRect(*c[0]), c[1])
        return
        
if __name__ == '__main__':
    unittest.main()
    