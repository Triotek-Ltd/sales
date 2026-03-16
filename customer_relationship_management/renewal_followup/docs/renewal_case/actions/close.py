"""Action handler seed for renewal_case:close."""

from __future__ import annotations


DOC_ID = "renewal_case"
ACTION_ID = "close"
ACTION_RULE = {'allowed_in_states': ['open', 'in_review', 'renewed', 'lost'], 'transitions_to': 'closed'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['customer_account', 'account_interaction_log', 'quote_record'], 'borrowed_fields': ['account', 'commercial context from linked account/quote records'], 'inferred_roles': ['account owner', 'case owner']}, 'actors': ['account owner', 'case owner'], 'action_actors': {'create': ['account owner'], 'assign': ['account owner'], 'review': ['case owner'], 'close': ['account owner'], 'archive': ['account owner']}}

def handle_close(payload: dict, context: dict | None = None) -> dict:
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
