"""Action handler seed for customer_account:create."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "customer_account"
ACTION_ID = "create"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['active', 'inactive'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'maintain active customer relationships with a clear history of interactions, satisfaction, and growth plans', 'actors': ['account manager', 'support owner', 'customer-success lead'], 'start_condition': 'a customer relationship must be created or maintained', 'ordered_steps': ['Create or update the customer account.'], 'primary_actions': ['create', 'update', 'review'], 'primary_transitions': ['customer_account: draft -> active'], 'downstream_effects': ['supports collections, service recovery, and revenue growth planning'], 'action_actors': {'create': ['account manager'], 'update': ['account manager'], 'review': ['support owner'], 'archive': ['support owner']}}

def handle_create(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = cast(str | None, ACTION_RULE.get("transitions_to"))
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
