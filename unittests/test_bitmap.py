import imp_unittest, unittest
import wtc
import wx
import os

pngFile = os.path.join(os.path.dirname(__file__), 'toucan.png')

#---------------------------------------------------------------------------

class BitmapTests(wtc.WidgetTestCase):
    
    def test_BitmapCtors(self):
        b1 = wx.Bitmap()
        self.assertTrue( not b1.IsOk() )
        b2 = wx.Bitmap(5, 10, 32)
        self.assertTrue( b2.IsOk() )
        b3 = wx.Bitmap(wx.Size(5,10), 32)
        self.assertTrue( b3.IsOk() )
        b4 = wx.Bitmap((5,10), 32)
        self.assertTrue( b4.IsOk() )
        b5 = wx.Bitmap(pngFile)
        self.assertTrue( b5.IsOk() )
        img = wx.Image(pngFile)
        b6 = wx.Bitmap(img)
        self.assertTrue( b6.IsOk() )
        
        
    def test_Bitmap__nonzero__(self):
        b1 = wx.Bitmap()
        self.assertTrue( not b1.IsOk() )
        b2 = wx.Bitmap(5, 10, 24)
        self.assertTrue( b2.IsOk() )
        self.assertTrue( b2.__nonzero__() == b2.IsOk() )

        # check that the __nonzero__ method can be used with if satements
        nzcheck = False
        if b2:
            nzcheck = True
        self.assertTrue(nzcheck)
        nzcheck = False
        if not b1:
            nzcheck = True
        self.assertTrue(nzcheck)

        
    def test_BitmapNullBitmap(self):
        # just make sure this one exists
        wx.NullBitmap
        self.assertTrue(not wx.NullBitmap.IsOk())

        
    def test_BitmapSetMaskColour(self):
        b5 = wx.Bitmap(pngFile)
        b5.SetMaskColour(wx.Colour(1,2,3))
        b5.SetMaskColour('black')
        
        
    def test_BitmapMask(self):
        b5 = wx.Bitmap(pngFile)
        m = wx.Mask()
        m = wx.Mask(b5, 4)
        m = wx.Mask(b5)
        m = wx.Mask(b5, wx.Colour(1,2,3))
                    
        
#---------------------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()