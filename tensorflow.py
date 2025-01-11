import tensorflow as tf


# Simple TensorFlow constant
hello = tf.constant("Hello, TensorFlow!")
with tf.compat.v1.Session() as sess;
    result = sess.run(hello)
    print(hello.decode())
