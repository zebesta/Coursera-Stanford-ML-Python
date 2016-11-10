import numpy as np

def computeCost(X, y, theta):
    """
       computes the cost of using theta as the parameter for linear
       regression to fit the data points in X and y
    """
    m = y.size
    J = 0

# ====================== YOUR CODE HERE ======================
# Instructions: Compute the cost of a particular choice of theta
#               You should set J to the cost.
    print "Computing inner"
    print X.shape
    print theta.shape
    print theta.T.shape
    print y.shape

    inner = np.power((np.dot(X, theta.T) - y), 2)
    print "summing cost"
    J = np.sum(inner)/(2*len(X))

    # inner = np.power(((X * theta.T)-y), 2)
    # return np.sum(inner)/(2*len(X))

# =========================================================================

    return J
