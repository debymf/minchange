# minchange

<b>COMPILATION</b><br><br>
To run this web application, it is necessary to have web.py installed.
<br>
The command for execution is:<br>
python index.py <b>portnumber</b><br>
where <b>portnumber</b> should be replace for a choosen port number


<b>DESIGN CHOICES</b>
<p>&nbsp;&nbsp;&nbsp;&nbsp;The design of this web application was based on the pattern Model-View-Controller. In the folder templates are the html files, which serve as interface/view. There are two files: index.html and result.html. The file index.html presents the initial page, where the user can update a text file with a number to be processed by the application. The file result.html presents the final result, after the number has been processed.</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;The controller role is done by the index.py file, that invokes the view and the method for computing the minimum change. The function to compute the minimum change is called CoinDeterminer, its design is based on Dynamic Programming, a technique that has been proven correct for this kind of problem[1]. The framework web.py is used to create this web application and communicate with the html interfaces</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;In this implementation the Model part was not implemented, it was judged not necessary for this solution. However, if the program has to evolve and expand, this component can be easily added.</p>
  <br>
  References
  [1] http://www.ccs.neu.edu/home/jaa/CSG713.04F/Information/Handouts/dyn_prog.pdf
<br>
<br>
<b> ASSUMPTIONS</b>
The user is going to send a file cointaining only one number to be processed.
