#===========================================================================
#
# mu_c.py
#
# For the Poisson Probability calculate mu_c
#
# mu_c = pie x r**2 x (m to +infinity) sum_n_m / area
#
# Density of background IR sources per sqa sec.
#
#===========================================================================
#
# S. Weston
# AUT University
# Nov 2013
#===========================================================================

def mu_star():

    print "\nStarting mu_star calculations "

    execfile('constants.py')

# Connect to the local database with the atlas uid

    db=_mysql.connect(host="localhost",user="atlas",passwd="atlas")

# Lets run a querry to get a list of the matches, we need cid,swire_index_spitzer and r_arcsec
	
    sql1="select cid,swire_index_spitzer,r_arcsec from atlas_dr3."+field+"_matches"
    db.query(sql1)

# now do a loop looking at each match
    
    r=db.store_result()
    rows=r.fetch_row(maxrows=0)
    db.close
    
    for row in rows:
       cid=row[0]
       swire_index_spitzer=row[1]
       r_arcsec=float(row[2])
       
       sys.stdout.write('.')
#       print cid," ",swire_index_spitzer," ",r_arcsec
       
       db=_mysql.connect(host="localhost",user="atlas",passwd="atlas")
       sql2="select IRAC_3_6_micron_FLUX_MUJY FROM fusion.swire_"+field+" where index_spitzer='"+swire_index_spitzer+"';"
#       print sql2
       
       db.query(sql2)
       
       r2=db.store_result()
       rows2=r2.fetch_row(maxrows=1)
       for row2 in rows2:
           ir_flux=float(row2[0])
           str_ir_flux=row2[0]
#           print ir_flux 
       
       db.close
       
#      Now find the sum (m to infinity) n(m) dm, based on the ir_flux.
       sql3="select count(*) FROM fusion.swire_"+field+" where IRAC_3_6_micron_FLUX_MUJY >= "+str_ir_flux+";"
#       print sql3
       db=_mysql.connect(host="localhost",user="atlas",passwd="atlas")
       db.query(sql3)
       
       r3=db.store_result()
       rows3=r3.fetch_row(maxrows=1)
       for row3 in rows3:
           n_m=float(row3[0])
#           print n_m 
       db.close()

       mu_star=pie*(r_arcsec**2)*n_m/sqasec
 
#       print "mu*         :",mu_star
       
#    db.query("select IRAC_3_6_micron_FLUX_MUJY FROM %s.swire where index_spitzer=swire_index_spitzer  \
#    This IR flux is used   

#   Calculate the p_star

       p_star=1-(e**(-mu_star))
    
#       print "p*          :",p_star
       
#   Look at p_star, need if statement here as we use different formula for E depending on p_star to p_c

       if p_star >= p_c:
          E=p_star
       else:
          E=p_star*(1+math.log(p_c/p_star))
       
#   Calculate P_not

       p_not=1-(e**(-E))

#       print "P_not       :",p_not
       
#   insert p_not into matches table
       db=_mysql.connect(host="localhost",user="atlas",passwd="atlas")
       db.query("set autocommit=0;")
       sql_insert="update atlas_dr3.%s_matches set p_not=%f where cid='%s' and swire_index_spitzer='%s';" % (field, p_not, cid, swire_index_spitzer)
#       print sql_insert
       db.query("update atlas_dr3.%s_matches set p_not=%f where cid='%s' and swire_index_spitzer='%s';" % (field, p_not, cid, swire_index_spitzer))
       db.commit()
       db.close()
       
#   End of loop
    
    print "End of mu_star\n"





