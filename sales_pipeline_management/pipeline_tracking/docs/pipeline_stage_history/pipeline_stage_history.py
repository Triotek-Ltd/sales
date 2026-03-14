"""Doc runtime hooks for pipeline_stage_history."""

class DocRuntime:
    doc_key = "pipeline_stage_history"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'archive']
