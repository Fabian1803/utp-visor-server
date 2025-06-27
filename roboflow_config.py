from roboflow import Roboflow

def load_model():
    rf = Roboflow(api_key="rLyWOJGnNULZrutusRfT")
    project = rf.workspace("utpvisor").project("custom-workflow-object-detection-qmeim")
    version = project.version(1)
    model = version.model
    print("roboflow_config.py cargado")
    return model
