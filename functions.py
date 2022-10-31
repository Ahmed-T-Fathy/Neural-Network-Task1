def gradient_descent(epochs ,rate):
    for i in range(epochs):
        Y_pred = m * X + c  # The current predicted value of Y
        D_m = (-2 / n) * sum((Y - Y_pred) * X)  # Derivative wrt m
        D_c = (-2 / n) * sum(Y - Y_pred)  # Derivative wrt c
        m = m - L * D_m  # Update m
        c = c - L * D_c  # Update c
def signum(input):
    if(input>=0):
        return 1
    else:
        return 0