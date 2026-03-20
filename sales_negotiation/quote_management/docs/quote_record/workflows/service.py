"""Workflow service seed for quote_record."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "quote_record"
ARCHETYPE = "transaction"
INITIAL_STATE = 'draft'
STATES = ['draft', 'submitted', 'approved', 'accepted', 'expired', 'cancelled', 'archived']
TERMINAL_STATES = ['archived']
ACTION_RULES: dict[str, dict[str, Any]] = {'create': {'allowed_in_states': ['draft', 'submitted', 'approved', 'accepted', 'expired', 'cancelled'], 'transitions_to': None}, 'review': {'allowed_in_states': ['draft', 'submitted', 'approved', 'accepted', 'expired', 'cancelled'], 'transitions_to': None}, 'approve': {'allowed_in_states': ['draft', 'submitted', 'approved', 'accepted', 'expired', 'cancelled'], 'transitions_to': 'approved'}, 'issue': {'allowed_in_states': ['approved'], 'transitions_to': None}, 'accept': {'allowed_in_states': ['draft', 'submitted', 'approved', 'accepted', 'expired', 'cancelled'], 'transitions_to': None}, 'expire': {'allowed_in_states': ['draft', 'submitted', 'approved', 'accepted', 'expired', 'cancelled'], 'transitions_to': None}, 'cancel': {'allowed_in_states': ['draft', 'submitted', 'approved', 'accepted', 'expired', 'cancelled'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['draft', 'submitted', 'approved', 'accepted', 'expired', 'cancelled'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'manage proposal revisions, negotiation decisions, and final agreement closure with a prospect', 'actors': ['sales rep', 'approver', 'customer negotiator'], 'start_condition': 'a proposal is presented to a prospect', 'ordered_steps': ['Issue the sales proposal and opening quote.', 'Revise quote and commercial terms as needed.'], 'primary_actions': ['create', 'review', 'issue', 'update', 'approve'], 'primary_transitions': ['quote_record: draft -> active', 'quote_record: active -> revised -> approved'], 'downstream_effects': ['feeds order capture, billing, and relationship management'], 'action_actors': {'create': ['sales rep'], 'review': ['approver'], 'approve': ['approver'], 'issue': ['sales rep'], 'cancel': ['sales rep'], 'archive': ['sales rep']}}

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
        return cast(str | None, rule.get("transitions_to"))

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
