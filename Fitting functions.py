%load_ext autoreload
%autoreload 2 
from IPython.display import Image
from   collections              import defaultdict
import networkx                 as nx
from   prettytable              import PrettyTable  # Tables & matrix libraries
import numpy                    as     np 
import pandas                   as     pd
import pylab                    as     pl
import matplotlib.pyplot        as     plt # Tables & plots libraries
import sklearn.metrics          as     met 
import sklearn.datasets         as     dt
import sklearn.linear_model     as     li # Inequalities libraries
import sklearn.model_selection  as     ms
import scipy                    as     linalg 

# Naive Bayes model libraries
from   pgmpy.models             import NaiveBayes, BayesianModel
from   pgmpy.factors.discrete   import TabularCPD
from   pgmpy.inference          import VariableElimination


np.random.seed(0)
IRIS = dt.load_iris()
Table = PrettyTable(['Database','Attributes','NO of samples','NO of classes'])
Table.add_row(['Canser','10','699','2'])
Table.add_row(['adult','15','32561','2'])
Table.add_row(['bridges.version1','13','108','7'])
Table.add_row(['bridges.version2','13','108','7'])
Table.add_row(['Car','7','1728','4'])
Table.add_row(['dermatology','35','366','6'])
Table.add_row(['ecoli','8','336','8'])
Table.add_row(['flag','3','194','8'])
Table.add_row(['glass','11','214','6'])
Table.add_row(['hepatitis','20','155','2'])
Table.add_row(['iris','5','150','3'])
Table.add_row(['nursery','9','12960','5'])
Table.add_row(['soybean-small','36','47','4'])
Table.add_row(['zoo','18','110','7'])
Table.add_row(['cmc','10','1473','3'])
Table.add_row(['transfusion','5','748','2'])
Table.add_row(['yellow-small','5','20','2'])
Table.add_row(['lenses','5','24','3'])
Table.add_row(['magic Gamma','11','19020','2'])
Table.add_row(['sonar','61','208','2'])

np.array(Table)
