#===========================================================================
#
# Plot P_not
#
# Python script to query atlas mysql database to
# plot p_not, see if its truely poisson
#
#===========================================================================
#
# S. Weston
# AUT University
# Nov 2013
#===========================================================================

def plot_p_not():

    print "\nStarting plot_p_not\n"

# Connect to the local database with the atlas uid

    db=_mysql.connect(host="localhost",user="atlas",passwd="atlas")

# First find the max and min p_not, then set bins for p_not based on colour

    db.query("SELECT min(p_not),max(p_not) from atlas_dr3."+field+"_matches where reliability is not null;")

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

# Connect to the local database with the atlas uid

    db=_mysql.connect(host="localhost",user="atlas",passwd="atlas")

# First find the max and min p_not, then set bins for p_not based on colour

    db.query("SELECT p_not from atlas_dr3."+field+"_matches where reliability is not null;")

    r2=db.use_result()

# fetch results, returning char we need float !

    rows2=r2.fetch_row(maxrows=0)

# rows is a tuple, convert it to a list

    p_not=[]

    for row2 in rows2:
#    print row1
        p_not.append(float(row2[0]))

	
# Close connection to the database

    db.close()

#numpy.histogram(rows,bins=50)

# fetch_row paramaters, maxrows and how

#The other oddity is: Assuming these are numeric columns, why are they returned 
#as strings? Because MySQL returns all data as strings and expects you to 
#convert it yourself. This would be a real pain in the ass, but in fact, _mysql 
#can do this for you. (And MySQLdb does do this for you.) To have automatic 
#type conversion done, you need to create a type converter dictionary, and pass 
#this to connect() as the conv keyword parameter.

    (hist,bins)=numpy.histogram(p_not,bins=25,range=[p_not_min,p_not_max])
    width = 0.7*(bins[1]-bins[0])
    center = (bins[:-1]+bins[1:])/2
#plt.yscale('log')
#plt.xscale('log')
    plt.bar(center, hist, align = 'center',width = width,linewidth=0)
#    plot_title=field+' P_not'
#    plt.title(plot_title)
    plt.ylabel('n(P_not)')
    plt.xlabel('P_not')
    plot_fname='atlas_' +field+ '_p_not.eps'
    fname=output_dir + plot_fname
    plt.savefig(fname,orientation='landscape',format="eps")
    plt.show()
    
    print "End of plot_p_not\n"