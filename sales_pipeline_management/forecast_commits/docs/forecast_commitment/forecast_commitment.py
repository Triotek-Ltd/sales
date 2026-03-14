"""Doc runtime hooks for forecast_commitment."""

class DocRuntime:
    doc_key = "forecast_commitment"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'commit', 'revise', 'archive']
