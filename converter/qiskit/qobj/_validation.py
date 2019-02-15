



from converter.qiskit import _schema_validation
from converter.qiskit import _qiskiterror


class QobjValidationError(_qiskiterror.QISKitError):
    pass


def validate_qobj_against_schema(qobj):
    pass
