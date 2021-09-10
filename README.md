# Braves_Interview
This application was created for the Atlanta Braves Organization in order to demonstate basic visualization skills and a fundamental understanding of baseball statisitcs by Jake Hlavaty.  

If any questions, feel free to reach out to me at:  
jake_hlavaty@gatech.edu  
(203)980-2803  

Additional information can also be found in the original email linking this github.

### Dashboard/Home Menu
The dashboard includes a dropdown select box to select a pitcher all 3 pitch heatmap plots. These scatter plots demonstrate pitch locations for a given pitcher and when a pitch is hovered over, offers additional details related to pitch velocity and type. Scatter plot dots are also color coded to indiate whether a pitch was a strike, ball, or hit into play.  In order, the first chart represents the pitch locations overall, the second for pitches against left handed batters, and the third for pitches against the right handed batter. In order to navigate to other pages, a navigation menu is included at the top of the screen. 

### Charting
Like the dashboard, this page also includes a dropdown menu to filter by pitcher. The chart included on this page is a spraychart representing to the play event for balls in play. Dots are colored based on play result and visualtized across a basic field spread. 

### Tendencies
Included on this page are box plots representing velocities and spin rates for different pitches thrown by Max Fried. Unfortuately due to time restrictions, I did not setup the filter for this data set due to the complicated calulations involved in quartile calculations. 

### Side v Height
Included on this page is dropdown menu to filter by pitcher and represents strikes, balls, and in-play. This plot lacks some effectiveness due to no auto scaling on the axes which would be incorporated with more time. However, the goal is to judge effectiveness of the pitcher based on release point to determine ideal release release. 

### Summary Table
This page includes a table of basic statistics for all active pitches on the Braves CSV. It includes pitch type percentages, hit totals, and basic stat calculations.
