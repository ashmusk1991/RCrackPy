#!/usr/bin/env python

import RainbowCrack

tables = "/media/data/RainbowTables/MD5/"
md5_hash = "af5b3d17aa1e2ff2a0f83142d692d701"

print "[*] Cracking hashes, please wait..."
results = RainbowCrack.single_hash(md5_hash, tables, maxThreads = 4)
print "Got:", results
