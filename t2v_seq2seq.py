#!/usr/bin/python
# -*- encoding: utf8 -*-

import numpy as np
import optparse
import random
import sys
import tensorflow as tf
import datetime

def learn(train_fname, test_fname, test_output_fname, test_fname2, test_output_fname2):
    def loopf(prev, i):
        return prev

    learning_rate = 0.0001
    training_epochs = 4

    size = 128
    batch_size = 1
    max_length = 100
    feature_count = 2

    input_length = tf.placeholder(tf.int32)

    initializer = tf.random_uniform_initializer(-1, 1)

    seq_input = tf.placeholder(tf.float32, [max_length, batch_size, feature_count])

    useful_input = seq_input[0:input_length[0]]
    loss_inputs = [tf.reshape(useful_input, [-1])]
    encoder_inputs = [item for item in tf.unstack(seq_input)]
    # if encoder input is "X, Y, Z", then decoder input is "0, X, Y, Z". Therefore, the decoder size
    # and target size equal encoder size plus 1. For simplicity, here I droped the last one.
    decoder_inputs = ([tf.zeros_like(encoder_inputs[0], name="GO")] + encoder_inputs[:-1])
    targets = encoder_inputs

    # basic LSTM seq2seq model
    cell = tf.contrib.rnn.LSTMCell(size, state_is_tuple=True, use_peepholes=True)
    _, enc_state = tf.contrib.rnn.static_rnn(cell, encoder_inputs, sequence_length=input_length[0], dtype=tf.float32)
    cell = tf.contrib.rnn.OutputProjectionWrapper(cell, feature_count)
    dec_outputs, dec_state = tf.contrib.legacy_seq2seq.rnn_decoder(decoder_inputs, enc_state, cell, loop_function=loopf)

    # flatten the prediction and target to compute squared error loss
    y_true = [tf.reshape(encoder_input, [-1]) for encoder_input in encoder_inputs]
    y_pred = [tf.reshape(dec_output, [-1]) for dec_output in dec_outputs]

    # Define loss and optimizer, minimize the squared error
    loss = 0
    for i in range(len(loss_inputs)):
        loss += tf.reduce_sum(tf.square(tf.subtract(y_pred[i], y_true[len(loss_inputs) - i - 1])))
    optimizer = tf.train.RMSPropOptimizer(learning_rate).minimize(loss)

    # Initializing the variables
    init = tf.initialize_all_variables()

    # Launch the graph
    with tf.Session() as sess:
        sess.run(init)
        default_features = [[0] * feature_count]
        for epoch in range(training_epochs):
            print epoch

            total_cost = 0.0
            data_count = 0
            with open(train_fname) as f:
                for line in f:
                    data = eval(line)
                    length = len(data)

                    if length < max_length:
                        data.extend(default_features * (max_length-length))
                    if length > max_length:
                        data = data[:max_length]
                        length = max_length

                    x = np.array(data)
                    x = x.reshape((max_length, batch_size, feature_count))

                    embedding = None
                    feed = {seq_input: x, input_length: [length]}
                    _, cost_value, embedding, en_int, de_outs, loss_in = sess.run(
                        [optimizer, loss, enc_state, encoder_inputs, dec_outputs, loss_inputs], feed_dict=feed)

                    total_cost += cost_value
                    data_count += 1

                    if data_count % 1000 == 0:
                        print epoch, data_count, total_cost / data_count, datetime.datetime.now()

                print total_cost / data_count

#       print 'Dump vectors'
#       vectors = []
#       with open(output_fname, 'w') as fo:
#           with open(train_fname) as f:
#               for line in f:
#                   data = eval(line)
#                   length = len(data)

#                   if length < max_length:
#                       data.extend(default_features * (max_length-length))
#                   if length > max_length:
#                       data = data[:max_length]
#                       length = max_length

#                   x = np.array(data)
#                   x = x.reshape((max_length, batch_size, feature_count))

#                   embedding = None
#                   feed = {seq_input: x, input_length: [length]}
#                   _, cost_value, embedding, en_int, de_outs, loss_in = sess.run(
#                       [optimizer, loss, enc_state, encoder_inputs, dec_outputs, loss_inputs], feed_dict=feed)
#                   fo.write('%s\n' % ' '.join(map(str, embedding[0][0])))

        print 'Dump test vectors'
        vectors = []
        with open(test_output_fname, 'w') as fo:
            with open(test_fname) as f:
                for line in f:
                    data = eval(line)
                    length = len(data)

                    if length < max_length:
                        data.extend(default_features * (max_length-length))
                    if length > max_length:
                        data = data[:max_length]
                        length = max_length

                    x = np.array(data)
                    x = x.reshape((max_length, batch_size, feature_count))

                    embedding = None
                    feed = {seq_input: x, input_length: [length]}
                    _, cost_value, embedding, en_int, de_outs, loss_in = sess.run(
                        [optimizer, loss, enc_state, encoder_inputs, dec_outputs, loss_inputs], feed_dict=feed)
                    fo.write('%s\n' % ' '.join(map(str, embedding[0][0])))

        print 'Dump test vectors'
        vectors = []
        with open(test_output_fname2, 'w') as fo:
            with open(test_fname2) as f:
                for line in f:
                    data = eval(line)
                    length = len(data)

                    if length < max_length:
                        data.extend(default_features * (max_length-length))
                    if length > max_length:
                        data = data[:max_length]
                        length = max_length

                    x = np.array(data)
                    x = x.reshape((max_length, batch_size, feature_count))

                    embedding = None
                    feed = {seq_input: x, input_length: [length]}
                    _, cost_value, embedding, en_int, de_outs, loss_in = sess.run(
                        [optimizer, loss, enc_state, encoder_inputs, dec_outputs, loss_inputs], feed_dict=feed)
                    fo.write('%s\n' % ' '.join(map(str, embedding[0][0])))


def main(train_fname, test_fname, test_output_fname, test_fname2, test_output_fname2, options):
    '''\
    %prog [options] <train_fname> <output_fname>
    '''
    learn(train_fname, test_fname, test_output_fname, test_fname2, test_output_fname2)
    return 0


if __name__ == '__main__':
    parser = optparse.OptionParser(usage=main.__doc__)
    options, args = parser.parse_args()

    if len(args) != 5:
        parser.print_help()
        sys.exit()

    sys.exit(main(args[0], args[1], args[2], args[3], args[4], options))
