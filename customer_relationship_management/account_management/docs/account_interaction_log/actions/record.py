"""Action handler seed for account_interaction_log:record."""

from __future__ import annotations


DOC_ID = "account_interaction_log"
ACTION_ID = "record"
ACTION_RULE = {'allowed_in_states': ['active'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'capture account touchpoints, preserve relationship history, and hand off follow-up work to the right owner', 'actors': ['account manager', 'support representative', 'sales manager'], 'start_condition': 'an account interaction or follow-up event occurs', 'ordered_steps': ['Record the interaction.', 'Review the follow-up requirement.', 'Archive when the interaction history is no longer active.'], 'primary_actions': ['record', 'review', 'archive'], 'action_actors': {'record': ['account manager', 'support representative'], 'review': ['sales manager'], 'archive': ['account manager']}, 'primary_transitions': ['account_interaction_log: active -> archived'], 'downstream_effects': ['supports customer-account follow-up, renewal visibility, and relationship audit history']}

def handle_record(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = ACTION_RULE.get("transitions_to")
    updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
    return {
        "doc_id": DOC_ID,
        "action_id": ACTION_ID,
        "payload": payload,
        "context": context,
        "allowed_in_states": ACTION_RULE.get("allowed_in_states", []),
        "next_state": next_state,
        "updates": updates,
        "workflow_objective": WORKFLOW_HINTS.get("business_objective"),
    }
