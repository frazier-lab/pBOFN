"""
for each observation k, z, f_k(z), it should transformed to the following format

X: `d`-dimensional Tensor, with those entries that are inputs of node `k` having values, others being `NA`
y: `K`-dimensional Tensor, with those nodes that are inputs of node `k` having values, others being `NA`

in total, the number of filled values in `X` and `y` combined should be equal to the dimension of `z`
"""


class KGPartialEvaluations(MCAcquisitionFunction, OneShotAcquisitionFunction):
    def __init__():
        pass

    def forward(self, k: int, z: Tensor, X_fantasies: Tensor):
        r"""
        Args:
            k: int, index of the node being evaluated
            z: Tensor, input of the node `k`
            X_fantasies: Tensor, solutions to the inner optimization problems of KG

        Returns:
            A Tensor indicating the KG value evluated at `k`, `z`, with inner points `X_fantasies`
        """
        pass
