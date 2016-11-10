from computeCost import computeCost
import numpy as np


def gradientDescent(X, y, theta, alpha, num_iters):
    """
     Performs gradient descent to learn theta
       theta = gradientDescent(x, y, theta, alpha, num_iters) updates theta by
       taking num_iters gradient steps with learning rate alpha
    """
    print "Sizes"
    print X.shape
    print theta.shape
    print y.shape
    # Initialize some useful values
    J_history = []
    m = y.size  # number of training examples
    print "setting temp"
    temp = np.zeros(theta.shape)
    print theta
    print temp
    parameters = theta.size
    print "Parameters: "
    print parameters

    for i in range(num_iters):
        print i
        error = np.dot(X, theta.T) - y
        print error
        for j in range(parameters):
            print j
            print error.shape
            print X.shape
            print error
            print X[:,j]
            term = np.multiply(error, X[:,j])
            print term
            print temp.shape
            print theta.shape
            temp[j] = theta[j] - ((alpha / len(X)) * np.sum(term))
        #   ====================== YOUR CODE HERE ======================
        # Instructions: Perform a single gradient step on the parameter vector
        #               theta.
        #
        # Hint: While debugging, it can be useful to print out the values
        #       of the cost function (computeCost) and gradient here.
        #


        # ============================================================
        #save new theta after all temps pave been update in the j loop
        theta = temp
        # Save the cost J in every iteration
        J_history.append(computeCost(X, y, theta))
    return theta, J_history
