## Dataset:
The dataset contains property prices in the city of Banglore.<br>
<br>
## Overview:<br>
Examined price_per_sqft column and did the following,<br>
<br>
(1) Removed outliers using percentile technique first. Used [0.001, 0.999] for lower and upper bound percentiles<br>
(2) After removing outliers in step 1, got a new dataframe.<br>
(3) On step(2) dataframe, used 4 standard deviation to remove outliers<br>
(4) Plotted histogram for new dataframe that is generated after step (3). Also plotted bell curve on same histogram<br>
(5) On step(2) dataframe, used zscore of 4 to remove outliers.<br>
This is quite similar to step (3) and got the exact same result<br>
