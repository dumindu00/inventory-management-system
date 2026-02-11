"""add reference to inventory_transactions

Revision ID: 1f23ccc9b5a5
Revises: 79163b1b0b73
Create Date: 2026-01-27 14:46:55.867257

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1f23ccc9b5a5'
down_revision: Union[str, Sequence[str], None] = '79163b1b0b73'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
     op.add_column(
        "inventory_transactions",
        sa.Column("reference", sa.String(length=50), nullable=False)
    )


def downgrade():
     op.drop_column("inventory_transactions", "reference")
