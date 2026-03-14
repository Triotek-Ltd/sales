"""Doc runtime hooks for forecast_review."""

class DocRuntime:
    doc_key = "forecast_review"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'schedule', 'complete', 'close', 'archive']
