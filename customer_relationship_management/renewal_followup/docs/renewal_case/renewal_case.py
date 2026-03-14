"""Doc runtime hooks for renewal_case."""

class DocRuntime:
    doc_key = "renewal_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'review', 'renew', 'lose', 'close', 'archive']
