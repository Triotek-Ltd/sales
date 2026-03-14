"""Doc runtime hooks for forecast_line."""

class DocRuntime:
    doc_key = "forecast_line"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'review', 'archive']
