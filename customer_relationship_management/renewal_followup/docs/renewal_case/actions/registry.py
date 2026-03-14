"""Action registry seed for renewal_case."""

from __future__ import annotations


DOC_ID = "renewal_case"
ALLOWED_ACTIONS = ['create', 'assign', 'review', 'renew', 'lose', 'close', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['open', 'in_review', 'renewed', 'lost'], 'transitions_to': None}, 'assign': {'allowed_in_states': ['open', 'in_review', 'renewed', 'lost'], 'transitions_to': 'in_review'}, 'review': {'allowed_in_states': ['open', 'in_review', 'renewed', 'lost'], 'transitions_to': 'in_review'}, 'renew': {'allowed_in_states': ['open', 'in_review', 'renewed', 'lost'], 'transitions_to': 'renewed'}, 'lose': {'allowed_in_states': ['open', 'in_review', 'renewed', 'lost'], 'transitions_to': None}, 'close': {'allowed_in_states': ['open', 'in_review', 'renewed', 'lost'], 'transitions_to': 'closed'}, 'archive': {'allowed_in_states': ['open', 'in_review', 'renewed', 'lost'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'

def get_action_handler_name(action_id: str) -> str:
    return f"handle_{action_id}"

def get_action_module_path(action_id: str) -> str:
    return f"actions/{action_id}.py"

def action_contract(action_id: str) -> dict:
    return {
        "state_field": STATE_FIELD,
        "rule": ACTION_RULES.get(action_id, {}),
    }
