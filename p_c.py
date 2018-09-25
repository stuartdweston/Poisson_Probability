#===========================================================================
#
# p_c.py
#
# For the Poisson Probability calculate p_c
#
# P_c = 1 - e ** -mu_c
#
#
#===========================================================================
#
# S. Weston
# AUT University
# Nov 2013
#===========================================================================

def p_c():

    global p_c
    
    print "\nStarting p_c calculations "

    execfile('constants.py')

    p_c=1-(e**(-mu_c))
    
    print "p_c       :",p_c
    
    print "End of p_c\n"





