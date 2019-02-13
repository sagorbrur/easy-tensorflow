# import tensorflwo
import tensorflow as tf

#Graph Part
x = 2
y = 3
#simple mathematical operation using tensorflow
add_op = tf.add(x, y, name='Add')
mul_op = tf.multiply(x, y, name='Multiply')
pow_op = tf.pow(add_op, mul_op, name='Power')
useless_op = tf.multiply(x, add_op, name='Useless')

#Session Part
with tf.Session() as sess:
    pow_out, useless_out = sess.run([pow_op, useless_op])
    # to visualize tensorboard
    # run: tensorboard --logdir=graph --port=6006
    writer = tf.summary.FileWriter('/graph', sess.graph)
