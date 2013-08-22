#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import glob

class SearchAndChange:
	def __init__(self):
		if len(sys.argv) != 3:
			print ("Musíte zadat argumenty: searchandchange [co] [čím]")
			sys.exit(1)
		
		co = sys.argv[1]
		cim = sys.argv[2]
		
		seznam = glob.glob("*")
		seznam = self.filter(seznam)
		for item in seznam:
			fr = open(item, "r")
			text = fr.read()
			fr.close()
			if text.find(co) != -1:
				fw = open(item, "w")
				wtext = text.replace(co, cim)
				print "  Měním soubor %s" % item
				fw.write(wtext)
				fw.close()

	def filter(self, seznam):
		new_list = []
		for item in seznam:
			if item[-4:] == ".xpm":
				new_list.append(item)
		return new_list

if __name__ == "__main__":
	sach = SearchAndChange()
