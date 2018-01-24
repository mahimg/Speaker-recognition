import lasagne
import theano


from lasagne import init
from lasagne import nonlinearities
from lasagne.layers import get_all_layers
from lasagne.layers import (
    NonlinearityLayer, BiasLayer,
    DropoutLayer, GaussianNoiseLayer,
    InputLayer, InverseLayer)


def build_autoencoder(layer, nonlinearity='same', b=init.Constant(0.)):
    """
    Unfolds a stack of layers into a symmetric autoencoder with tied weights.
    Given a :class:`Layer` instance, this function builds a
    symmetric autoencoder with tied weights.
    Parameters
    ----------
    layer : a :class:`Layer` instance or a tuple
        The :class:`Layer` instance with respect to which a symmetric
        autoencoder is built.
    nonlinearity : 'same', list, callable, or None
        The nonlinearities that are applied to the decoding layer.
        If 'same', each decoder layer has the same nonlinearity as its
        corresponding encoder layer. If a list is provided, it must contain
        nonlinearities for each decoding layer. Otherwise, if a single
        nonlinearity is provided, it is applied to all decoder layers.
        If set to ``None``, all nonlinearities for the decoder layers are set
        to lasagne.nonlinearities.identity.
    b : callable, Theano shared variable, numpy array, list or None
        An initializer for the decoder biases. By default, all decoder
        biases are initialized to lasagne.init.Constant(0.). If a shared
        variable or a numpy array is provided, the shape must match the
        incoming shape (only in case all incoming shapes are the same).
        Additianlly, a list containing initializers for the biases of each
        decoder layer can be provided. If set to ``None``, the decoder
        layers will have no biases, and pass through their input instead.
    Returns
    -------
    layer: :class:`Layer` instance
       The output :class:`Layer` of the symmetric autoencoder with
       tied weights.
    encoder: :class:`Layer` instance
       The code :class:`Layer` of the autoencoder (see Notes)
    Notes
    -----
    The encoder (input) :class:`Layer` is changed using
    `unfold_bias_and_nonlinearity_layers`. Therefore, this layer is not the
    code layer anymore, because it has got its bias and nonlinearity stripped
    off.
    Examples
    --------
    >>> from lasagne.layers import InputLayer, DenseLayer
    >>> from lasagne.layers import build_autoencoder
    >>> l_in = InputLayer((100, 20))
    >>> l1 = DenseLayer(l_in, num_units=50)
    >>> l2 = DenseLayer(l1, num_units=10)
    >>> l_ae, l2 = build_autoencoder(l2, nonlinearity='same', b=None)
    """

    if isinstance(nonlinearity, (tuple, list)):
        n_idx = 0

    if isinstance(b, (tuple, list)):
        b_idx = 0

    encoder = unfold_bias_and_nonlinearity_layers(layer)
    layers = get_all_layers(encoder)
    autoencoder_layers = [encoder]

    kwargs_b = dict(b=None)
    kwargs_n = dict(nonlinearity=nonlinearities.identity)
    for i, layer in enumerate(layers[::-1]):

        incoming = autoencoder_layers[-1]
        if isinstance(layer, InputLayer):
            continue
        elif isinstance(layer, BiasLayer):
            if b is None:
                kwargs_b = dict(b=None)
            elif isinstance(b, (tuple, list)):
                kwargs_b = dict(b=b[b_idx])
                b_idx += 1
            else:
                kwargs_b = dict(b=b)
        elif isinstance(layer, NonlinearityLayer):
            if nonlinearity == 'same':
                kwargs_n = dict(nonlinearity=layer.nonlinearity)
            elif nonlinearity is None:
                kwargs_n = dict(nonlinearity=nonlinearities.identity)
            elif isinstance(nonlinearity, (tuple, list)):
                kwargs_n = dict(nonlinearity=nonlinearity[n_idx])
                n_idx += 1
            else:
                kwargs_n = dict(nonlinearity=nonlinearity)
        elif isinstance(layer, DropoutLayer):
            a_layer = DropoutLayer(
                incoming=incoming,
                p=layer.p,
                rescale=layer.rescale
            )
            autoencoder_layers.append(a_layer)
        elif isinstance(layer, GaussianNoiseLayer):
            a_layer = GaussianNoiseLayer(
                incoming=incoming,
                sigma=layer.sigma
            )
            autoencoder_layers.append(a_layer)
        else:
            a_layer = InverseLayer(
                incoming=incoming,
                layer=layer
            )
            if hasattr(layer, 'b'):
                a_layer = BiasLayer(
                    incoming=a_layer,
                    **kwargs_b
                )
            if hasattr(layer, 'nonlinearity'):
                a_layer = NonlinearityLayer(
                    incoming=a_layer,
                    **kwargs_n
                )
            autoencoder_layers.append(a_layer)

    return autoencoder_layers[-1], encoder


