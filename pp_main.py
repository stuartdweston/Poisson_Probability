#===========================================================================
#
# pp_main.py
#
# Python script to query mysql database to determine the
# nearest neigbours within search radius between catalogues
# and calculate their Probability based on Poisson Probability.
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

from astropysics.constants import c,G

# Load in the definitions and constants
execfile('constants.py')
    
def auks():
    global pie
    global e
    global eradian
    pie=math.pi
    e=math.e
    eradian=180.0/math.pi

def print_header():
	print "Likelihood Ratio"
	
def print_end():
    print "End"

# Location to put plot files etc

global output_dir
output_dir='d:/temp/'

#===================================================================================================

# ask which field to process
answer=raw_input('Which field ecdfs/elais ?')
print "\nentered : ",answer,"\n"

global local_fld

if answer == 'ecdfs': 
   field='cdfs'
   survey='atlas'
   local_fld='ecdfs'
   swire_schema='swire_cdfs'
else:
   field='elais'
   survey='atlas'
   local_fld='elais'
   swire_schema='swire_es1'
   
print "Field : ",field," ; swire_schema : ",swire_schema

# now the field string is the same as the database schema name.

# notify use of nearest neigbour search radius

answer=raw_input('Nearest neighbour search radius (%s arcsec) :' % (sr))

if answer !='':
    sr=answer
    print "New nearest neighbour search radius : ",answer,"\n"

execfile('area_none_radio_survey.py')
execfile('populate_matches.py')
execfile('n_m.py')
execfile('mu_c.py')
execfile('p_c.py')
execfile('mu_star.py')
execfile('plot_p_not.py')
execfile('plot_rel_vs_pnot.py')
execfile('plot_lr_vs_pnot.py')

auks()
print_header()	

# First truncate all the working tables in the database

# Calculate the spherical area of the none-radio survey being used
# for cross matching to get an accurate measure of the area for determing
# the bacground source density per unit area.

area_nr=area_none_radio_survey()
print "Area returned  : %f" % area_nr

global sqasec
sqasec=area_nr

# Fine the nearest neighbour matches within search radius
#pm()

# Determine n(m) and update data base
#n_m()

# Determine mu_c

answer=raw_input('Determine mu_c (y/n)       : ')

if (answer =='Y' or answer=='y'):
    print "Determine mu_c      : ",answer,"\n"
    mu_c()


# Determine p_c

answer=raw_input('Determine p_c (y/n)       : ')

if (answer =='Y' or answer=='y'):
    print "Determine p_c      : ",answer,"\n"
    p_c()

# Determine mu for each IR candidate to Radio Source

answer=raw_input('Determine mu_star (y/n)       : ')

if (answer =='Y' or answer=='y'):
    print "Determine mu_star  : ",answer,"\n"
    mu_star()

# present data in plots

plot_p_not()

# compare PP to LR

plot_rel_vs_pnot()
plot_lr_vs_pnot()

print_end()
