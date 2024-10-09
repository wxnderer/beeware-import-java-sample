from java import jclass

def get_onnxruntime_version():
    OrtEnvironment = jclass('ai.onnxruntime.OrtEnvironment')
    env = OrtEnvironment.getEnvironment()
    version = env.getVersion()
    return version
