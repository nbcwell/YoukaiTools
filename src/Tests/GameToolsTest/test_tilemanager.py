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

from YoukaiTools import GameTools






tiles = [[1, 3, 5, 3, 2, 5, 6, 1],
         [1, 3, 5, 3, 2, 5, 6, 1],
         [1, 3, 5, 3, 2, 5, 6, 1],
         [1, 3, 5, 3, 2, 5, 6, 1],
         [1, 3, 5, 3, 2, 5, 6, 1],
         [1, 3, 5, 3, 2, 5, 6, 1],
         [1, 3, 5, 3, 2, 5, 6, 1],
         [1, 3, 5, 3, 2, 5, 6, 1]]

cam = GameTools.Camera2D((1.2, 2.3, 5.1, 6.3), (100, 100))

tm = GameTools.TileManager(cam, 8, 8, tiles)

print(tm.getShownTiles())
cam.zoom(2)
print(tm.getShownTiles())

ss = GameTools.SpriteSheet((8, 0, 0, 8), (8, 0, 0, 8), 20)
print(ss.getSprite(3))
print(ss.getSprite(9))
print(ss.getSprite(19))
print(ss.getSpriteFromCache(3))
print(ss.getSpriteFromCache(9))
print(ss.getSpriteFromCache(19))

