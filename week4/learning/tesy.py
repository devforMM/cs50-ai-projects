import tensorflow as tf

print("TensorFlow version:", tf.__version__)
print("CUDA enabled:", tf.test.is_built_with_cuda())
print("cuDNN enabled:", tf.test.is_built_with_cuda())
print("GPUs disponibles:", tf.config.list_physical_devices('GPU'))
