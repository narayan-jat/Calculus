# Calculus
This repository contains **complete tutorials** on various topics covered in calculus which are required of machine learning.

[Topics](#Topics)
1. [Linear Regression](#Linearregression)
2. [Type of damping](#Type-of-damping)
3. [Gradient descent](#GradientDescent)
4. [Ordinary differntial equations](#ordinary-differential-equation)

gradient descent method 

Gradient descent is a popular optimization algorithm used in machine learning and other fields to find the minimum of a function. The algorithm is based on the idea of iteratively adjusting the parameters of a model or function in order to minimize a cost function that measures the error or discrepancy between the predicted values and the actual values of the dependent variable.

The gradient descent algorithm works by starting with an initial guess of the parameter values and then iteratively updating the values in the direction of the negative gradient of the cost function, until a minimum is reached. The negative gradient points in the direction of steepest descent, i.e., the direction of the greatest decrease in the cost function.

The update rule for the parameters is typically written as:

θ = θ - α * ∇J(θ)

Where:

θ is the vector of parameter values to be updated
α is the learning rate, which determines the size of the step taken in the direction of the negative gradient
J(θ) is the cost function, which measures the error or discrepancy between the predicted values and the actual values of the dependent variable
∇J(θ) is the gradient of the cost function with respect to the parameter vector θ
The learning rate α is a hyperparameter that controls the size of the steps taken in each iteration. If the learning rate is too large, the algorithm may overshoot the minimum and fail to converge, while if it is too small, the algorithm may take too long to converge or get stuck in a local minimum.

Gradient descent can be used with a variety of cost functions, including the mean squared error function used in linear regression, the cross-entropy function used in logistic regression, and other cost functions used in neural networks and other machine learning models. The algorithm is widely used in deep learning and other applications, and there are several variants of the algorithm, including stochastic gradient descent, mini-batch gradient descent, and others.
