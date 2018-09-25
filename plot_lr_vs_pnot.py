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

def plot_lr_vs_pnot():

    print "\nStarting Plotting comparing Likelihood Ratio to P_not\n"

# Connect to the local database with the atlas uid

    db=_mysql.connect(host="localhost",user="atlas",passwd="atlas")

# select from matches the IR Flux, Radio Flux, Redshift etc so we can do some science

    db.query("SELECT lr,p_not from atlas_dr3."+field+"_matches where lr is not null;")
          
# store_result() returns the entire result set to the client immediately.
# The other is to use use_result(), which keeps the result set in the server 
#and sends it row-by-row when you fetch.

#r=db.store_result()
# ...or...
    r=db.use_result()

# fetch results, returning char we need float !

    rows=r.fetch_row(maxrows=5000)

# rows is a tuple, convert it to a list

    lr=[]
    p_not=[]

    for row in rows:
#    print row
        lr.append(float(row[0]))
        p_not.append(float(row[1]))
	
	        	
#    End of do block

# Close connection to the database
    db.close()

# Connect to the local database with the atlas uid

    db=_mysql.connect(host="localhost",user="atlas",passwd="atlas")

# select from matches the IR Flux, Radio Flux, Redshift etc so we can do some science

    db.query("SELECT lr,p_not from atlas_dr3."+field+"_matches where lr is not null and reliability > 0.8;")
          
# store_result() returns the entire result set to the client immediately.
# The other is to use use_result(), which keeps the result set in the server 
#and sends it row-by-row when you fetch.

#r=db.store_result()
# ...or...
    r=db.use_result()

# fetch results, returning char we need float !

    rows=r.fetch_row(maxrows=5000)

# rows is a tuple, convert it to a list

    lr_08=[]
    p_not_08=[]

    for row in rows:
#    print row
        lr_08.append(float(row[0]))
        p_not_08.append(float(row[1]))
	
	        	
#    End of do block

# Close connection to the database
    db.close()
# Now plot the data

    plt.yscale('log')
    plt.xscale('log')
    plt.grid(True)
# plot(x,y,args)
    plt.plot(lr, p_not,'k.')
    plt.plot(lr_08, p_not_08,'rx')
#plot_title=field+'  ir_3_6/ir_4_5 vs ir_5_8/ir_8_0'
#    plt.title(field+' Likelihood Ratio vs Probability_not log log')
    plt.ylabel('p_not')
    plt.xlabel('Likelihood Ratio')
    plot_fname='atlas_' +field+ '_lr_vs_pnot_log.eps'
    fname=output_dir + plot_fname
    plt.savefig(fname,orientation='landscape',format="eps")
    plt.show()

    print "End Plotting comparing Likelihood Ratio to P_not\n"


