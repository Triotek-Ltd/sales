"""Action handler seed for deal_negotiation_case:agree."""

from __future__ import annotations


DOC_ID = "deal_negotiation_case"
ACTION_ID = "agree"
ACTION_RULE = {'allowed_in_states': ['open', 'negotiating', 'agreed', 'lost'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['quote_record', 'opportunity_record', 'pricing_exception_request'], 'borrowed_fields': ['commercial terms from quote_record', 'deal value from opportunity_record'], 'inferred_roles': ['account owner', 'case owner']}, 'actors': ['account owner', 'case owner'], 'action_actors': {'create': ['account owner'], 'assign': ['account owner'], 'review': ['case owner'], 'close': ['account owner'], 'archive': ['account owner']}}

def handle_agree(payload: dict, context: dict | None = None) -> dict:
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
