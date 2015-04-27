import web
from sys import maxsize

urls = ('/', 'Index',
	'/result(.*)', 'Result'
	)

render = web.template.render('templates/')

class CoinsControl:
  """ 
  A Class that deals with all the control related to the coins""" 
  @staticmethod
  
  def CoinDeterminer(n):
    """
    This function determines the minimum amount of coins necessary to amount to a given value.
    
    Args:
    n: Value that is going to be changed.
    
    Returns:
    int: The minimum change for num or -1 if the given num was not allowed.
    """
    
    INPUTBOUNDS = [1,250]
    COINSLIST = [11, 9, 7, 5, 1]
    
    n = int(n)
    if n < INPUTBOUNDS[0] or n > INPUTBOUNDS[1]:
      return -1
    
    C = [0] * (n+1)
    for p in range(1, (n+1)):
      minimum = maxsize
      for i in range(len(COINSLIST)):
	if COINSLIST[i] <= p:
	  if 1+ C[p - COINSLIST[i]] < minimum:
	    minimum = 1 + C[p-COINSLIST[i]]
	    C[p] = minimum
	    
    return C[n]
	  
class Index:
  """A Class that deals with the index page"""    
  
  def GET(self):
    """
    GET function for the Index page
    
    Args:
    self: Instance of Index.
    """
    return render.index()
  
  def POST(self):
    """
    POST function for the Index page. It obtains the upload file content and pass it to a instance of CoinsControl, so the value of the minimum change can be computed. After the value is computed, the application changes to the results page
    
    Args:
    self: Instance of Index.
    """
    
    inputFile = web.input(numberFile={})
    self.coinsControl = CoinsControl()
    self.result = self.coinsControl.CoinDeterminer(inputFile['numberFile'].value)
    raise web.seeother('/result/'+str(self.result))
  
class Result:
  """A Class that deals with the result page"""   
  
  def GET(self,value):
    """
    GET function for the Result page. It receives the computed value and print the resul or an error message, according to the given num
    Args:
    self: Instance of Index.
    value: Minimum change value.
    """
    value = value.replace("/", "")
    return render.result(int(value))
	      
if __name__ == "__main__":
  app = web.application(urls, globals())
  app.run()
  
		