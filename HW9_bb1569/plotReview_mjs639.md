## Plot Review for mjs639

I found this plot interesting, as it gives an initial glance at a topic that can be analyzed in more depth : how SAT scores vary depending on neighborhood's socio-economic characterstics. 



![image of env](https://github.com/biabbiassago/PUI2017_bb1569/blob/master/HW9_bb1569/satmap.png)


Link to interactive map:  https://mjs639.carto.com/builder/10f6d682-fad1-4050-87ea-703f4120f7a9/embed


__CLARITY__:  

It was easy to understand what the map represents, since the legend is very evident. However, I think it would have been better to have specified that SAT Score Average is BY SCHOOL. 

One thing that would help clarity, in my opinion, is to improve the scale. The SAT scores go from a min of 800 to a max of 2100, so I think it would be useful to have that specified on the legend.


__AESTHETIC__  :   

The choice of color makes it a bit hard to interpret the map. In particular, for very low SAT Average Score, the bright yellow color is too similar to the maps' background color, making it hard to see where the points are. 

I think that using a gradient rather than bins colors makes it a bit harder to differentiate between levels of SAT score.You could choose to cut off points (for example at percentiles) in different-color bins.

# FBB A diverging color map (https://matplotlib.org/examples/color/colormaps_reference.html) - for example RdBu - would be appropriate here, with point of divergence the average score. This way the above average and below average SAT scores are encoded with different colors providing an additional piece of info at a glance, and provide more color resolution on either sides of the average

__HONESTY__:   

All the dots are the same size which is a good choice, since it is does not give more importance to higher or lower scores. 

# FBB an additional dimension: number of students could be encoded as point size

However, as I mentioned before, having a light color that is hard to see makes it seem like the average score is higher than in reality, and this impacts the honesty of the plot. 

A last suggestion would be to think of a way to deal with overlapping dots, perhaps changing the alpha-levels for some bins. In this plot, the darker dots show a lot more so when dots are overlapping it is hard to see the lower-score schools. 

# FBB a problem with carto is that when uploading the link on a browser the zoom in level can crop regions, depending on the size of the browser window. This is an issue because outer borroughs (Bx, SI) are likely to get cut out

# FBB 10/10
