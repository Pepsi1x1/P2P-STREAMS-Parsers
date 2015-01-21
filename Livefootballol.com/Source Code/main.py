# -*- coding: utf-8 -*-

""" P2P-STREAMS XBMC ADDON

Livefootballol.com module parser

"""
import sys,os
current_dir = os.path.dirname(os.path.realpath(__file__))
basename = os.path.basename(current_dir)
core_dir =  current_dir.replace(basename,'').replace('parsers','')
sys.path.append(core_dir)
from peertopeerutils.webutils import *
from peertopeerutils.pluginxbmc import *
from peertopeerutils.directoryhandle import *
import acestream as ace
import sopcast as sop

base_url = "http://www.livefootballol.com/live-football-streaming.html"

def module_tree(name,url,iconimage,mode,parser,parserfunction):
	if not parserfunction: livefootballol_main()
    
def livefootballol_main():
	try:
		source = abrir_url(base_url)
	except: source="";xbmcgui.Dialog().ok(translate(40000),translate(40128))
	if source:
		match = re.compile('<div>\n<img src="(.+?)".+?\n<span class="RED">(.+?)<.+?\n(.+?)\n<a href="(.+?)">(.+?)</a>').findall(source)
		for iconurl,time,league,link,fixture in match:
			addDir("[COLOR red]["+time +"][/COLOR][COLOR orange]"+league+"[/COLOR][B][COLOR white]("+fixture+")[/COLOR][/B]",base_url+link,401,iconurl,len(match),True)