
#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def make_AB_hist(numpyArray_A, numpyArray_B):

    A_mu, A_sigma, B_mu, B_sigma = str(np.mean(numpyArray_A)), str(np.std(numpyArray_A)), str(np.mean(numpyArray_B)), str(np.std(numpyArray_B))

    fig = plt.figure(figsize = (15, 10))
    ax = fig.add_subplot(1, 1, 1)

    ax.hist(numpyArray_A, bins = 300, normed = True, color = 'orange', alpha = 0.5)
    ax.hist(numpyArray_B, bins = 300, normed = True, color = 'blue', alpha = 0.5)

    ax.set_title('Reslt\n$A:\ \mu=' + A_mu + ',\ \sigma=' + A_sigma + '$\n$B:\ \mu=' + B_mu + ',\ \sigma=' + B_sigma + '$', fontsize=18, color='grey', loc='left')
    ax.set_xlabel('parameter')
    ax.set_ylabel('frequency')
    ax.set_ylim(0, 0.1)

    fn = 'result/AB_test_result' + datetime.now().strftime('%Y%m%d%H%S') + '.png'
    fig.savefig(fn)
    fig.show()
