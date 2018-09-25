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

# First find the max and min p_not, then set bins for p_not based on colour

db.query("SELECT min(p_not),max(p_not) from atlas.ecdfs_matches where reliability is not null;")

r=db.use_result()

# fetch results, returning char we need float !

rows=r.fetch_row(maxrows=1)

# rows is a tuple, convert it to a list

p_not_min=[]
p_not=[]

for row in rows:
    print row
    p_not_min=float(row[0])
    p_not_max=float(row[1])
    print p_not_min," ",p_not_max

db.close()

p_not_inc=p_not_max/5
	
#-------------------------------------------------------------------------------

#   Connect to the local database with the atlas uid

db=_mysql.connect(host=db_host,user=db_user,passwd=db_passwd)

# select from matches the IR Flux, Radio Flux, Redshift etc so we can do some science

p_not_min=0.0
p_not_max=p_not_inc
print p_not_min," ",p_not_max

sql1="SELECT reliability,lr from atlas.ecdfs_matches \
          where reliability is not null \
          and p_not > %f and p_not < %f;" % (p_not_min,p_not_max)

legend1="p_not gt %f and p_not lt %f" % (p_not_min,p_not_max)
print legend1

print sql1
db.query(sql1)
          
# store_result() returns the entire result set to the client immediately.
# The other is to use use_result(), which keeps the result set in the server 
#and sends it row-by-row when you fetch.

#r=db.store_result()
# ...or...
r1=db.use_result()

# fetch results, returning char we need float !

rows1=r1.fetch_row(maxrows=5000)

# rows is a tuple, convert it to a list

reliability1=[]
lr1=[]

for row1 in rows1:
#    print row1
    reliability1.append(float(row1[0]))
    lr1.append(float(row1[1]))
	
# Close connection to the database

db.close()

#    End of do block
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

#   Connect to the local database with the atlas uid

db=_mysql.connect(host=db_host,user=db_user,passwd=db_passwd)

# select from matches the IR Flux, Radio Flux, Redshift etc so we can do some science

p_not_min=p_not_max
p_not_max=p_not_max+p_not_inc
print p_not_min," ",p_not_max

sql2="SELECT reliability,lr from atlas.ecdfs_matches \
          where reliability is not null \
          and p_not > %f and p_not < %f;" % (p_not_min,p_not_max)

print sql2
db.query(sql2)
          
# store_result() returns the entire result set to the client immediately.
# The other is to use use_result(), which keeps the result set in the server 
#and sends it row-by-row when you fetch.

#r=db.store_result()
# ...or...
r2=db.use_result()

# fetch results, returning char we need float !

rows2=r2.fetch_row(maxrows=5000)

# rows is a tuple, convert it to a list

reliability2=[]
lr2=[]

for row2 in rows2:
#    print row2
    reliability2.append(float(row2[0]))
    lr2.append(float(row2[1]))
	
# Close connection to the database

db.close()

#    End of do block
#-------------------------------------------------------------------------------

#   Connect to the local database with the atlas uid

db=_mysql.connect(host=db_host,user=db_user,passwd=db_passwd)

# select from matches the IR Flux, Radio Flux, Redshift etc so we can do some science

p_not_min=p_not_max
p_not_max=p_not_max+p_not_inc
print p_not_min," ",p_not_max

sql3="SELECT reliability,lr from atlas.ecdfs_matches \
          where reliability is not null \
          and p_not > %f and p_not < %f;" % (p_not_min,p_not_max)

print sql3
db.query(sql3)
          
# store_result() returns the entire result set to the client immediately.
# The other is to use use_result(), which keeps the result set in the server 
#and sends it row-by-row when you fetch.

#r=db.store_result()
# ...or...
r3=db.use_result()

# fetch results, returning char we need float !

rows3=r3.fetch_row(maxrows=5000)

# rows is a tuple, convert it to a list

reliability3=[]
lr3=[]

for row3 in rows3:
#    print row3
    reliability3.append(float(row3[0]))
    lr3.append(float(row3[1]))
	
# Close connection to the database

db.close()

#    End of do block
#-------------------------------------------------------------------------------

#   Connect to the local database with the atlas uid

db=_mysql.connect(host=db_host,user=db_user,passwd=db_passwd)

# select from matches the IR Flux, Radio Flux, Redshift etc so we can do some science

