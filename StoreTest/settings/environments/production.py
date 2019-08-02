import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://48569c40c86b47be8013bcb53f04019f@sentry.io/1520119",
    integrations=[DjangoIntegration()]
)
