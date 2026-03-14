"""Doc runtime hooks for lead_record."""

class DocRuntime:
    doc_key = "lead_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'assign', 'qualify', 'disqualify', 'archive']