p_not_min=p_not_max
p_not_max=p_not_max+p_not_inc
print p_not_min," ",p_not_max

sql4="SELECT reliability,lr from atlas.ecdfs_matches \
          where reliability is not null \
          and p_not > %f and p_not < %f;" % (p_not_min,p_not_max)

print sql4
db.query(sql4)
          
# store_result() returns the entire result set to the client immediately.
# The other is to use use_result(), which keeps the result set in the server 
#and sends it row-by-row when you fetch.

#r=db.store_result()
# ...or...
r4=db.use_result()

# fetch results, returning char we need float !

rows4=r4.fetch_row(maxrows=5000)

# rows is a tuple, convert it to a list

reliability4=[]
lr4=[]

for row4 in rows4:
#    print row4
    reliability4.append(float(row4[0]))
    lr4.append(float(row4[1]))
	
# Close connection to the database

db.close()

#    End of do block
#-------------------------------------------------------------------------------
#   Connect to the local database with the atlas uid

db=_mysql.connect(host=db_host,user=db_user,passwd=db_passwd)

# select from matches the IR Flux, Radio Flux, Redshift etc so we can do some science

p_not_min=p_not_max
p_not_max=p_not_max+p_not_inc
print p_not_min," ",p_not_max

sql5="SELECT reliability,lr from atlas.ecdfs_matches \
          where reliability is not null \
          and p_not > %f and p_not < %f;" % (p_not_min,p_not_max)

print sql5
db.query(sql5)
          
# store_result() returns the entire result set to the client immediately.
# The other is to use use_result(), which keeps the result set in the server 
#and sends it row-by-row when you fetch.

#r=db.store_result()
# ...or...
r5=db.use_result()

# fetch results, returning char we need float !

rows5=r5.fetch_row(maxrows=5000)

# rows is a tuple, convert it to a list

reliability5=[]
lr5=[]

for row5 in rows5:
#    print row5
    reliability5.append(float(row5[0]))
    lr5.append(float(row5[1]))
	
# Close connection to the database

db.close()

#    End of do block
#-------------------------------------------------------------------------------

#   Connect to the local database with the atlas uid

db=_mysql.connect(host=db_host,user=db_user,passwd=db_passwd)

# select from matches the IR Flux, Radio Flux, Redshift etc so we can do some science

p_not_min=p_not_max
p_not_max=p_not_max+p_not_min
print p_not_min," ",p_not_max

sql6="SELECT reliability,lr from atlas.ecdfs_matches \
          where reliability is not null \
          and p_not > %f and p_not < %f;" % (p_not_min,p_not_max)

print sql6
db.query(sql6)
          
# store_result() returns the entire result set to the client immediately.
# The other is to use use_result(), which keeps the result set in the server 
#and sends it row-by-row when you fetch.

#r=db.store_result()
# ...or...
r6=db.use_result()

# fetch results, returning char we need float !

rows6=r6.fetch_row(maxrows=6000)

# rows is a tuple, convert it to a list

reliability6=[]
lr6=[]

for row6 in rows6:
#    print row6
    reliability6.append(float(row6[0]))
    lr6.append(float(row6[1]))
	
# Close connection to the database

db.close()

#    End of do block
#-------------------------------------------------------------------------------

# Now plot the data

#plt.yscale('log')
plt.xscale('log')
# plot(x,y,args)

plt.plot(lr1, reliability1,'mo',lr2, reliability2,'bo',lr3, reliability3,'go',lr4, reliability4,'yo',lr5, reliability5,'co',lr6, reliability6,'ro')
plt.legend((' lt %f' % p_not_inc,'lt %f' % (p_not_inc*2),'lt %f' % (p_not_inc*3),'lt %f' % (p_not_inc*4),'lt %f' % (p_not_inc*5),'lt %f' % (p_not_inc*6)),title='P_not',loc=2)
#plot_title=field+'  ir_3_6/ir_4_5 vs ir_5_8/ir_8_0'
#plt.title(' Likelihood Ratio vs Reliability')
plt.xlabel('LR')
plt.ylabel('Reliability')
#    plot_fname='atlas_'+field+'_magnitude_dependance.ps'
#    fname=output_dir + plot_fname
#    plt.savefig(fname)
plt.show()

print "End Plotting\n"


