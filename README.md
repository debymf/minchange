# minchange

DESIGN CHOICES

  The design of this web application was based on the pattern Model-View-Controller. In the folder templates we have the html files, which serve as our interface/view. There are two files: index.html and result.html. The file index.html presents the initial page, where the user can update a text file with a number to be processed by the application. The file result.html presents the final result, after the number has been processed.
  The controller role is done by the index.py file, that invokes the view and the method for computing the minimum change. The function to compute the minimum change is called CoinDeterminer, its design is based on Dynamic Programming, a technique that has been proven correct for this kind of problem[1].
  In this implementation the Model part was not implemented, it was judged not necessary for this solution. However, if the program has to evolve and expand, this component can be easily added.
  
  References
  [1] http://www.ccs.neu.edu/home/jaa/CSG713.04F/Information/Handouts/dyn_prog.pdf
