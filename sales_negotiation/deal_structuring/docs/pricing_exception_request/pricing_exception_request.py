"""Doc runtime hooks for pricing_exception_request."""

class DocRuntime:
    doc_key = "pricing_exception_request"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'submit', 'review', 'approve', 'reject', 'close', 'archive']