def unfold_bias_and_nonlinearity_layers(layer):
    """
    Unfolds a stack of layers adding :class:`BiasLayer` and
    :class:`NonlinearityLayer` when needed.
    Given a :class:`Layer` instance representing a stacked network,
    this function adds a :class:`BiasLayer` instance and/or a
    :class:`NonlinearityLayer` instance in between each layer with attributes
    b (bias) and/or nonlinearity, with the same bias and nonlinearity,
    while deleting the bias and or setting the nonlinearity
    of the original layer to the identity
    function.
    Parameters
    ----------
    layer : a :class:`Layer` instance or a tuple
        The :class:`Layer` instance with respect to wich the new
        stacked Neural Network with added :class:`BiasLayer`: and
        class:`NonlinearityLayer` are built.
    Returns
    -------
    layer: :class:`Layer` instance
        The output :class:`Layer` of the symmetric autoencoder with
        tied weights.
    Examples
    --------
    >>> import lasagne
    >>> from lasagne.layers import InputLayer, DenseLayer
    >>> from lasagne.layers import BiasLayer, NonlinearityLayer
    >>> from lasagne.layers import unfold_bias_and_nonlinearity_layers
    >>> from lasagne.layers import get_all_layers
    >>> from lasagne.nonlinearities import tanh, sigmoid, identity
    >>> l_in = InputLayer((100, 20))
    >>> l1 = DenseLayer(l_in, num_units=50, nonlinearity=tanh)
    >>> l_out = DenseLayer(l1, num_units=10, nonlinearity=sigmoid)
    >>> l_out = unfold_bias_and_nonlinearity_layers(l_out)
    """
    layers = get_all_layers(layer)
    incoming = layers[0]

    for ii, layer in enumerate(layers[1:]):
        layer.input_layer = incoming
        # Check if the layer has a bias
        b = getattr(layer, 'b', None)
        add_bias = False
        # Check if the layer has a nonlinearity
        nonlinearity = getattr(layer, 'nonlinearity', None)
        add_nonlinearity = False
        if b is not None and not isinstance(layer, BiasLayer):
            layer.b = None
            del layer.params[b]
            add_bias = True
        if (nonlinearity is not None and
                not isinstance(layer, NonlinearityLayer) and
                nonlinearity != nonlinearities.identity):
            layer.nonlinearity = nonlinearities.identity
            add_nonlinearity = True

        if add_bias:
            layer = BiasLayer(
                incoming=layer,
                b=b
            )
        if add_nonlinearity:
            layer = NonlinearityLayer(
                incoming=layer,
                nonlinearity=nonlinearity
            )
        incoming = layer
    return layer

# Alias
expand_nonlinearity_layers = unfold_bias_and_nonlinearity_layers


if __name__ == '__main__':

    input_shape = (100, 30)
    l_in = lasagne.layers.InputLayer(input_shape)

    l1 = lasagne.layers.DenseLayer(l_in, 30, b=None,
                                   nonlinearity=nonlinearities.identity)
    l2 = lasagne.layers.BiasLayer(l1)
    l3 = lasagne.layers.NonlinearityLayer(l2)
    l4 = lasagne.layers.DenseLayer(l3, 10, b=None,
                                   nonlinearity=nonlinearities.identity)
    l5 = lasagne.layers.BiasLayer(l4)
    l6 = lasagne.layers.NonlinearityLayer(l5)
    all_layer_names = [l.__class__.__name__ for l in get_all_layers(l6)]
    l6_e = unfold_bias_and_nonlinearity_layers(l6)
    all_layer_names_e = [l.__class__.__name__ for l in get_all_layers(l6)]

    print all([i == j for i, j in zip(all_layer_names, all_layer_names_e)])