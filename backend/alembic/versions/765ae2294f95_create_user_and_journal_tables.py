"""Create user and journal tables

Revision ID: 765ae2294f95
Revises: 04c2cdaa5564
Create Date: 2024-07-11 06:19:37.857648

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '765ae2294f95'
down_revision: Union[str, None] = '04c2cdaa5564'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###