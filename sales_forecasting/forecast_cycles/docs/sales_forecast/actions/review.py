"""Action handler seed for sales_forecast:review."""

from __future__ import annotations


DOC_ID = "sales_forecast"
ACTION_ID = "review"
ACTION_RULE = {'allowed_in_states': ['draft', 'reviewed', 'committed', 'revised'], 'transitions_to': 'reviewed'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'translate historical performance, market signals, and pipeline opportunity data into forecast commitments and management targets', 'actors': ['sales manager', 'sales operations analyst', 'team lead', 'management reviewer'], 'start_condition': 'a new forecast period is opened', 'ordered_steps': ['Create the forecast header for the period.', 'Approve and activate the forecast for operational use.'], 'primary_actions': ['create', 'review', 'approve', 'activate', 'revise'], 'primary_transitions': ['sales_forecast: draft', 'sales_forecast: draft -> reviewed -> committed or revised'], 'downstream_effects': ['feeds production planning, demand planning, budgeting, and management reporting'], 'action_actors': {'create': ['sales manager'], 'review': ['management reviewer'], 'archive': ['sales manager']}}

def handle_review(payload: dict, context: dict | None = None) -> dict:
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
