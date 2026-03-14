"""Doc runtime hooks for quote_record."""

class DocRuntime:
    doc_key = "quote_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'issue', 'accept', 'expire', 'cancel', 'archive']
