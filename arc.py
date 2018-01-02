# Generate SQLite Tile Archive for Osmdroid
#
# See org.osmdroid.tileprovider.modules.DatabaseFileArchive
#

import os
from os import path
import sys
import sqlite3

if len(sys.argv) != 4:
	print( "invalid args." )
	print( "usage: arc.py [TGT_DIR] [PROVIDER] [ARC_NAME.sqlite]" )
	exit(1)

TGT_DIR = sys.argv[1]
PROVIDER = sys.argv[2]
ARCHIVE = sys.argv[3]

# Basic info
print( "Directory   : " + TGT_DIR )
print( "Provider    : " + PROVIDER )
print( "Archive     : " + ARCHIVE )
print( "" )

# Create archive file
db = sqlite3.connect( ARCHIVE )
db.execute("PRAGMA page_size = 1024;")	# 왜 필요할까?
db.execute('''
CREATE TABLE tiles (
	key INTEGER PRIMARY KEY,
	provider TEXT,
	tile BLOB)
''')

# Key Gen Func
def make_key( z, x, y ):
	return ((z << z) + x << z) + y

# Add tiles to archive
zl = [ d for d in os.listdir( TGT_DIR ) if path.isdir(path.join(TGT_DIR,d)) ]
print( "Zoom Levels : " + ", ".join(zl) )
print( "" )

for z in zl:
	print( "Processing zoom level " + z )
	z_dir = path.join(TGT_DIR,z)
	xl = [ d for d in os.listdir(z_dir) if path.isdir(path.join(z_dir,d)) ]

	for x in xl:
		x_dir = path.join(z_dir,x)
		yl = [ f for f in os.listdir(x_dir) if path.isfile(path.join(x_dir,f)) ]

		for tilefile in yl:
			y, ext = path.splitext(tilefile)
			print("  (z,x,y) = (%s,%s,%s)" % (z,x,y), end = "" )
			key = make_key(int(z),int(x),int(y))
			tilepath = path.join(x_dir,tilefile)
			print( "  key = %d  file = %s" % (key,tilepath), end = "" )

			with open(tilepath, 'rb') as tile:
				tileblob = tile.read()
			db.execute('INSERT INTO tiles VALUES(?,?,?)',
				(key, PROVIDER, sqlite3.Binary(tileblob)) )
			db.commit()
			print(" ... done.")

	print( "Zoom level " + z + " complete." )
	print( "" )

db.close()
print( "complete." )
