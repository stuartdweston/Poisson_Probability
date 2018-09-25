#===========================================================================
#
# plot_rel_vs_pnot.py
#
# Python script to query SWIRE_ES1 mysql database to 
# select from matches the IR Flux, Radio Flux, Redshift etc so we can do some science
#
#===========================================================================
#
# S. Weston
# AUT University
# Jan 2015
#===========================================================================

def plot_rel_vs_pnot():

    print "\nStarting Plotting comparing Reliability to P_not\n"

# Connect to the local database with the atlas uid

    db=_mysql.connect(host="localhost",user="atlas",passwd="atlas")

# select from matches the IR Flux, Radio Flux, Redshift etc so we can do some science

    db.query("SELECT reliability,p_not from atlas_dr3."+field+"_matches where reliability is not null;")
          
# store_result() returns the entire result set to the client immediately.
# The other is to use use_result(), which keeps the result set in the server 
#and sends it row-by-row when you fetch.

#r=db.store_result()
# ...or...
    r=db.use_result()

# fetch results, returning char we need float !

    rows=r.fetch_row(maxrows=5000)

# rows is a tuple, convert it to a list

    reliability=[]
    p_not=[]

    for row in rows:
#    print row
        reliability.append(float(row[0]))
        p_not.append(float(row[1]))
	
	        	
#    End of do block

# Close connection to the database
    db.close()

# Select those where rel > 0.8

# Connect to the local database with the atlas uid

    db=_mysql.connect(host="localhost",user="atlas",passwd="atlas")

# select from matches the IR Flux, Radio Flux, Redshift etc so we can do some science

    db.query("SELECT reliability,p_not from atlas_dr3."+field+"_matches where reliability > 0.8;")
          
# store_result() returns the entire result set to the client immediately.
# The other is to use use_result(), which keeps the result set in the server 
#and sends it row-by-row when you fetch.

#r=db.store_result()
# ...or...
    r=db.use_result()

# fetch results, returning char we need float !

    rows=r.fetch_row(maxrows=5000)

# rows is a tuple, convert it to a list

    reliability_8=[]
    p_not_8=[]

    for row in rows:
#    print row
        reliability_8.append(float(row[0]))
        p_not_8.append(float(row[1]))
	
	        	
#    End of do block

# Close connection to the database
    db.close()



# Now plot the data

#    plt.yscale('log')
#    plt.xscale('log')
    plt.grid(True)
# plot(x,y,args)
    plt.plot(reliability, p_not,'k.')
    plt.plot(reliability_8, p_not_8,'rx')
#plot_title=field+'  ir_3_6/ir_4_5 vs ir_5_8/ir_8_0'
    plt.title(field+' Reliability vs Probability_not')
    plt.ylabel('p_not')
    plt.xlabel('reliability')
    plot_fname='atlas_' +field+ '_rel_vs_pnot.eps'
    fname=output_dir + plot_fname
    plt.savefig(fname,orientation='landscape',format="eps")
    plt.show()

    print "End Plotting comparing Reliability to P_not\n"


