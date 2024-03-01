# Question 4:
[Python] Implement CTC as described in this paper. Your implementation should support both forward and backward propagation operations.
# Answer: 
    import numpy as np
    from mindspore import nn, context

    #Define the CTC forward-backward algorithm
    class CTCForwardBackward(nn.Cell):
    def __init__(self, config):
        super(CTCForwardBackward, self).__init__()
        self.config = config
        self.net = CTCModel(input_size=config.feature_dim, batch_size=config.batch_size,
                            hidden_size=config.hidden_size, num_class=config.n_class, num_layers=config.n_layer)
        self.loss_fn = CTC_Loss(batch_size=config.batch_size, max_label_length=config.max_label_length)
        self.loss_net = WithCtcLossCell(self.net, self.loss_fn)

    def construct(self, log_probs, labels):
        T, V = log_probs.shape  # T: number of time steps, V: number of classes (including blank)
        L = len(labels) * 2 + 1  # Length of modified label sequence

        # Initialize forward variables
        alpha = np.zeros((T, L))
        alpha[0, 0] = log_probs[0, 0]  # Initialize with the first symbol of the first label

        # Initialize forward variables for modified label sequence
        alpha_bar = np.zeros((T, L))
        alpha_bar[0, 1] = log_probs[0, labels[0]]  # Initialize with the first symbol of the first label

        # Forward recursion
        for t in range(1, T):
            for s in range(L):
                alpha[t, s] = alpha[t - 1, s] + alpha_bar[t - 1, s]
                if s > 0:
                    alpha[t, s] += alpha_bar[t - 1, s - 1]
                if s < L - 1:
                    alpha_bar[t, s] = log_probs[t, labels[s // 2]] if labels[s // 2] == s // 2 else 0
                    alpha_bar[t, s] += alpha[t, s]

        # Initialize backward variables
        beta = np.zeros((T, L))
        beta[T - 1, L - 1] = log_probs[T - 1, 0]  # Initialize with the first symbol of the last label

        # Initialize backward variables for modified label sequence
        beta_bar = np.zeros((T, L))
        beta_bar[T - 1, L - 2] = log_probs[T - 1, labels[-1]]  # Initialize with the last symbol of the last label

        # Backward recursion
        for t in range(T - 2, -1, -1):
            for s in range(L - 1, -1, -1):
                beta[t, s] = beta[t + 1, s] + beta_bar[t + 1, s]
                if s < L - 1:
                    beta[t, s] += beta_bar[t + 1, s + 1]
                if s > 0:
                    beta_bar[t, s] = log_probs[t, labels[(s - 1) // 2]] if labels[(s - 1) // 2] == (s - 1) // 2 else 0
                    beta_bar[t, s] += beta[t, s]

        # Compute conditional probabilities p(l|x)
        conditional_probs = np.exp(alpha + beta - log_probs.sum(axis=1)[:, np.newaxis])

        return conditional_probs


# Example:
    config = {}  # Define your configuration
    log_probs = np.random.rand(10, 4)  # Example log probabilities (time steps, num_classes)
    labels = [1, 2, 1]  # Example label sequence

    #Initialize MindSpore context
    context.set_context(mode=context.GRAPH_MODE)

    #Create CTC forward-backward algorithm
    ctc_forward_backward = CTCForwardBackward(config)

    #Perform forward-backward propagation
    conditional_probs = ctc_forward_backward(log_probs, labels)
    print("Conditional probabilities:", conditional_probs)
