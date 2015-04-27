# Minimum Change

## SUMMARY 
This web application is used to print the minimum amount of coins that can be combined into a certain user defined value. The user should upload a file with the amount. The result is presented on the screen.

If the user writes a number that is outside the allowed range (defined in CoinDeterminer), then an error message appears. The obtained results were as expected:

    Input Test:
    6
    16
    23
    Test Output:
    2
    2
    3

## COMPILATION
To run this web application, it is necessary to have <b>web.py</b> installed.

The command for execution is:

    python index.py portnumber
where <b>portnumber</b> should be replaced for a choosen port number.


## DESIGN CHOICES
The design of this web application was based on the pattern Model-View-Controller. In the folder templates are the html files, which serve as interface/view. There are two files: index.html and result.html. The file index.html presents the initial page, where the user can update a text file with a number to be processed by the application. The file result.html presents the final result, after the number has been processed.

The controller role is done by the index.py file, that invokes the view and the method for computing the minimum change. The function to compute the minimum change is called CoinDeterminer. Its design is based on Dynamic Programming, a technique that has been proven correct for this kind of problem [1]. The framework web.py is used to create this web application and communicate with the html interfaces.

In this solution the Model part was not implemented, it was judged not necessary for this solution. However, if the software has to evolve and expand, this component can be easily added.

References<br>
    [1] http://www.ccs.neu.edu/home/jaa/CSG713.04F/Information/Handouts/dyn_prog.pdf


## ASSUMPTIONS
The file uploaded should cointain only one number to be processed.

The coin denominations used are provided in the function CoinDeterminer. It is assumed that they are always provided in strict descending order. This could easily be checked:

    if all(COINSLIST[i] >= COINSLIST[i+1] for i in xrange(len(COINSLIST)-1)) == False:
        print "Check typos in COINSLIST"
