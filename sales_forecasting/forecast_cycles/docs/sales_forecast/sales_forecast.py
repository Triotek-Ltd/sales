"""Doc runtime hooks for sales_forecast."""

class DocRuntime:
    doc_key = "sales_forecast"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'commit', 'revise', 'archive']
