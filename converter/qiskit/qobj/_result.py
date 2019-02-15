


from converter.qiskit.qobj import QobjItem


class Result(QobjItem):
    pass




    def __init__(self, backend_name, backend_version, qobj_id, job_id,
                 success, results, **kwargs):
        pass



class ExperimentResult(QobjItem):
    pass




    def __init__(self, success, shots, data, **kwargs):
        pass

