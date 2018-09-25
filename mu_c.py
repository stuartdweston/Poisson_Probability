#===========================================================================
#
# mu_c.py
#
# For the Poisson Probability calculate mu_c
#
# mu_c = pie x sr**2 x sum_n_m / area
#
# Density of background IR sources per sqa sec.
#
#===========================================================================
#
# S. Weston
# AUT University
# Nov 2013
#===========================================================================

def mu_c():

    global mu_c
    
    print "\nStarting mu_c calculations "

    execfile('constants.py')

# Connect to the local database with the atlas uid

    db=_mysql.connect(host="localhost",user="atlas",passwd="atlas")

# Lets run a querry
	
    sql="select sum(n_m) from atlas_dr3."+field+"_n_m_lookup"
    db.query(sql)
    
    r=db.store_result()
    rows=r.fetch_row(maxrows=1)
    for row in rows:
       sum_n_m=float(row[0])

    db.close()

    print "sum_n_m    :",sum_n_m
    
    mu_c=pie*(sr**2)*sum_n_m/sqasec

    print "mu_c       :",mu_c
    
    print "End of mu_c\n"





