import tensorflow as tf
import os
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

# load dataset MNIST
mnist = input_data.read_data_sets("./data/", one_hot=True)

# Define graph for MLP
# Define placeholders, variables
x = tf.placeholder(dtype=tf.float32, shape=(None, 784))
y = tf.placeholder(dtype=tf.float32, shape=(None, 10))

W1 = tf.get_variable(name='h1_weight', shape=(784, 256))
b1 = tf.get_variable(name='h1_bias', shape=256)

W2 = tf.get_variable(name='h2_weight', shape=(256, 256))
b2 = tf.get_variable(name='h2_bias', shape=256)

W3 = tf.get_variable(name='h3_weight', shape=(256, 10))
b3 = tf.get_variable(name='h3_bias', shape=10)

# Assemble graph
layer1 = tf.add(tf.matmul(x, W1), b1)
layer1_relu = tf.nn.leaky_relu(layer1)

layer2 = tf.add(tf.matmul(layer1_relu, W2), b2)
layer2_relu = tf.nn.leaky_relu(layer2)

layer3 = tf.add(tf.matmul(layer2_relu, W3), b3)
layer3_sigmoid = tf.nn.sigmoid(layer3)

# Define loss function
loss_op = tf.reduce_mean(tf.losses.softmax_cross_entropy(onehot_labels=y, logits=layer3_sigmoid))
tf.summary.scalar("loss", loss_op)

# Define metric to calculate training accuracy
correct_prediction = tf.equal(tf.argmax(layer3_sigmoid, 1), tf.argmax(y, 1))
# Calculate accuracy
accuracy_op = tf.reduce_mean(tf.cast(correct_prediction, "float"))
tf.summary.scalar("training_accuracy", accuracy_op)

# Define optimizer
train_op = tf.train.AdamOptimizer(learning_rate=0.001).minimize(loss_op)

# define a initializer for variables
init = tf.global_variables_initializer()

summary_op = tf.summary.merge_all()
saver = tf.train.Saver()

iter = 0
batch_size = 100

with tf.Session() as sess:
    # check whether there is checkpoint or not
    ckpt = tf.train.get_checkpoint_state('./checkpoints/')
    if ckpt:
        saver.restore(sess, './checkpoints/-38000')
        print("Successfully restored model")
    else:
        # initiate all variables
        sess.run(init)

    writer = tf.summary.FileWriter('./graphs', sess.graph)

    for iter in range(40000):
        batch_x, batch_y = mnist.train.next_batch(batch_size)
        # Run optimization op
        _, loss, tr_acc = sess.run([train_op, loss_op, accuracy_op], feed_dict={x: batch_x, y: batch_y})

        if iter % 100 == 0:
            print("Iter %d: loss %f, train_accuracy %f" % (iter, loss, tr_acc))
            summary = sess.run(summary_op, feed_dict={x: batch_x, y: batch_y})
            writer.add_summary(summary, iter)

            if iter % 2000 == 0:
                saver.save(sess, './checkpoints/', global_step=iter)
