"""Doc runtime hooks for contact_record."""

class DocRuntime:
    doc_key = "contact_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'archive']
