"""Doc runtime hooks for deal_negotiation_case."""

class DocRuntime:
    doc_key = "deal_negotiation_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'review', 'counter', 'agree', 'lose', 'close', 'archive']
