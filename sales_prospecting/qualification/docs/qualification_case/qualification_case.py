"""Doc runtime hooks for qualification_case."""

class DocRuntime:
    doc_key = "qualification_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'review', 'qualify', 'disqualify', 'close', 'archive']
