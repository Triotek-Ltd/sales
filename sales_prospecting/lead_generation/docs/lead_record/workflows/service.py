"""Workflow service seed for lead_record."""

from __future__ import annotations


DOC_ID = "lead_record"
ARCHETYPE = "master"
INITIAL_STATE = 'new'
STATES = ['new', 'contacted', 'qualified', 'disqualified', 'archived']
TERMINAL_STATES = ['archived']
ACTION_RULES = {'create': {'allowed_in_states': ['new', 'contacted', 'qualified', 'disqualified'], 'transitions_to': None}, 'update': {'allowed_in_states': ['new', 'contacted', 'qualified', 'disqualified'], 'transitions_to': None}, 'assign': {'allowed_in_states': ['new', 'contacted', 'qualified', 'disqualified'], 'transitions_to': None}, 'qualify': {'allowed_in_states': ['new', 'contacted', 'qualified', 'disqualified'], 'transitions_to': None}, 'disqualify': {'allowed_in_states': ['new', 'contacted', 'qualified', 'disqualified'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['new', 'contacted', 'qualified', 'disqualified'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'turn raw prospects into qualified leads with documented outreach and qualification evidence', 'actors': ['sales rep', 'sales manager', 'reviewer'], 'start_condition': 'a target customer or lead source is identified', 'ordered_steps': ['Capture the lead and basic prospect context.', 'Advance qualified prospects into opportunity management.'], 'primary_actions': ['create', 'update', 'convert', 'close'], 'primary_transitions': ['lead_record: draft -> active', 'lead_record: active -> qualified -> converted'], 'downstream_effects': ['feeds opportunity, negotiation, and forecast workflows']}

class WorkflowService:
    def allowed_actions_for_state(self, state: str | None) -> list[str]:
        if not state:
            return list(ACTION_RULES.keys())
        allowed = []
        for action_id, rule in ACTION_RULES.items():
            states = rule.get("allowed_in_states") or []
            if not states or state in states:
                allowed.append(action_id)
        return allowed

    def is_action_allowed(self, action_id: str, state: str | None) -> bool:
        return action_id in self.allowed_actions_for_state(state)

    def next_state_for(self, action_id: str) -> str | None:
        rule = ACTION_RULES.get(action_id, {})
        return rule.get("transitions_to")

    def apply_action(self, action_id: str, state: str | None) -> dict:
        if not self.is_action_allowed(action_id, state):
            raise ValueError(f"Action '{action_id}' is not allowed in state '{state}'")
        next_state = self.next_state_for(action_id)
        updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
        return {
            "action_id": action_id,
            "current_state": state,
            "next_state": next_state,
            "updates": updates,
        }

    def is_terminal(self, state: str | None) -> bool:
        return bool(state and state in TERMINAL_STATES)

    def workflow_summary(self) -> dict:
        return {
            "initial_state": INITIAL_STATE,
            "states": STATES,
            "terminal_states": TERMINAL_STATES,
            "business_objective": WORKFLOW_HINTS.get("business_objective"),
            "ordered_steps": WORKFLOW_HINTS.get("ordered_steps", []),
        }

    def workflow_profile(self) -> dict:
        return {'mode': 'entity_lifecycle', 'case_management': False}
