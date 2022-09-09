#QBB2022 - Day 4 - Homework Exercise Submission

A.
numpy.arrange is used to output values that have identical spaces between them according to the intervals that are provided. Since the intervals we provided were 0.55, 1.05, and 0.05, the output values will be spaced by 0.5. 

For the function numpy.around( ,decimals=2), numpy.around means that it will round the output values evenly to the decimal that is given. We told it to round to 2 decimal places (decimals=2). If there is no decimal place given, and only numpy.around() is used, then the output values will be rounded to 0 decimal places and will give a whole number. We may want it to round to the nearest whole number if we want all of our values to be integers, for the sake of writing the code or because of neatness of our output values.

The part of the code that has [::-1] means that it is going through the array backwards, and then converting the values from integers into strings.


C.
A trend that I see in the heatmap is that a lower probability and a lower number of tosses results in a low power value. This makes sense because the probability of getting heads a certain number of times will be very small if there is a low number of tosses. Another trend I see in the heatmap is that a higher probability and a high number of tosses results in a high power value. This again makes sense because the probability of getting heads a certain number of times will be greatly increased with a very high number of tosses. A general trend that I saw was that as the number of tosses increases, the probability graadually increases as well, making the power value larger. 


D.
The biological phenomenon that this study is focusing on is the exception to Mendel's Law of Segregation that has been seen in some alleles. There are a small amount of alleles in some parents that are inherited disproportionately by their offspring, which goes against Mendel's Law of Segregation (there is an equal probability that the offspring will inherit either of its parents alleles). They wanted to study this in humans, because it has not been well studied and because there is not a lot of data. They also wanted to apply a lot of statistical power to the data. 

The simulation experiment that I performed is similar to the simulation experiment performed in Figure S13 because they show similar trends. In my heatmap, it showed that a higher number of tosses increased the probability of getting heads, which resulted in a high power value. In Figure S13, a higher number of sperm resulted in an increased transmission rate. High numbers of sperm and high transmission rates showed a very high power value. However, even when there were the highest amount of sperm possible, sometimes the transmission rate was still very low. I think that the heatmaps in Figure S13 showed that disproportionally inherited alleles are not as common when a statistically powerful analysis is used.

The prob_heads parameter in my experiment corresponds with the transmission rate parameter in Figure S13. The n_tosses parameter corresponds with the number of sperm in Figure S13. 

Both simulations use a binomial test because binomial tests are used in probability situations. In both experiments, we wanted to see the probability of either getting heads or not getting heads, or the probability of a high transmission rate or a low transmission rate. We used the binomial test to see the resulting probabilities and check if the results matched our expectations.




