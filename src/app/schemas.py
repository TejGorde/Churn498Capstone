"""
Pydantic response and request models for Retain API.

Every endpoint has a typed schema. TypeScript mirrors live in
frontend/src/types/api.ts.
"""

from pydantic import BaseModel, ConfigDict


# =============================================================================
# Dashboard
# =============================================================================


class KPIResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    total_accounts: int
    active_subscribers: int
    churned_accounts: int
    churn_rate_30d: float
    high_risk_count: int
    at_risk_mrr: float
    cac: float
    retention_cost_per_save: float


class TrendPoint(BaseModel):
    label: str
    value: int
    predicted: int | None = None


class RiskDistribution(BaseModel):
    low: int
    medium: int
    high: int


class ActiveInactiveDistribution(BaseModel):
    active: int
    inactive: int
    recent_churn_30d: int


class AgentInsight(BaseModel):
    title: str
    content: str
    timestamp: str | None = None


# =============================================================================
# Accounts
# =============================================================================


class AccountAtRisk(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    account_id: str
    email: str
    churn_probability: float
    risk_tier: str
    plan_type: str
    tenure_days: int
    last_payment_days: int
    last_stream_days: int
    open_tickets: int
    top_drivers: list[str]


class PaginatedAccounts(BaseModel):
    items: list[AccountAtRisk]
    total: int
    page: int
    per_page: int


class PaymentRecord(BaseModel):
    date: str
    amount: float
    status: str
    method: str


class TicketRecord(BaseModel):
    id: str
    date: str
    subject: str
    status: str
    priority: str


class SHAPFeature(BaseModel):
    feature: str
    importance: float
    direction: str


class AccountDetail(AccountAtRisk):
    recent_payments: list[PaymentRecord]
    recent_tickets: list[TicketRecord]
    watch_hours_30d: float
    watch_hours_90d: float
    sessions_30d: int
    content_categories: list[str]


# =============================================================================
# Analytics
# =============================================================================


class PlanBreakdown(BaseModel):
    plan: str
    count: int
    churn_rate: float


class SegmentBreakdown(BaseModel):
    by_plan: list[PlanBreakdown]
    by_tenure: list[PlanBreakdown]


class ModelMetrics(BaseModel):
    auc_roc: float
    precision: float
    recall: float
    f1_score: float
    log_loss: float
    calibration_error: float
    last_trained: str
    training_samples: int


class DriftFeature(BaseModel):
    feature: str
    psi: float
    status: str


class DriftStatus(BaseModel):
    overall_status: str
    features: list[DriftFeature]
    last_checked: str


class AnalyticsOverview(BaseModel):
    kpis: KPIResponse
    risk_distribution: RiskDistribution
    top_shap_features: list[SHAPFeature]


# =============================================================================
# Prescriptions
# =============================================================================


class PrescriptionGroup(BaseModel):
    strategy: str
    display_name: str
    account_count: int
    estimated_mrr: float
    accounts: list[AccountAtRisk]


# =============================================================================
# Interventions
# =============================================================================


class InterventionDraft(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    account_id: str
    strategy: str
    status: str
    subject: str
    body_html: str
    body_plaintext: str
    agent_rationale: str
    created_at: str
    updated_at: str


class DraftRequest(BaseModel):
    account_id: str
    strategy: str


class BatchDraftRequest(BaseModel):
    account_ids: list[str]
    strategy: str


class StatusUpdateRequest(BaseModel):
    status: str


class ContentUpdateRequest(BaseModel):
    subject: str | None = None
    body: str | None = None


# =============================================================================
# Agents
# =============================================================================


class AgentTriggerResponse(BaseModel):
    run_id: str
    status: str


class AgentStatusResponse(BaseModel):
    run_id: str
    status: str
    result: dict | None = None


# =============================================================================
# System
# =============================================================================


class HealthResponse(BaseModel):
    status: str
    demo_mode: bool
    db_connected: bool


class ErrorResponse(BaseModel):
    error: str
    detail: str | None = None
