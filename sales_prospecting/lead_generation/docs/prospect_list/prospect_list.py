"""Doc runtime hooks for prospect_list."""

class DocRuntime:
    doc_key = "prospect_list"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'activate', 'close', 'archive']
