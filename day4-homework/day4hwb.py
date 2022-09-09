def run_experiment(n_iters = 100, seed = 389, correct_the_pvalues = False):
    '''
    Input: prob_heads, a float, the probability of a simulated coin toss returning heads
           n_toss, an integer, the number of coin tosses to simulate
           n_iters, an integer, the number of iterations for each simulation. default is 100
           seed, an integer, the random seed that you will set for the whole simulation experiment. default is 389
           correct_the_pvalues, a boolean, whether or not to perform multiple hypothesis testing correction
    Output: power, a float, the power of the experiment
    '''
    
    n_tosses = numpy.array([10, 50, 100, 250, 500, 1000])
    prob_heads = numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)[::-1]
    power_mat = numpy.zeros((len(n_tosses), len(prob_heads)))
    #print(power_mat)
 
    numpy.random.seed(seed)
        
    for i, n in enumerate(n_tosses):
        for j, p in enumerate(prob_heads):
            
            # compute power for this n and p
            # run_experiment(n,p) > power_ou    
            pvals = []
            for k in range(n_iters):
               
                results_arr = simulate_coin_toss(n, prob_heads = p)
                n_success = numpy.sum(results_arr)
                pvals.append(perform_hypothesis_test(n_success, n))
            if correct_the_pvalues:
                pvals = correct_pvalues(pvals)
            pvals_translated_to_bools = interpret_pvalues(pvals)
            power = compute_power(numpy.sum(pvals_translated_to_bools), n_iters)
            power_mat[i,j] = power
    return power_mat

    

    
    
#def perform_hypothesis_test(prob_heads, n_tosses):
 #   binom_result = binomtest(prob_heads, n_tosses)
 #   pval = binom_result.pvalue
    #return(pval)

#def correct_pvalues(pvals):
 #   correct_pvalues = multipletests(pvals, method="bonferroni")
 #   return(correct_pvalues[1])

#print(correct_pvalues(pvals))



#power1 = run_experiment(0.6, 500, correct_the_pvalues = True)
power2 = run_experiment(correct_the_pvalues = True)
power2b = run_experiment(correct_the_pvalues = False)

fig, ax = plt.subplots()
ax.plot(power2)
plt.xlabel('Experiment 2')
plt.ylabel('Power Computed with Multiple Hypothesis Testing Correction')
#plt.show()
#plt.savefig("power2.png")

fig, ax = plt.subplots()
ax.plot(power2b)
plt.xlabel('Experiment 2b')
plt.ylabel('Power Computed without Multiple Hypothesis Testing Correction')
#plt.show()
plt.savefig("power2b.png")
