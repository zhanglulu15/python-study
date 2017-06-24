from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
def parser(x):
    return datetime.strptime('190' + x,'%y-%m')
series = read_csv('shampoo-sales.csv',header = 0,parse_dtes = [0],\
                  index_col = 0,squeeze = True,date_parser = parser)
series.plot()
pyploy.show()