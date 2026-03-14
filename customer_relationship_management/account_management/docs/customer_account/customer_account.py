"""Doc runtime hooks for customer_account."""

class DocRuntime:
    doc_key = "customer_account"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'archive']
