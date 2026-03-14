"""Doc runtime hooks for target_plan."""

class DocRuntime:
    doc_key = "target_plan"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'approve', 'archive']
