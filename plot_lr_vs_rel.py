#===========================================================================
#
# plot_science.py
#
# Python script to query SWIRE_ES1 mysql database to 
# select from matches the IR Flux, Radio Flux, Redshift etc so we can do some science
#
#===========================================================================
#
# S. Weston
# AUT University
# Nov 2013
#===========================================================================

import math
import array
import _mysql
import numpy
import scipy
import matplotlib.pyplot as plt
import astropysics as astro
import pylab
import sys

# Database 
global db_host
db_host='localhost'
global db_user
db_user='atlas'
global db_passwd
db_passwd='atlas'

print "\nStarting Plot Science"

#   Connect to the local database with the atlas uid

db=_mysql.connect(host=db_host,user=db_user,passwd=db_passwd)

# select from matches the IR Flux, Radio Flux, Redshift etc so we can do some science

db.query("SELECT lr,reliability from atlas.elais_matches where reliability is not null;")
          
# store_result() returns the entire result set to the client immediately.
# The other is to use use_result(), which keeps the result set in the server 
#and sends it row-by-row when you fetch.

#r=db.store_result()
# ...or...
r=db.use_result()

# fetch results, returning char we need float !

rows=r.fetch_row(maxrows=10000)

# rows is a tuple, convert it to a list

reliability=[]
lr=[]

for row in rows:
#    print row
    reliability.append(float(row[1]))
    lr.append(float(row[0]))
	
	        	
#    End of do block

# Close connection to the database
db.close()

# Now plot the data

plt.yscale('log')
plt.xscale('log')
# plot(x,y,args)
plt.plot(lr,reliability,'k.')
#plot_title=field+'  ir_3_6/ir_4_5 vs ir_5_8/ir_8_0'
plt.title(' Likelihood Ratio vs Reliability')
plt.xlabel('LR')
plt.ylabel('reliability')
#    plot_fname='atlas_'+field+'_magnitude_dependance.ps'
#    fname=output_dir + plot_fname
#    plt.savefig(fname)
plt.show()

print "End Plotting\n"


