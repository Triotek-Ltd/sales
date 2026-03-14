"""Doc runtime hooks for outreach_activity."""

class DocRuntime:
    doc_key = "outreach_activity"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'review', 'archive']
