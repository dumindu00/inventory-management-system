"""add transaction_type to inventory_transactions

Revision ID: 79163b1b0b73
Revises: 570075bc1669
Create Date: 2026-01-27 14:40:42.213030

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '79163b1b0b73'
down_revision: Union[str, Sequence[str], None] = '570075bc1669'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column(
        "inventory_transactions",
        sa.Column("transaction_type", sa.String(length=20), nullable=False)
    )


def downgrade():
    op.drop_column("inventory_transactions", "transaction_type")