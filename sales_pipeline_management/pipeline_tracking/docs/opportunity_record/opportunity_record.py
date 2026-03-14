"""Doc runtime hooks for opportunity_record."""

class DocRuntime:
    doc_key = "opportunity_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'advance', 'win', 'lose', 'archive']
