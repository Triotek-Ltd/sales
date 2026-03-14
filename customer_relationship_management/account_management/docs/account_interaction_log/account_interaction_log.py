"""Doc runtime hooks for account_interaction_log."""

class DocRuntime:
    doc_key = "account_interaction_log"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'review', 'archive']
