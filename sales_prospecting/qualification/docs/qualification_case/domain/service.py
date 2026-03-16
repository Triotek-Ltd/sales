"""Business-domain service seed for Qualification Case."""

from __future__ import annotations


ARCHETYPE_PROFILE = {'workflow_profile': {'mode': 'case_flow', 'supports_assignment': True, 'supports_escalation': True}, 'reporting_profile': {'supports_snapshots': True, 'supports_outputs': False}, 'integration_profile': {'external_sync_enabled': False}, 'lifecycle_states': ['open', 'in_review', 'qualified', 'disqualified', 'closed', 'archived'], 'is_transactional': False}

CONTRACT = {'title_field': 'title', 'status_field': 'workflow_state', 'reference_field': 'reference_no', 'required_fields': ['title', 'workflow_state'], 'field_purposes': {'workflow_state': 'lifecycle_state', 'owner': 'actor_reference', 'related_outreach_activity': 'relation_collection', 'related_opportunity_record': 'relation_collection'}, 'search_fields': ['title', 'reference_no', 'description', 'case_code', 'lead', 'qualification_criteria'], 'list_columns': ['title', 'reference_no', 'workflow_state', 'modified'], 'initial_state': 'open', 'lifecycle_states': ['open', 'in_review', 'qualified', 'disqualified', 'closed', 'archived'], 'terminal_states': ['closed', 'archived'], 'action_targets': {'create': None, 'assign': 'in_review', 'review': 'in_review', 'qualify': None, 'disqualify': None, 'close': 'closed', 'archive': 'archived'}}

WORKFLOW_HINTS = {'business_objective': 'turn raw prospects into qualified leads with documented outreach and qualification evidence', 'actors': ['sales rep', 'sales manager', 'reviewer'], 'start_condition': 'a target customer or lead source is identified', 'ordered_steps': ['Open and progress the qualification case.'], 'primary_actions': ['create', 'assign', 'qualify', 'disqualify', 'close'], 'primary_transitions': ['qualification_case: opened -> in_review -> qualified or disqualified -> closed'], 'downstream_effects': ['feeds opportunity, negotiation, and forecast workflows'], 'action_actors': {'create': ['sales rep'], 'assign': ['sales rep'], 'review': ['reviewer'], 'close': ['sales manager'], 'archive': ['sales manager']}}

SIDE_EFFECT_HINTS = {'downstream_effects': ['feeds opportunity, negotiation, and forecast workflows'], 'related_docs': ['lead_record', 'outreach_activity', 'opportunity_record'], 'action_targets': {'create': None, 'assign': 'in_review', 'review': 'in_review', 'qualify': None, 'disqualify': None, 'close': 'closed', 'archive': 'archived'}, 'action_side_effects_file': 'side_effects.json'}

class DomainService:
    doc_id = "qualification_case"
    archetype = "workflow_case"
    doc_kind = "workflow_case"

    def required_fields(self) -> list[str]:
        return CONTRACT.get("required_fields", [])

    def state_field(self) -> str | None:
        return CONTRACT.get("status_field")

    def default_state(self) -> str | None:
        return CONTRACT.get("initial_state")

    def list_columns(self) -> list[str]:
        return CONTRACT.get("list_columns", [])

    def validate_invariants(self, payload: dict, *, partial: bool = False) -> dict:
        if partial:
            required_scope = [field for field in self.required_fields() if field in payload]
        else:
            required_scope = self.required_fields()
        missing_fields = [field for field in required_scope if not payload.get(field)]
        if missing_fields:
            raise ValueError(f"Missing required business fields: {', '.join(missing_fields)}")
        state_field = self.state_field()
        allowed_states = set(CONTRACT.get("lifecycle_states", []))
        if state_field and payload.get(state_field) and allowed_states and payload[state_field] not in allowed_states:
            raise ValueError(f"Invalid state '{payload[state_field]}' for {state_field}")
        return payload

    def prepare_create_payload(self, payload: dict, context: dict | None = None) -> dict:
        payload = dict(payload)
        state_field = self.state_field()
        if state_field and not payload.get(state_field) and self.default_state():
            payload[state_field] = self.default_state()
        title_field = CONTRACT.get("title_field")
        reference_field = CONTRACT.get("reference_field")
        if title_field and not payload.get(title_field) and reference_field and payload.get(reference_field):
            payload[title_field] = str(payload[reference_field])
        payload = self.validate_invariants(payload)
        return payload

    def after_create(self, instance, serialized_data: dict, context: dict | None = None) -> dict:
        return serialized_data

    def prepare_update_payload(self, instance, payload: dict, context: dict | None = None) -> dict:
        payload = dict(payload)
        payload = self.validate_invariants(payload, partial=True)
        return payload

    def after_update(self, instance, serialized_data: dict, context: dict | None = None) -> dict:
        return serialized_data

    def after_action(
        self,
        instance,
        action_id: str,
        payload: dict,
        action_result: dict,
        context: dict | None = None,
    ) -> dict:
        return {
            "updates": {},
            "side_effects": [],
        }

    def shape_retrieve_data(self, instance, serialized_data: dict, context: dict | None = None) -> dict:
        serialized_data.setdefault("_business_capabilities", self.business_capabilities())
        return serialized_data

    def workflow_objective(self) -> str | None:
        return WORKFLOW_HINTS.get("business_objective")

    def side_effect_hints(self) -> dict:
        return SIDE_EFFECT_HINTS

    def business_capabilities(self) -> dict:
        return {
            **ARCHETYPE_PROFILE,
            "required_fields": self.required_fields(),
            "state_field": self.state_field(),
            "default_state": self.default_state(),
        }
