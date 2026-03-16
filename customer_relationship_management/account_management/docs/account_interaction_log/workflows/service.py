"""Workflow service seed for account_interaction_log."""

from __future__ import annotations


DOC_ID = "account_interaction_log"
ARCHETYPE = "ledger"
INITIAL_STATE = 'active'
STATES = ['active', 'archived']
TERMINAL_STATES = ['archived']
ACTION_RULES = {'record': {'allowed_in_states': ['active'], 'transitions_to': None}, 'review': {'allowed_in_states': ['active'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['active'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'capture account touchpoints, preserve relationship history, and hand off follow-up work to the right owner', 'actors': ['account manager', 'support representative', 'sales manager'], 'start_condition': 'an account interaction or follow-up event occurs', 'ordered_steps': ['Record the interaction.', 'Review the follow-up requirement.', 'Archive when the interaction history is no longer active.'], 'primary_actions': ['record', 'review', 'archive'], 'action_actors': {'record': ['account manager', 'support representative'], 'review': ['sales manager'], 'archive': ['account manager']}, 'primary_transitions': ['account_interaction_log: active -> archived'], 'downstream_effects': ['supports customer-account follow-up, renewal visibility, and relationship audit history']}

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
        return {'mode': 'posting_flow', 'supports_reconciliation': True}
