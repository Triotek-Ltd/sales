"""Workflow service seed for forecast_commitment."""

from __future__ import annotations


DOC_ID = "forecast_commitment"
ARCHETYPE = "transaction"
INITIAL_STATE = 'draft'
STATES = ['draft', 'reviewed', 'committed', 'revised', 'archived']
TERMINAL_STATES = ['archived']
ACTION_RULES = {'create': {'allowed_in_states': ['draft', 'reviewed', 'committed', 'revised'], 'transitions_to': None}, 'review': {'allowed_in_states': ['draft', 'reviewed', 'committed', 'revised'], 'transitions_to': 'reviewed'}, 'commit': {'allowed_in_states': ['draft', 'reviewed', 'committed', 'revised'], 'transitions_to': None}, 'revise': {'allowed_in_states': ['draft', 'reviewed', 'committed', 'revised'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['draft', 'reviewed', 'committed', 'revised'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'translate historical performance, market signals, and pipeline opportunity data into forecast commitments and management targets', 'actors': ['sales manager', 'sales operations analyst', 'team lead', 'management reviewer'], 'start_condition': 'a new forecast period is opened', 'ordered_steps': ['Collect pipeline, history, and demand inputs.'], 'primary_actions': ['create', 'review', 'commit'], 'primary_transitions': ['forecast_commitment: draft -> reviewed -> committed'], 'downstream_effects': ['feeds production planning, demand planning, budgeting, and management reporting']}

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
        return {'mode': 'transaction_flow', 'supports_submission': True}
