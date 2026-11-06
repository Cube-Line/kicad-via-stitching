# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class FillAreaDialog
###########################################################################

class FillAreaDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"过孔缝合参数", pos = wx.DefaultPosition, size = wx.Size( 402,590 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"过孔铜径 (mm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		fgSizer1.Add( self.m_staticText3, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_SizeMM = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_SizeMM.SetMinSize( wx.Size( 1000,-1 ) )

		fgSizer1.Add( self.m_SizeMM, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"过孔钻孔 (mm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		fgSizer1.Add( self.m_staticText9, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_DrillMM = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_DrillMM, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"过孔安全间距 (mm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		fgSizer1.Add( self.m_staticText5, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_ClearanceMM = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_ClearanceMM, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"过孔网格间距 (mm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.m_StepMM = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_StepMM, 1, wx.ALL|wx.EXPAND, 5 )


		fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_bitmapStitching = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_bitmapStitching, 0, wx.EXPAND, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"网络名称", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		fgSizer1.Add( self.m_staticText6, 1, wx.ALL|wx.EXPAND, 5 )

		m_cbNetChoices = []
		self.m_cbNet = wx.ComboBox( self, wx.ID_ANY, u"GND", wx.DefaultPosition, wx.DefaultSize, m_cbNetChoices, wx.CB_READONLY )
		fgSizer1.Add( self.m_cbNet, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText42 = wx.StaticText( self, wx.ID_ANY, u"排列方式", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )

		fgSizer1.Add( self.m_staticText42, 0, wx.ALL, 5 )

		m_cbFillTypeChoices = [ u"同心圆", u"沿轮廓", u"沿轮廓（无孔）", u"矩形", u"星形" ]
		self.m_cbFillType = wx.ComboBox( self, wx.ID_ANY, u"矩形", wx.DefaultPosition, wx.DefaultSize, m_cbFillTypeChoices, wx.CB_READONLY )
		self.m_cbFillType.SetSelection( 3 )
		fgSizer1.Add( self.m_cbFillType, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"随机偏移", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		fgSizer1.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.m_Random = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_Random, 0, wx.ALL, 5 )

		self.m_staticText81 = wx.StaticText( self, wx.ID_ANY, u"仅在选中的铺铜区内", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )

		fgSizer1.Add( self.m_staticText81, 0, wx.ALL, 5 )

		self.m_only_selected = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_only_selected, 0, wx.ALL, 5 )

		self.m_staticText71 = wx.StaticText( self, wx.ID_ANY, u"忽略其他层的区域", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )

		fgSizer1.Add( self.m_staticText71, 0, wx.ALL, 5 )

		self.m_viaThroughAreas = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_viaThroughAreas, 0, wx.ALL, 5 )

		self.m_staticText72 = wx.StaticText( self, wx.ID_ANY, u"同网络走线上也放置", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText72.Wrap( -1 )

		fgSizer1.Add( self.m_staticText72, 0, wx.ALL, 5 )

		self.m_sameNetTracks = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_sameNetTracks, 0, wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"调试模式", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		fgSizer1.Add( self.m_staticText7, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_Debug = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_Debug, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( fgSizer1, 1, wx.EXPAND, 5 )

		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		bSizer1.Add( self.m_staticText101, 1, wx.ALL, 5 )

		self.m_button1 = wx.Button( self, wx.ID_OK, u"运行", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button1.SetDefault()
		bSizer1.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_CANCEL, u"取消", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button2, 0, wx.ALL, 5 )

		self.m_button3_delete = wx.Button( self, wx.ID_DELETE, u"删除过孔", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button3_delete, 0, wx.ALL, 5 )


		bSizer3.Add( bSizer1, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button3_delete.Bind( wx.EVT_BUTTON, self.onDeleteClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def onDeleteClick( self, event ):
		event.Skip()


