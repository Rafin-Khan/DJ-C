
Things I did
===================================
- Did not change the javascript.
- Used bootstrap to make the table look bit more appealing, and responsive for users with smaller screen.
- Used built-in django functions for the count order in contact, and sum of order in company.(This brought the load time of   page to 50000ms from 100000ms).
- Used get_queryset function in indexview where count total order for company was performed which reduced initial load time to less than 10000ms.
- Used Database Caching which brought the refresh time below 200ms once page loaded.
